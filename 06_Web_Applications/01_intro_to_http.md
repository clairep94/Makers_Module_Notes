# INTRO TO HTTP

* **Web Server**: A 'central' machine where the program runs, maybe uses a database to store its data.
  * Either the machine or the software program running the program and responding to clients.
  * Sends `response` to client

* **Client**: A software that connects to the server, allows users to interact with the program.
  * eg. web browser, mobile phone, etc.
  * Sends `request` to server
  * Displays the `response` to the user

* **"web server"** will usually refer to a (Python) program that receives `requests` and sends back `responses`, and **"client"** will refer to either Postman, a web browser or `curl`.

## Restaurant Analogy:

* **Web Client**: Customer who wants to order food from a restaurant.

* **Web Server**: Kitchen in a restaurant. Prepares and serves requests data or services.

* **Database**: Kitchen inventory. Raw materials of data that can be packaged by the web server.

* **HTTP Request**: The customer's order in a restaurant. It needs to follow request format specified in the API.

* **API (Application Programming Interface)**: Restaurant's menu. A set of rules and options that the web server provides to its clients. Defines the available endpoints (dishes) and how to request and recieve the data or services from the web server.

## Example: A news website:

1. The client program (web browser) connects to the server and asks for the all latest articles -> **HTTP Request**

2. The server (a program, written in Python or other language) receives the request and prepares the list of articles (maybe from a database)

3. The server sends back the list of articles to the client -> **HTTP Response**

4. The client recieves the list of articles and displays them to the user --> **End of the first request-response cycle**

5. The client sens a request to get a specific article.

6. The server receives the request.

7. The server retrieves this specific article from the database and sends back a response containing that article's data.

8. The client recieves the response and displays that article's content.

<br>
<hr>
<hr>


## REQUESTS:

An HTTP request is defined by:

* its **method** (also called 'verb') (`GET`, `POST`)
* its **URL** (`https://jsonplaceholder.typicode.com`)
* its **path** - is all that follows the first `/` of the URL (`/todos/12`, `/`)
* its **parameters** (or request data) (a key-value pair of parameters) -- see next section.

`curl` does a `GET` request by default.


## RESPONSE:

An HTTP response is defined by:

* **Status Code** (`200`, `404`, etc.)
* **Content or Data** (`JSON`, etc.)