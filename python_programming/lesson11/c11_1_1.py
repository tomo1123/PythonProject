"""辞書型とJSON形式の比較"""
import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print("#############")
print(json.dumps(j))