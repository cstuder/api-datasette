# api-datasette

Datasettes containing data related to [api.existenz.ch](https://api.existenz.ch).

`LIVE`: <https://api-datasette.konzept.space>

## Structure

Run `poetry run python generate.py`

- Raw metadata gets downloaded from the Existenz-API.
- Gets put into `existenz-api.db` ([SQLite file](https://sqlite.org)).
- [datasette](https://datasette.io) displays the database as webpages.

## Start Datasette

`poetry run datasette existenz-api.db -m metadata.json`

## Update

`poetry add datasette:latest`

`poetry update`

If Datasette has changed: Re-run plugin installations, i.e. `poetry run datasette install datasette-cluster-map`.

If new plugins are required, add their installation to `post_compile`.

### Initial setup

`brew install pipx`

`pipx install poetry`

`pipx inject poetry poetry-plugin-export`

## Upgrade Python

See officially supported runtimes here: <https://devcenter.heroku.com/articles/python-support#supported-runtimes>

To switch to a new Python version on Dokku, update the string in `.python-version` and push to Dokku.

## Deployment

Run `git push dokku main`

If without changes and you just want to rebuild: `git commit --allow-empty -m "Rebuild."`

### Deployment setup

- Create a dokku app on `konzept.space` with `dokku apps:create api-datasette; dokku letsencrypt:enable api-datasette`
- Locally: `git remote add dokku dokku@konzept.space:api-datasette`

Dokku will identify this as a Python project, load the appropriate buildpack, run the `post_compile` script and then start serving the service defined in the `Procfile`. Pretty nifty.
