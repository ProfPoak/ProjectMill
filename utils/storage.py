import json

def save(data, path="data/db.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load(path="data/db.json"):
    try:
        with open(path, "r") as f:
            content = f.read()
            if not content.strip():
                return {}
            return json.loads(content)
    except FileNotFoundError:
        return {}  
    except json.JSONDecodeError:
        return {}