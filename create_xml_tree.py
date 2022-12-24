
def find_children(children, tag, kwargs, result=[]):
    for child in children:
        if (child.tag == tag and child.attributes == kwargs):
            result.append(child)
        if (len(child.children)):
            find_children(child.children, tag, kwargs, result)
    return result


class XMLNode:
    def __init__(self, tag, attributes, children=[], content=None):
        self.tag = tag  # The tag <tag>
        self.attributes = attributes  # A dictionary from attributes to values
        # A list of either XMLNode objects and strings, corresponding to tags and text between them.
        self.children = children
        # A string of everything in the original document inside these tags
        self.content = content

    def __str__(self):
        return f'tag: {self.tag}, attributes: {self.attributes}'

    def find(self, tag, **kwargs):
        """
        Search for a given tag and atributes anywhere in the XML tree
        Args:
        tag (string): tag to match
        kwargs (dictionary): list of attribute name / attribute value 
        pairs to match
        Returns:
        (list): a list of XMLNode objects that match from anywhere in 
        the tree
        """
        return find_children(self.children, tag, kwargs)


def create_xml_tree():
    """parse an XML tree from a string"""

    return XMLNode('', {}, [
        XMLNode('', {}, [], '<!DOCTYPE xml>'),
        XMLNode('', {}, [], '<?xml version="1.0" encoding="UTF-8"?>'),
        XMLNode('', {}, [], 'This is a comment'),
        XMLNode('note', {'date': '8/31/12'}, [
            XMLNode('to', {}, [], "Tove"),
            XMLNode('from', {}, [], "Jani"),
            XMLNode('heading', {'type': 'Notification'}),
            XMLNode('heading', {'type': 'Reminder'}),
            XMLNode('body', {}, [], "Don't forget me this weekend!"),
            XMLNode(
                '', {}, [], "This is a multiline comment, which take a bit of care to parse"),
        ]),
    ])
