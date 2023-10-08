# DATABASES IN PYTHON

## DATABASE:

* Used to store data from a program long term vs. during the 
use of a program. 
* For 100 days of Python, I was doing this via .txt and .csv files

<br>

* A collection of tables
* Has columns for attributes of records -- fixed unless we're changing the schema of a table
* Each record is a row



```
Table: students

 id |     name     | cohort_name
----+--------------+------------
  1 | Sarah        | April 2022
  2 | Georgia      | April 2022
  3 | David        | May 2022
  4 | Ali          | April 2022
```

* _(By convention, table names and column names are always lowercase, using underscores to separate words). Table names are always plural.)_


## PostgreSQL:

* Database software runs on our machine and manages the data we need to store.

* We interact with it using a language called SQL. It comes with different commands to **query**, **create** or **modify** data stored in the database.
* We run queries to:

  * Get all the records from a table.
  * Get all the records from a table where some conditions are met (e.g. where the name is "John").
  * Create a new record.
  * Update or delete a record where some conditions are met.
  * And more complex things, like create new tables.

* Programs that talk to a database to **create, read, update or delete data** are often called [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) applications.


## PRIMARY & FOREIGN KEYS:

### KEYS:

* `id` - used to uniquely identify each record

* `foreign key` - points to the primary key in another table

```
  albums                                                    artists

 id |        title         | artist_id |                  | id |     name     
----+----------------------+-----------+                  |----+--------------
  1 | Doolittle            |         1 | ---------------> |  1 | Pixies
  2 | Surfer Rosa          |         1 |                  |    |
  3 | Waterloo             |         2 | ---------------> |  2 | ABBA
  4 | Super Trouper        |         2 |                  
  5 | Bossanova            |         1 |                                
  ```

### EXAMPLE CODE:

``` sql
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);
```

## SEED:

* Initial sets of data which can be used to populate a database and its tables

* Seed should contain SQL queries to:

  * create the tables (the structure)
  * insert some records in these tables (the data itself)

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

