import requests

base = "http://localhost:8000"

# 1. Create note
r = requests.post(f"{base}/notes/", json={
    "title": "Project Plan",
    "content": "Initial draft",
    "tag": "work"
})
print(r.json())

# 2. Get all versions
r = requests.get(f"{base}/notes/Project Plan")
print(r.json())

# 3. List all notes
r = requests.get(f"{base}/notes/")
print(r.json())
