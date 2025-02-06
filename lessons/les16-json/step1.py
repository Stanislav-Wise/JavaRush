import pickle


data = {
    "name": "Alice",
    "age": 28,
    "languages": ["Python", "JavaScript"],
    "is_student": False
}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)