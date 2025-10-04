import re

def name_validator(name):
    pattern = r""
    if not type(name) == str and re.match(pattern, name):
        raise NameError("invalid NAME!!!!!")
    else:
        return name
    

