import json

def load_dictionary(filepath='dictionary.json'):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_dictionary(data, filepath='dictionary.json'):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)