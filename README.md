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

## Update

`poetry add datasette:latest`

`poetry update`

If any dependencies have changed: Run `poetry export --without-hashes -f requirements.txt --output requirements.txt` and commit the file.

If new plugins are required, add their installation to `post_compile`.

### Deployment setup

- Create a dokku app on `konzept.space` with `dokku apps:create api-datasette; dokku letsencrypt:enable api-datasette`
- Locally: `git remote add dokku dokku@konzept.space:api-datasette`

Dokku will identify this as a Python project, load the appropriate buildpack, run the `post_compile` script and then start serving the service defined in the `Procfile`. Pretty nifty.
