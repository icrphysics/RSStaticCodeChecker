import sys
import importlib
from checker_config import config
import col_to_calculator

enable_printing = False
def results_for_dict(d, attribute_bases, wildcards, parents, percentage_from = 0, percentage_to = 0.5):
    """
    Returns a list of all results for an attribute_error in the given AST node.
    @param d: The dict that should be checked (json parsed ast_to_json node)
    @param attribute_bases: A list of all possible attribute combinations. Most likely a json.loads of the information/all_attributes.json file
    @param parents: A list of references to all parent dicts (if starting then insert empty list)
    @param percentage_from: The percentage start for this element. for a in {a:{b:1, c:2}, d:{e:5, f:3}} it would be 0.0
    @param percentage_to: The percentage to for this element. for a in {a:{b:1, c:2}, d:{e:5, f:3}} it would be 0.5
    @returns a list of all attribute errors in the given node
    """
    results = []
    if isinstance(d, dict):

        base_score, base_object_type = get_base_score(d)
        if base_score == sys.maxint:
            new_parents = list(parents)
            new_parents.append(d)

            percentage_start = percentage_from
            if len(d) > 0:
                percentage_addition = (percentage_to - percentage_from) / float(len(d))

            for k in d:
                results.extend(results_for_dict(d[k], attribute_bases, wildcards, new_parents, percentage_start, percentage_start+percentage_addition))
                percentage_start += percentage_addition
        else:
            new_parents = list(parents)
            parents_rev = new_parents[::-1]
            base = base_object_type
            left_over_attributes = filter(lambda x: x.startswith(base), attribute_bases)
            if not left_over_attributes:
                return results #should never happen
            for i, parent in enumerate(parents_rev):
                if not isinstance(parent, dict):
                    break
                else:
                    if isinstance(parent, dict) and parent.get("_PyType") == "Attribute":
                        base += ".{}".format(parent.get("attr"))
                        left_over_attributes = filter(lambda x: x.startswith(base), attribute_bases)
                        if not left_over_attributes and parent.get("attr") not in wildcards:
                            a = {
                                "score": (float(base_score)/float(i+1)),
                                "value": parent,
                                "error_type": "attribute_error",
                                "test_id": i,
                                "error_code": base
                            }
                            if d.get("lineno"):
                                a["lineno"] = d.get("lineno")
                            if d.get("col_offset"):
                                a["col_offset"] = d.get("col_offset")
                                a["col_offset_to"] = col_to_calculator.get_to_col_offset(a.get("value"))
                            results.append(a)
                            break
                    elif isinstance(parent, dict) and parent.get("_PyType") == "Subscript":
                        base1 = "{}.[]".format(base)
                        base2 = "{}.[]".format(base)
                        if parent.get("slice").get("_PyType") == "Index":
                            if parent.get("slice").get("value").get("_PyType") == "Str":
                                base2 = "{}.{}".format(base, parent.get("slice").get("value").get("s"))
                        left_over_attributes = filter(lambda x: x.startswith((base1, base2)), attribute_bases)
                        if not left_over_attributes and parent.get("attr") not in wildcards:
                            a = {
                                "score": (float(base_score)/float(i+1)),
                                "value": parent,
                                "error_type": "attribute_error",
                                "test_id": i,
                                "error_code": base2
                            }
                            if d.get("lineno"):
                                a["lineno"] = d.get("lineno")
                            if d.get("col_offset"):
                                a["col_offset"] = d.get("col_offset")
                                a["col_offset_to"] = col_to_calculator.get_to_col_offset(a.get("value"))

                            results.append(a)
                            break
                        else:
                            left_over_attributes_1 = filter(lambda x: x.startswith(base1), attribute_bases)
                            left_over_attributes_2 = filter(lambda x: x.startswith(base2), attribute_bases)
                            if left_over_attributes_1:
                                base = base1
                            else:
                                base = base2
                    else:
                        # It is something else. The left_over_attributes seem to be okay (because otherwise we wouldn't have come this far)
                        break

    elif isinstance(d, list):
        new_parents = list(parents)
        new_parents.append(d)
        percentage_start = percentage_from
        if len(d) > 0:
            percentage_addition = (percentage_to - percentage_from) / float(len(d))
        for k in d:
            results.extend(results_for_dict(k, attribute_bases, wildcards, new_parents, percentage_start, percentage_start+percentage_addition))
            percentage_start += percentage_addition

    if enable_printing:
        sys.stdout.write("\r")
        sys.stdout.write("{:.0%}".format(float(percentage_to)))
        sys.stdout.flush()

    return results

def get_base_score(d):
    """
    Gets the score and the base_type for the base of a dict.
    @param d: a dict that could be a base variable
    @returns a score for the given dict as well as the object_type that returned that score
    """
    if not isinstance(d, dict):
        return sys.maxint
    for object_type in config.get_object_types():
        module_name = "score_{}".format(object_type.replace(".", "_"))
        module = "generated.bases.{}".format(module_name)
        i = importlib.import_module(module)
        score = i.get_score(d)
        if score != sys.maxint:
            return score, object_type
    return sys.maxint, None
