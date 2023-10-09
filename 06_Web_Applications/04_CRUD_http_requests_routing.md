# CRUD HTTP REQUESTS AND ROUTING:

## ROUTING TABLE:

Associates a given request **method** with a given **path** and a block of python code

| CRUD | HTTP Method | Path                  | Python repo method | SQL query                             | 
| -----| ----------- | --------------------- | ------------------ | ------------------------------------- |
|   C  | POST        | `/books`              | `#create`          | `INSERT INTO books VALUES ...`        | 
|   R  | GET         | `/books` or `/books/1`| `#find` & `#all`   | `SELECT * FROM books (WHERE id = ...)`|
|   U  | PATCH       | `/books/1`            | `#update`          | `UPDATE books SET ... WHERE id = ...` |
|   D  | DELETE      | `/books/1`            | `#delete`          | `DELETE FROM books WHERE id = ...`    |

## CRUD APPLICATION:

* **Create**, **Read**, **Update**, **Delete**

### Example of CRUD operations - HTTP Route -> Repo Class Method -> SQL Query

We can execute CRUD operations (Create, Read, Update, Delete) on a given Resource, by sending HTTP requests to the right method and path.

The pattern of routing below is called [**RESTful Routing**](https://restfulapi.net/)

```shell
# Books resource: -- 'resource' that we execute CRUD operations (Create, Read, Update, Delete)

# Create a new book --> #create --> INSERT INTO books VALUES ...
Request: POST /books
  With body parameters: "title=No Place on Earth&author_name=Christa Wolf"
Response: None (just creates the resource on the server)

# Read a single book --> #find --> SELECT * FROM books WHERE id = ...
Request: GET /books/1 #get book with ID 1
Response: of a single book

# Update a single book --> #update --> UPDATE books SET ... WHERE id = ...
Request: PATCH /books/1
  With body parameters: "title=No Place on Earth&author_name=Christa Wolf"
Response: None (just updates the resource on the server)

# Delete a book --> #delete --> DELETE FROM books WHERE id = ...
Request: DELETE /books/1
Response: None (just deletes the resource on the server)

# List all the books --> #all --> SELECT * FROM books
Request: GET /books
Response: list of books
```