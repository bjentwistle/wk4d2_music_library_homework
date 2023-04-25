from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo 
import repositories.artist_repo as artist_repo

artist_repo.delete_all()
album_repo.delete_all()

    # self.artist_name = artist_name
    # self.id = id

artist1 = Artist("Amy Winehouse")
artist_repo.save(artist1)
artist2 = Artist("Bon Jovi")
artist_repo.save(artist2)

artist_repo.select_all()

    # self.id = id
    # self.title = title
    # self.genre = genre
    # self.artist = artist_id

album1 = Album("Back to Black", "Soul", artist1)
album_repo.save(album1)
album2 = Album("Slippery when wet", "Hard Rock", artist2)
album_repo.save(album2)

album_repo.select_all()





