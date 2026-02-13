from lib.music_tracker import *

"""
Given an empty list
returns and empty list
"""

def test_empty_list_returns_empty_list():
    track_list = MusicTracker([])
    assert track_list.list_of_tracks == []


"""
Given a track added by user
returns list including user submission
"""

def test_user_adds_1_track():
    track_list = MusicTracker([])
    track_list.add_tracks("Break free")
    assert track_list.list_of_tracks == ["Break free"]