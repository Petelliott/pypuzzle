import requests


def challenge(url, func):
    data = requests.get(url).json()
    data["answers"] = []
    for value in data["values"]:
        if type(value) is tuple:
            data["answers"].append(func(*value))
        else:
            data["answers"].append(func(value))

    data = requests.post(url,json=data).json()
    print(data)
