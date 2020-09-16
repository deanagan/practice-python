import pytest


from friends import check_connection


def test_check_connection():
    assert check_connection(
       ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
        "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
       "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
       ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
        "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
       "super", "scout2") == True, "Super Scout"
    assert check_connection(
       ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
        "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
       "dr101", "sscout") == False, "I don't know any scouts."

    assert check_connection(
        ("nikola-robin","batman-nwing","mr99-batman",
         "mr99-robin","dr101-out00","out00-nwing",),
        "dr101","mr99") == True, "blah"