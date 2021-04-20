import json

def red_file_json():
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["name"])

def write_Json_file():

    # a Python object (dict):
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

red_file_json()
write_Json_file()