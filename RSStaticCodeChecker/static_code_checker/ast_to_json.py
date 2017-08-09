from _ast import AST
import ast
import json

def ast2json( node ):
    """
    Converting an ast (e.g. by ast.parse()) to a JSON file

    Original code here: https://github.com/ivan111/vpyast/blob/master/main.py

    @param node: The node that should be converted to JSON
    @returns: the json... obviously 
    """
    if not isinstance( node, AST ):
        raise TypeError( 'expected AST, got %r' % node.__class__.__name__ )


    def _format( node ):
        if isinstance( node, AST ):
            fields = [ ( '_PyType', _format( node.__class__.__name__ ) ) ]
            fields += [ ( a, _format( b ) ) for a, b in iter_fields( node ) ]
            if hasattr(node, "lineno"):
                fields += [ ( 'lineno', _format( node.lineno ) )]
            if hasattr(node, "col_offset"):
                fields += [ ( 'col_offset', _format( node.col_offset ) )]
            return '{ %s }' % ', '.join( ( '"%s": %s' % field for field in fields ) )

        if isinstance( node, list ):
            return '[ %s ]' % ', '.join( [ _format( x ) for x in node ] )

        return json.dumps( node, ensure_ascii=False )


    return _format( node )

def iter_fields( node ):
    for field in node._fields:
        try:
            yield field, getattr( node, field )
        except AttributeError:
            pass