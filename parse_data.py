import json
from pathlib import Path
# Logic for loading and reading from a JSON file.
# The function must return only the items
def load_items(filename):
    file_path = Path(filename)
    with file_path.open("r") as file:
        data = json.load(file)
    return data["items"]


# Logic for getting only those items that are not yet claimed
# It should return only the items that are unclaimed
def get_unclaimed_items(items):
    unclaimed = [item for item in items if item["status"] == "unclaimed"]
    return unclaimed


# Logic to save the result to a JSON file.
# The function should create the directory if it does not exist and save the result in a JSON format.
def save_result(result, filename):
    output_path = Path(filename).parent
    output_path.mkdir(parents=True, exist_ok=True)

    with Path(filename).open("w") as file:
        json.dump(result, file, indent=2)