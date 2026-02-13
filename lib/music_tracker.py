class MusicTracker():
    
    def __init__(self, empty_list):
        self.list_of_tracks = empty_list

    def add_tracks(self, track):
        if track:
            self.list_of_tracks.append(track)