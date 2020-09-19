def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                if v:
                    stack.append((path + (k,), v))
                    if "empty" in result:
                        del result["empty"]
                else:
                    result["/".join((path + (k,)))] = ""
            else:
                result["/".join((path + (k,)))] = v

    return result