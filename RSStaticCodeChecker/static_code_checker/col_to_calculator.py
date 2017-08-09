def get_to_col_offset(node):
    """
    Checks the highest col offset in the nodes children.
    @param node: The JSON parsed AST for which the children should be checked
    @returns the highest value found for col_offset in the children
    """
    hco = get_highest_col_in_children(node)
    return hco

def get_highest_col_in_children(node):
    highest = 0
    if not isinstance(node, list) and not isinstance(node, dict):
        return 0
    if isinstance(node, list):
        for i,val in enumerate(node):
            highest = max(highest, get_highest_col_in_children(val))
    elif isinstance(node, dict):
        for key in node:
            highest = max(highest, get_highest_col_in_children(node[key]))
        if node.get("col_offset"):
            highest = max(highest, int(node.get("col_offset")))
    return highest