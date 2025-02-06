import pickle


with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)