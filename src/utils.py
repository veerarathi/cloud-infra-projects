import os
import json
import datetime

def log_status(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def validate_file_extension(filepath, extension=".json"):
    return filepath.lower().endswith(extension)

def load_schema_config(filepath):
    if not os.path.exists(filepath):
        log_status(f"File not found: {filepath}", "ERROR")
        return None
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            log_status(f"Configuration loaded: {os.path.basename(filepath)}")
            return data
    except json.JSONDecodeError:
        log_status("Failed to decode JSON. Check file syntax.", "ERROR")
        return None
