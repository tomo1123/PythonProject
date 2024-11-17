import json

items=[
  {"name":"item1","price":10},
  {"name":"item2","price":20},
  {"name":"item3","price":30}
]

with open("test.json", "w", encoding="utf-8") as fp:
  json.dump(items, fp, indent=4)