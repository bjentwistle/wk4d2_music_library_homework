class Album:
    
    def __init__(self, title, genre, artist_id, id = None):
        self.id = id
        self.title = title
        self.genre = genre
        self.artist = artist_id