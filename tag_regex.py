import re

tag_open = re.compile("<(?!\?)(?!\!)(?!\/).+?(?<!\/)>")
tag_close = re.compile("<\/.*>")
tag_open_close = re.compile("<.*\/>")
comment = re.compile("(?s)<!--.*?-->")
xml_prolog = re.compile("<\?.*?\?>")
html_declaration = re.compile("<!DOCTYPE.*?>")


def tag_regex(inp):
    return {
        "tag_open": tag_open.findall(inp),
        "tag_close": tag_close.findall(inp),
        "tag_open_close": tag_open_close.findall(inp),
        "comment": comment.findall(inp),
        "xml_prolog": xml_prolog.findall(inp),
        "html_declaration": html_declaration.findall(inp)
    }
