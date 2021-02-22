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

# Helpers
def get_value_from_path(values, path):
    path_parts = path.split(".")
    current = values

    while len(path_parts) > 0:
        p = path_parts.pop(0)

        current = current[p]

    return current


# Get definitions
with open(api_definition_file) as file:
    definitions = yaml.safe_load(file)

    for api_name, definition in definitions["api"].items():
        print(f"Generating database for API {api_name}")

        fields_string = ", ".join(
            [f"{field['key']} {field['type']}" for field in definition["fields"]]
        )

        question_marks = ",".join("?" for field in definition["fields"])

        create_query = f"CREATE TABLE {api_name} ({fields_string})"
        print(create_query)

        c.execute(create_query)

        c.execute(
            f"CREATE UNIQUE INDEX {api_name}_{definition['primary-key']}_index ON {api_name}({definition['primary-key']})"
        )

        print(f"Fetching data from {definition['url']}")
        r = requests.get(definition["url"])
        r.raise_for_status()

        # Insert rows
        for key, row in r.json()["payload"].items():
            values = []

            for field in definition["fields"]:
                value = get_value_from_path(row, field["path"])

                if "prefix" in field:
                    value = f"{field['prefix']}{value}"

                values.append(value)

            c.execute(f"INSERT INTO {api_name} VALUES({question_marks})", values)

# Save
db.commit()
db.close()

print("Done.")
