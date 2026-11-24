import json 

with open("test.json") as ptr:
    data = json.load(ptr)

for shaxs in data.copy():
    if shaxs['second'] == "Valiyev":
        data.remove(shaxs)

with open("test.json", "w") as ptr:
    json.dump(data, ptr, indent=4)