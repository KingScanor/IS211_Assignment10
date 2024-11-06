--Artists Table
CREATE TABLE Artist (
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL
);

--Albums Table
CREATE TABLE Albums (
    album_id INTEGER PRIMARY KEY,
    album_name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES Artist (artist_id)
);

--Songs Table
CREATE TABLE Songs (
    song_id INTEGER PRIMARY KEY,
    song_name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    duration_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES Albums (album_id)
);