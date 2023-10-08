# SELECT:

The `SELECT` SQL query is used to retrieve records from a table.

Here's the general syntax of a `SELECT` query:

``` sql
SELECT [columns to select] FROM [table name];
```

``` sql
SELECT [columns to select] FROM [table name] WHERE [conditions];
```

The result of running a `SELECT` query on the database is called a result set, and is also in the shape of a table.

### Example:

``` sql
SELECT id, title FROM albums;
```

``` sql
-- From albums,
-- filter where id is '2',
-- and select only values for the columns id, title and release_year.
SELECT id, title, release_year
  FROM albums
  WHERE id = 2;

-- We can use the keywords AND and OR
-- to combine conditions.

-- From albums,
-- filter where release_year is greater than 1989 AND artist_id is '1',
-- and select only values for the columns id, title, release_year and artist_id.
SELECT id, title, release_year, artist_id
  FROM albums
  WHERE release_year > 1989 AND artist_id = 1;
```

# UPDATE:

``` sql
UPDATE [table_name] SET [column_name] = [new_value];
```
``` sql
UPDATE [table_name] SET [column_name] = [new_value]
  WHERE [conditions];
```

### Example:

```sql
UPDATE albums SET title = 'A new title';
```

# DELETE:

```sql
DELETE FROM [table_name] WHERE [conditions];

-- Or, delete all records (never do this!)
DELETE FROM [table_name];
```

# INSERT:

``` sql
INSERT INTO [table_name]
  ( [list of columns] )
  VALUES( [list of values] );
```

### Example Query:

```sql
-- We don't specify the value for the `id`
-- column, the database will automatically pick one.
INSERT INTO artists 
  (name, genre)
  VALUES('Massive Attack', 'Alternative');
```