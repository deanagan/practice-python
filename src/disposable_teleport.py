

def disposable_teleport(input: str) -> str:

    stations = {}
    result = ['1',]
    paths = input.split(',')
    for start,end in paths:
        stations.setdefault(start, []).append(end)
        stations.setdefault(end, []).append(start) # undirected

    def teleport(from_station):
        if len(set(result)) == 8 and result[0] == result[-1]:
            return True

        for to_station in stations[from_station]:
            used_path = next((p for p in paths if to_station in p and from_station in p), None)
            if used_path:
                paths.remove(used_path)
                result.append(to_station)
                if teleport(to_station):
                    return True
                paths.append(used_path)
                result.pop()


        return False

    teleport('1')

    return ''.join(result)
