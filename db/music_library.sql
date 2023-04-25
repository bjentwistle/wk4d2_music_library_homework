DROP TABLE IF EXISTS albums CASCADE;
DROP TABLE IF EXISTS artists CASCADE;


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255)

);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id)  
        --this uses the artist ID from the Artist's class above, ie a foreign key which points to another table's primary key
);
