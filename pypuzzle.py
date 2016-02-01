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
            data["answers"] += [func(*value)]
        else:
            data["answers"] += [func(value)]

    data = requests.post(url, json=data).json()

    values_len = str(maxLen(data["values"]))
    answers_len = str(maxLen(data["answers"]))
    form = "{0:"+values_len+"} | {1:<"+answers_len+"}"

    data = zip(data["values"], data["answers"], data["correct"])

    for value, answer, correct in data:
        line = form.format(str(value), str(answer))
        line = green(line) if correct else red(line)
        print(line)
