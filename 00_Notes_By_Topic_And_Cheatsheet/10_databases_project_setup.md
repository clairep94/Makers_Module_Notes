# Setting up a Database:

## POSTGRESQL 

* relational database software


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

* Database software (PostgreSQL) runs on our machine and manages the data we need to store.

* We interact with it using a language called SQL. It comes with different commands to query, create or modify data stored in the database. We run queries to:

  * Get all the records from a table.
  * Get all the records from a table where some conditions are met (e.g. where the name is "John").
  * Create a new record.
  * Update or delete a record where some conditions are met.
  * And more complex things, like create new tables.

* Programs that talk to a database to create, read, update or delete data are often called CRUD [https://en.wikipedia.org/wiki/Create,_read,_update_and_delete] applications.


## SYSTEM-WIDE SETUP:

### Install postgresql:
First, you will need to install PostgreSQL on your machine. You can do this using Homebrew on macOS. Here, we're using PostgreSQL 15 but if there's a newer release you're asked to use, just substitute in that version number instead:

```
# Install postgresql.
$ brew install postgresql@15
```
Once installed, you'll need to make sure that installation directory is on your PATH environment variable. In the output from the Homebrew installation you just ran, should be a line which looks like this one, which you should copy, paste into the terminal and run:

```
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
```

Afterwards, either start a new terminal session or just run `zsh`.

```
# Run this after the installation
# to start the postgresql software
# in the background.
$ brew services start postgresql@15

# You should get the following output:
==> Successfully started `postgresql@15` (label: homebrew.mxcl.postgresql@15)
```

<hr>
<hr>

## 0) PSQL PROJECT SET UP:

```
$ psql -h 127.0.0.1

psql (15.2)
Type "help" for help.

leoht=# 
```

### Getting an error?

If you get an error similar to `connection to server at "127.0.0.1", port 5432 failed: FATAL: database "leoht" does not exist` - you can use the `createdb command` to create the default database psql tries to connect to, which is named after your macOS system username.

For example, my macOS username is `leoht`, so I'd run the bash command: `createdb leoht` - this should fix the connection error.

## 1) CREATE A DATABASE:

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

### Seed:

* Initial sets of data which can be used to populate a database and its tables

* Seed should contain SQL queries to:

  * create the tables (the structure)
  * insert some records in these tables (the data itself)

### Import seed data:

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
