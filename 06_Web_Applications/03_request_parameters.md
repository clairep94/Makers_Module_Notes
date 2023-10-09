# POSTMAN & REQUESTS:

[Install Postman here](https://www.postman.com/downloads/)

## REQUEST PARAMETERS:

The `GET` method is often used to _query or retrieve_ information from the server. The exact data returned depends of the implementation of the web server.

A `GET` request can contain _query parameters_, as part of the URL.

The `POST` method is often used to _send_ data to the web server (usually to create or update data, or just send some information). What is done with this data depends of the implementation of the web server.

A `POST` request can contain _query parameters_ (like a `GET` request), but it can also contain _body parameters_. Contrarily to _query parameters_, they are not included in the URL, but within the request body itself.

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
