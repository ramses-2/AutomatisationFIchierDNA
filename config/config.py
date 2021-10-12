import json





file_path='./config/config.json'
config={}
with open(file_path) as f:
    config = json.load(f)
    print(config)
