# import json
# with open("C:\\stream\\b.json", "r") as f:
#     data = json.load(f)
# import os
# print(os.path.exists("C:\\stream\\b.json"))
# 
import json

with open("C:\\stream\\b.json", "r") as f:
    data = f.read()
    print("Raw File Content:", data)  # Check if the file contains data

    try:
        json_data = json.loads(data)  # Attempt to parse JSON
        print("Parsed JSON:", json_data)  # Show structured data
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)  # Show error message if JSON is invalid