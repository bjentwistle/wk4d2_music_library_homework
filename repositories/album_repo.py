
#This is the bones of our code that translates python to sql and back.
from db.run_sql import run_sql
from models.album import Album 
from models.artist import Artist
import repositories.artist_repo as artist_repo

def select_all():  
    albums = [ ]  # ADDED - in case we get `None` back from run_sql

    sql = "SELECT * FROM albums" #this is our sql query
    results = run_sql(sql) 

    for row in results: #translates the results from SQL query into an instance of our Album class.
        artist = artist_repo.select(row['artist_id']) #common problem is forgetting to call the artist Class first before calling Album
        album = Album(row['title'], artist, row['genre'], row['id'])
        albums.append(album)
    
    return albums

def select(id):
    album = None
    sql = 'SELECT * FROM albums WHERE id = %s'
    values = [id]
    rows = run_sql(sql, values)
    if rows: #this will check for flasey conditions ie in case rows doesn't exist (False)
        album_info = rows[0]
        artist = artist_repo.select(album_info['artist_id'])
        album = Album(album_info['title'], album_info['genre'], artist, album_info['id'])
    return album


def save(album):
    # sql = f"INSERT INTO albums (description, artist) VALUES('{album.description}','{album.artist}' )"
    #Here we are vulnerable to unscruptulous people inputting an sql injection (of code) that might delete our data/db. 
    # So we write it differently using %s as placeholders for our inputs.
    sql = f"INSERT INTO albums (title, genre, artist_id) VALUES(%s, %s, %s) RETURNING * " #just returns the single row we just created
    values = [album.title, album.genre, album.artist.id]
    rows = run_sql(sql, values)
    id = rows[0]['id'] # get the id assigned by the database an giving it to the variable id
    album.id = id # now our album.id is set to id from the database.
    
    return album


def delete_all():
    sql = 'DELETE FROM albums'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM albums WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update_album(id, column, value): 
    sql = 'UPDATE albums SET column = %s WHERE id = %s RETURNING *'
    values = [value]
    run_sql(sql, values)

    # UPDATE table_name SET column1 = value1, column2 = value2, WHERE condition
    # RETURNING * | output_expression AS output_name;

def update_genre(id, new_genre): 
    sql = "UPDATE albums SET genre = %s WHERE id = %s"
    values = [new_genre, id]
    run_sql(sql, values)

def update_title(id, new_title):
    sql = "UPDATE albums SET title = %s WHERE id = %s"
    values = [new_title, id]
    run_sql(sql, values)