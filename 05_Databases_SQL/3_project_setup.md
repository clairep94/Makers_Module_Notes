# PROJECT SETUP

This project will use a few components:

* **Python and Pytest**  
  The programming language and test framework will be the same as what you've
  previously used.

* **The `psycopg` library**  
  This library allows us to send SQL queries to the database, and retrieve the
  result set.

  * This is a dependency listed in Pipfile within the project starter.
  * Need to `pipenv install` and `pipshell` before running `pytest` or `python app.py`. -- creates a virtual environment where `psycopg` is installed, rather than on the global system.

* **A class `DatabaseConnection`**  
  This class acts as a thin layer with methods to connect to PostgreSQL and send SQL queries to it.
  * `/lib` folder needs `database_connection.py`
  * `/tests` folder needs `conftest.py` and `test_database_connection.py`

* **[Walkthrough of the Codebase](https://www.youtube.com/watch?v=8dBADUN8gdg&t=287s)**

``` shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install
# Read below if you see an error with `python_full_version`

# Activate the virtual environment
; pipenv shell

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py
```



## 1) CREATE A DATABASE:

To drop and re-connect:
```
# From the starter project directory, in your terminal
; dropdb music_library
; createdb music_library
; psql -h 127.0.0.1 music_library < seeds/music_library.sql
```

``` shell
# from psql:

psql -h 127.0.0.1
CREATE DATABASE music_library;

#You should get this output from the REPL
# acknowledging the database has been created.
CREATE DATABASE

\q #exit postgreSQL REPL
```

``` shell
# from terminal:

createdb music_library
```

* Creates an empty database with no tables.
* Can be viewed in TablePlus

## 2) IMPORT SEED DATA:

```
$ psql -h 127.0.0.1 {database_name} < {file_containing_sql}
```
``` shell
# Output:

NOTICE:  table "albums" does not exist, skipping
DROP TABLE
CREATE SEQUENCE
CREATE TABLE
NOTICE:  table "artists" does not exist, skipping
DROP TABLE
CREATE SEQUENCE
CREATE TABLE
INSERT 0 12
INSERT 0 4
```

### EXAMPLE SEED DATA:

``` sql
-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    artist_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');

INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Lover', 2019, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Folklore', 2020, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('I Put a Spell on You', 1965, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Baltimore', 1978, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Here Comes the Sun', 1971, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Fodder on My Wings', 1982, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ring Ring', 1973, 2);
```

