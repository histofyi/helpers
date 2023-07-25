
def slugify(text:str) -> str:
    slug_char = '_'
    to_replace = [' ','-','.',',','[',']','{','}','(',')','/','\\','*',':']
    for replace_me in to_replace:
        if replace_me in text:
            text = text.replace(replace_me, slug_char)
    return text.lower()