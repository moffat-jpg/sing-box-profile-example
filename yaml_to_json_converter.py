import json
import yaml # type: ignore
import os

os.chdir(
    os.path.dirname(
        os.path.abspath(
             _file_ # type: ignore
        )
    )
)

with open('config.json', 'r') as input:
    json_object: dict = json.loads(input.read())
    with open('config.json.yaml', 'w') as output:
        output.write(yaml.dump(json_object, allow_unicode=True, indent=4))
        