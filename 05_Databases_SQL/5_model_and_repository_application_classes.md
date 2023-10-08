# MODEL, REPOSITORY, and APPLICATION PYTHON CLASSES

* PostgreSQL allows us to manipulate tables, but we need a way to perform these queries through our Python program. We do this through two classes:

* A **Model** class is used to hold a record's data.
<br>For example, if we have a table `artists`, we'd have a class `Artist`, with attributes for each column. A single object holds the data for a specific artist record. This class usually doesn't contain any logic, but is only used to hold data.

* A **Repository** class implements methods to run SQL queries on the database to retrieve, create, update or delete data.
For example, if we have one table `artists`, we'd have a class `ArtistRepository` containing methods that communicates with the database using SQL.

## DESIGNING A DATABASE PROJECT:

### 1. Design Recipe

1. Design and create the table if needed.
2. Create test SQL seeds.
3. Define the Model and Repository class names.
4. Implement the Model class.
5. Design the Repository class interface.
6. Write test examples.
7. Test-drive and implement the Repository class behaviour.

### [2. SEQUENCE DIAGRAMS](https://github.com/clairep94/databases-in-python/blob/main/challenges/03_creating_sequence_diagrams.md) 

* Make sure the child(ren) -> parent. Eg. concerts -> venues

### 3. Designing a Schema:

1. List all the nouns from the specification or user stories.
2. Decide whether a noun is a record (the table name) or a property of it (a column).
3. Decide the column types.
4. Decide on the tables will be related and where a foreign key is needed.
5. Write the SQL to create the table.


## MODEL CLASS:

``` shell
class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre
        ### WATCH OUT FOR DATA TYPES BETWEEN THE SQL TABLE AND PYTHON.

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
```

```shell
from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
```

## REPOSITORY CLASS

``` shell
| Method   | Job              | Arguments | SQL query it executes                                | Returns             |
| -------- | ---------------- | --------- | ---------------------------------------------------- | ------------------- |
| `all`    | Get all artists  | none      | `SELECT * FROM artists;`                             | A list of `Artist`s |
| `find`   | Get one artist   | `id`      | `SELECT * FROM artists WHERE id = $1;`               | A single `Artist`   |
| `create` | Insert an artist | `Artist`  | `INSERT INTO artists (name, genre) VALUES (%s, %s);` | Nothing             |
| `delete` | Delete an artist | `id`      | `DELETE FROM artists WHERE id = $1;`                 | Nothing             |
```

```shell
from lib.artist import Artist

class ArtistRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by their id
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
                                 artist.name, artist.genre])
        return None

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None
```

``` shell
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new ArtistRepository

    artists = repository.all() # Get all artists

    # Assert on the results
    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3)
    assert artist == Artist(3, "Taylor Swift", "Pop")

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "The Beatles", "Rock"))

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "The Beatles", "Rock"),
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]
```

## APPLICATION CLASS

* Located in root folder along with `/lib` `/seeds` `/tests`

```shell
# file: app.py

from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

    artist_repository = ArtistRepository(self._connection)
    artists = artist_repository.all()

    for artist in artists:
        print(f"{artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()
```

* if __name__ == '__main__' means "only run this code if you're running this file directly, and not if you're importing it from another file".
* [More details here](https://realpython.com/if-name-main-python/)