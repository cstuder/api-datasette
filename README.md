# api-datasette

Datasettes containing data related to api.existenz.ch

## Structure

- Raw data gets downloaded to `/rawdata`.
- Parsed by PHP libraries and outputs CSVs to `/rawdata`.
- `sqlite-utils` converts CSVs to SQLite.
- `datasette` shows databases as webpages.
