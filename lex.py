from Text import Text
from Tag import Tag

def lex(body):
    out = []
    buffer = ""
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True;
            if buffer: out.append(Text(buffer))
            buffer = ""
        elif c == ">":
            in_tag = False
            out.append(Tag(buffer))
            buffer = ""
        else:
           buffer += c
        if not in_tag and buffer:
            out.append(Text(buffer))
    return out
