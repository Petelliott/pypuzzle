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


def urlForm(string):
    if "http" not in string:
        if ":" not in string:
            parts = string.split("/",1)
            return "http://" + parts[0] + ":23964/" + parts[1]
        return "http://"+string
    return string


def challenge(url, func):
    url = urlForm(url)

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

    data_iter = zip(data["values"], data["answers"], data["correct"])

    print("----"+url.split("/")[-1]+"----")
    for value, answer, correct in data_iter:
        line = form.format(str(value), str(answer))
        line = green(line) if correct else red(line)
        print(line)

    completed = False not in data["correct"]
    score = str(data["correct"].count(True)) + "/" + str(len(data["correct"]))
    footer = green("completed!") if completed else red("fail: "+score)
    print(footer)

    return completed


def solution(url):
    def dec(func):
        def new_func():
            challenge(url, func)
        return new_func
    return dec
