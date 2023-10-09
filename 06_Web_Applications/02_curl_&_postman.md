# CURL:

* [CURL DOCUMENTATION](https://www.warp.dev/terminus/curl-post-request#:~:text=cURL%20(curl)%20is%20an%20open,%5Boptions%5D%20%5BURL%5D.)

* We can use a small command line utility called curl — you can install it on Mac with Homebrew:

```shell
; brew install curl
```

* `curl` is an HTTP client -- it can send a request to a server and receive a response. The only required argument to the command is the URL.
  * `curl` is the command-line version of `requests` for Python.

### EXAMPLE:

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


<br>
<hr>
<hr>
<br>

# POSTMAN & REQUESTS:

[Install Postman here](https://www.postman.com/downloads/)

## EXAMPLE GET REQUEST:

In Postman, we can see our query params added to the `GET` request URL:

```shell
#GET REQUEST: 
curl https://jsonplaceholder.typicode.com/todos/12?name=Josh&age=30

#RESPONSE:
{
    "userId": 1,
    "id": 12,
    "title": "ipsa repellendus fugit nisi",
    "completed": true
}
```

**URL:** `https://jsonplaceholder.typicode.com` + <br>
**PATH:** `/todos/12` + <br>
**QUERY PARAMS:** `name = Josh` & `age = 30` = <br>