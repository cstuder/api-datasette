# api-datasette

Datasettes containing data related to [api.existenz.ch](https://api.existenz.ch).

## Structure

Run `poetry run python generate.py`

- Raw metadata gets downloaded from the Existenz-API.
- Gets put into `existenz-api.db` ([SQLite file](https://sqlite.org)).
- [datasette](https://datasette.io) displays the database as webpages.

## Start Datasette

`datasette existenz-api.db -m metadata.json``
