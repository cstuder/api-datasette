# api-datasette

Datasettes containing data related to [api.existenz.ch](https://api.existenz.ch).

`LIVE`: <https://api-datasette.konzept.space>

## Structure

Run `poetry run python generate.py`

- Raw metadata gets downloaded from the Existenz-API.
- Gets put into `existenz-api.db` ([SQLite file](https://sqlite.org)).
- [datasette](https://datasette.io) displays the database as webpages.

## Start Datasette

`datasette existenz-api.db -m metadata.json`

## Deployment

Run `git push dokku main`

If any dependencies have changed: Run `poetry export --without-hashes -f requirements.txt --output requirements.txt` and commit the file.

### Deployment setup

- Create an dokku app on `konzept.space`.
- `git remote add dokku dokku@konzept.space:api-datasette`
