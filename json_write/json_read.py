import json

with open("test.json", "r", encoding="utf-8") as fp:
  data = json.load(fp)
  
print(data[0]["name"], data[0]["price"])
print(data[1]["name"], data[1]["price"])
