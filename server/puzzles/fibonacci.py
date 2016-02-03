import random


def generate():
    values = []
    for _ in range(0, 50):
        x = random.SystemRandom().randint(0, 100)
        values.append(x)
    return values


def solve(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
