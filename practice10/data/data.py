import json
def get_data(file_path):
    with open(file_path, "r+") as f:
        content=json.load(f)
    return content

#print(get_data("/Users/apple/kse_pb/practice10/data/cinema_halls.json"))
def load_data(data, file_path):
    with open(file_path, 'r+') as f:
        json.dump(data, f)

