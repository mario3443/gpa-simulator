import json
import os

DATA_FILE = "data/records.json"

# 讀取檔案，並且如果沒讀到就回復空清單
def load_courses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# 將課程清單存到檔案中
def save_courses(courses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)
