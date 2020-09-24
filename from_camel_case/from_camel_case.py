

def from_camel_case(name):
    return name[0].lower() + "".join(ch if ch.islower() else "_" + ch.lower() for ch in name[1:])