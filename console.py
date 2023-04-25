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
artist3 = Artist("Beyonce")
artist_repo.save(artist3)
artist4 = Artist("Prince")
artist_repo.save(artist4)

artists_list_of_instances = artist_repo.select_all()
for artist in artists_list_of_instances:
    print(f"The artist name is {artist.artist_name}")

result_artist = artist_repo.select(2)
print(f"The selected artist's name is {result_artist.artist_name}")

    # self.id = id
    # self.title = title
    # self.genre = genre
    # self.artist = artist_id

album1 = Album("Back to Black", "Soul", artist1)
album_repo.save(album1)
album2 = Album("Slippery when wet", "Hard Rock", artist2)
album_repo.save(album2)
album3 = Album("Renaissance", "R&B", artist3)
album_repo.save(album3)
album4 = Album("Purple Rain", "Pop", artist4)
album_repo.save(album4)

album_table = album_repo.select_all()
for album in album_table:
    print(f"The seleted album's title is {album.title}")

result_album = album_repo.select(2)
print(f"The album title is {result_album.title}")

new_genre = album_repo.update_genre(4, "Rock")

new_title = album_repo.update_title(3, "Lemonade")

new_artist_name = artist_repo.update_artist_name(4, "@±$")
result_artist = artist_repo.select(4)
print(f"The selected artist's name is {result_artist.artist_name}")

