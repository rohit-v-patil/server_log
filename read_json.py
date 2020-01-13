import json
with open("status.json", "r") as read_file:
    data = json.load(read_file)
print(type(data))
print(data['hosts']['winserver']['plugin_output'])