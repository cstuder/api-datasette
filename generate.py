# Generate SQLite database
import yaml
import requests
import sqlite3
import os

db_filename = "existenz-api.db"
api_definition_file = "existenz-api-definition.yaml"

# Delete old database
os.remove(db_filename)

# Open database
db = sqlite3.connect(db_filename)
c = db.cursor()

# Get definitions
with open(api_definition_file) as file:
    definitions = yaml.safe_load(file)

    for api, definition in definitions["api"].items():
        print(f"Generating database for API {api}")

        fields_string = ", ".join(
            [f"{field['key']} {field['type']}" for field in definition["fields"]]
        )

        create_query = f"CREATE TABLE {api} ({fields_string})"

        print(create_query)

        # TODO run create query
        # TODO run CREATE UNIQUE INDEX {definition['api']}_{definition['primary-key']}_index ON {definition['api']}({definition['primary-key']})

        print(f"Fetching data from {definition['url']}")
        r = requests.get(definition["url"])
        r.raise_for_status()

        # Insert rows
        for key, row in r.json()["payload"].items():
            values = []

            # TODO collect values

# Save
c.commit()
c.close()

print("Done.")
