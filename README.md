# api-datasette

Datasettes containing data related to [api.existenz.ch](https://api.existenz.ch).

## Structure

- Raw metadata gets downloaded from the Existenz-API.
- Gets put into `existenz-api.db` ([SQLite file](https://sqlite.org)).
- [datasette](https://datasette.io) displays the dataas webpages.
