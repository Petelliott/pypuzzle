import random


def generate():
    values = []
    for _ in range(0, 50):
        x = random.SystemRandom().randint(0, 100)
        y = random.SystemRandom().randint(0, 100)
        values.append([x, y])
    return values


def solve(a, b):
    return a * b
