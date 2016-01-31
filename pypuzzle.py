import requests

def green(string):
    return "\033[1;32m"+str(string)+"\033[0m"


def red(string):
    return "\033[1;31m"+str(string)+"\033[0m"


def maxLen(iterate):
    maximum = 0
    for i in iterate:
        if len(str(i)) > maximum:
            maximum = len(str(i))
    return maximum


def challenge(url, func):
    data = requests.get(url).json()
    data["answers"] = []
    for value in data["values"]:
        if type(value) is list:
            data["answers"].append(func(*value))
        else:
            data["answers"].append(func(value))

    data = requests.post(url,json=data).json()

    form = "{0:"+str(maxLen(data["values"]))+"} | {1:<"+str(maxLen(data["answers"]))+"}"
    for i in range(0,len(data["values"])):
        line = form.format(str(data["values"][i]), str(data["answers"][i]))
        if data["correct"][i]:
            print(green(line))
        else:
            print(red(line))
