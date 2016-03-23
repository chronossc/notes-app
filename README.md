# Notes API

## Overview
This API is a very simple notes app for show people my code skills in a fast project. It came with a postman collection for anyone test it.

## Setup

Clone the project, install requirements and run `manage.py migrate`. A user will be created for you with username "foobar" and password "foobar".

You can load few notes with `manage.py loaddata notes`

## API Reference

### POST /api/auth/

Authenticate a user and returns a JWT Token to be used in all other requests. Token life time is 600 seconds. To use it add to request headers:

	"Authorization: JWT <token>"

### POST /api/notes/

Create a new note. Available fields are `title`, `note` and `favorited`.
Returns the created note object.

### GET /api/notes/

List the notes. You can filter favorited notes by appending `?favorited=True` to url.

### PATCH /api/notes/<id>/

Update a note. Available fields are `title`, `note` and `favorited`. You can favorite a note by using `{"favorited": "true"}`. Returns the created note object.

### DELETE /api/notes/<id>/

Delete a note.

## Setup Postman collection

You can import `Notes-API.postman_collection` into your Postman. This collection has two special variables:

* **server**: the server of the API, usually `http://localhost:8000`.
* **jwt_token**: the token to be used in all requests except `/api/auth/`.

To set these values go to `Manage Environments` and add a new one with both variables. After you have added a new environment select it in `Manage Environments` dropdown. Every time you request `/api/auth/` you need to update `jwt_token` value.