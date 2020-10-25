import pytest

from src.flatten_dict import flatten


def test_flatten_dict():
    assert flatten({"job": {"1": "scout", "2": "worker",
                            "3": "writer", "4": "reader",
                            "5": "learner"},
                     "name": {"nick": {}, "last": "Drone",
                             "first": "Second"},
                     "recent": {"places": {
                         "earth": {"NP": "", "NY": "2017", "Louvre": "2015"}},
                               "times": {"XXI": {"2064": "Nope"},
                                        "XX": {"1964": "Yes"}}}}
                    ) == {"job/1": "scout",
                          "recent/places/earth/NY": "2017",
                          "job/3": "writer",
                          "job/2": "worker",
                          "job/5": "learner",
                          "job/4": "reader",
                          "recent/times/XXI/2064": "Nope",
                          "recent/times/XX/1964": "Yes",
                          "recent/places/earth/Louvre": "2015",
                          "name/nick": "",
                          "recent/places/earth/NP": "",
                          "name/first": "Second", "name/last": "Drone"}
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
