import random


def generate():
    values = []
    for _ in range(0, 50):
        a = []
        for _ in range(0,10):
            x = random.SystemRandom().randint(0, 100)
            a.append(x)
        values.append(a)
    return values


def solve(*a):
    a = list(a)
    output = []
    for item in a:
        output = [item] + a
    return output
