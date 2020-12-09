import pytest
from src.disposable_teleport import disposable_teleport

def check_solution(func, teleports_str):
    route = func(teleports_str)
    teleports_map = [tuple(sorted([int(x), int(y)]))
                     for x, y in teleports_str.split(",")]
    if route[0] != '1' or route[-1] != '1':
        print("The path must start and end at 1")
        return False
    ch_route = route[0]
    for i in range(len(route) - 1):
        teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
        if not teleport in teleports_map:
            print("No way from {0} to {1}".format(route[i], route[i + 1]))
            return False
        teleports_map.remove(teleport)
        ch_route += route[i + 1]
    for s in range(1, 9):
        if not str(s) in ch_route:
            print("You forgot about {0}".format(s))
            return False
    return True

@pytest.mark.parametrize(('input'), [
    ("12,23,34,45,56,67,78,81"),
    ("12,28,87,71,13,14,34,35,45,46,63,65"),
    ("12,15,16,23,24,28,83,85,86,87,71,74,56"),
    ("13,14,23,25,34,35,47,56,58,76,68"),
])
def test_disposable_teleport(input):
    assert check_solution(disposable_teleport, input) == True