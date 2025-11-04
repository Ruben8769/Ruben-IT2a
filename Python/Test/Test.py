import json

with open("Python/Test/Test.json", "r") as f:
    data = json.load(f)

print(data)