# ONE-TO-MANY JOINS

## SQL QUERIES:

```sql
SELECT [columns to select] --all with {table_name.column}, {table_name.column}
  FROM [table name] --many/child
  JOIN [other table name] --one/parent
  ON [join condition]; --parent.id = child.parent_id
```

Example:

```sql
-- We added an alias for artists.id using the "AS" keyword.
SELECT albums.id AS album_id, -- NOTE THIS LINE
       albums.title,
       artists.id AS artist_id, --NOTE THIS LINE
       artists.name
  FROM albums
    JOIN artists
    ON artists.id = albums.artist_id;
```

```sql
 album_id |        title         | artist_id |     name     
----+----------------------+-----------+--------------
  1       | Doolittle            |         1 | Pixies
  2       | Surfer Rosa          |         1 | Pixies
  3       | Waterloo             |         2 | ABBA
  4       | Super Trouper        |         2 | ABBA
  5       | Bossanova            |         1 | Pixies
  6       | Lover                |         3 | Taylor Swift
  7       | Folklore             |         3 | Taylor Swift
  8       | I Put a Spell on You |         4 | Nina Simone
  9       | Baltimore            |         4 | Nina Simone
 10       | Here Comes the Sun   |         4 | Nina Simone
 11       | Fodder on My Wings   |         4 | Nina Simone
 12       | Ring Ring            |         2 | ABBA
```

## MODEL CLASS:

```shell
# file: lib/artist.py

class Artist():
    def __init__(self, id, name, genre, albums = []):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums #add this
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
```

```shell
# file: tests/test_artist_repository.py
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album

def test_find_with_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find_with_albums(1)
    assert artist == Artist(1, "Pixies", "Rock", [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(5, "Bossanova", 1990, 1),
    ])

# Note, you'll need to have the `__eq__` method on `Album` for this to work.
```

```shell
# file: lib/artist_repository.py
from lib.artist import Artist
from lib.album import Album

class ArtistRepository():
    # ...

    # Find a single artist, along with their albums
    def find_with_albums(self, artist_id):
        rows = self._connection.execute(
            "SELECT artists.id as artist_id, artists.name, artists.genre, albums.id AS album_id, albums.title, albums.release_year " \
            "FROM artists JOIN albums ON artists.id = albums.artist_id " \
            "WHERE artists.id = %s", [artist_id])
        albums = []
        for row in rows:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        # Each row has the same id, name, and genre, so we just use the first
        return Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]["genre"], albums)
    
    # ...
```

