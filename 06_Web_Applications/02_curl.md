# CURL:

* [CURL DOCUMENTATION](https://www.warp.dev/terminus/curl-post-request#:~:text=cURL%20(curl)%20is%20an%20open,%5Boptions%5D%20%5BURL%5D.)

* We can use a small command line utility called curl — you can install it on Mac with Homebrew:

```shell
; brew install curl
```

* `curl` is an HTTP client -- it can send a request to a server and receive a response. The only required argument to the command is the URL.
  * `curl` is the command-line version of `requests` for Python.

EXAMPLE:

```shell
; curl -X GET https://jsonplaceholder.typicode.com/todos/12
```

```shell
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

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