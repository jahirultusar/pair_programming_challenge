from lib.music_tracker import *

"""
Given an empty list
returns and empty list
"""

def test_empty_list_returns_empty_list():
    track_list = MusicTracker([])
    assert track_list.list_of_tracks == []