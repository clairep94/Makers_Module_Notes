# MANY-TO-MANY JOINS

A many-to-many relationship is needed when a record from the first table can have many records in the other table, but the opposite is also true.

You can recognise the need for a many-to-many relationship when you can answer "yes" to the following questions:

Can one [TABLE ONE] have many [TABLE TWO]?
Can one [TABLE TWO] have many [TABLE ONE]?
As an example: a blog post can have many tags. But a tag can also be associated with many posts.

Can a post have many tags? - Yes
Can a tag have many posts? - Yes
When designing a many-to-many relationship, you will need a third table, acting as a "link" between to the tables. This is called a **join table**. It contains two columns, which are two foreign keys, each linking to the two tables.

## DESIGN RECIPE

1. Extract nouns from user stories or specifications
2. Infer the table names and columns
3. Decide the column types
```shell
# EXAMPLE:

Table: posts
id: SERIAL
title: text
content: text

Table: tags
id: SERIAL
name: text
```
4. Design the many-to-many relationships
5. Design the join table
```shell
# EXAMPLE

Join table for tables: posts and tags
Join table name: posts_tags
Columns: post_id, tag_id
```
6. Write the SQL
7. Create the tables
```shell
psql -h 127.0.0.1 database_name < posts_tags.sql
```

## SQL SEED:

```sql
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

-- Create the second table.
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name text
);

-- Create the join table.
CREATE TABLE posts_tags (
  post_id int,
  tag_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (post_id, tag_id)
);

```

## SQL QUERIES:

### SELECT:

```shell
| Method        | Job                              | Arguments      | SQL query          | Returns         |
| ------------- | -------------------------------- | -------------- | ------------------ | --------------- |
| `find_by_tag` | Find all posts for the given tag | A tag (string) | `SELECT ... JOIN ` | Array of `Post` |


```

``` sql
-- Select all the tags associated with a given post.
-- Note how we're using two different joins to "link"
-- all the three tables together:
--    * first, by matching only records in the join table for the given post
--    * second, by matching only tags for these records in the join table
SELECT tags.id, tags.name
  FROM tags 
    JOIN posts_tags ON posts_tags.tag_id = tags.id
    JOIN posts ON posts_tags.post_id = posts.id
    WHERE posts.id = 2;
```

### CREATE:

```sql

INSERT INTO posts (title) VALUES ('My amazing post');
-- New post inserted with id 3

INSERT INTO tags (name) VALUES ('poetry');
-- New tag inserted with id 5

INSERT INTO posts_tags (post_id, tag_id) VALUES (3, 5);
```

