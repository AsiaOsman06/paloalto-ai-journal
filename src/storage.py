import json
from pathlib import Path

DATA_FILE = Path("data/entries.json")

def load_entries():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_entry(entry):
    entries = load_entries()
    entries.append(entry)
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)
