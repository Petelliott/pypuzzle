
def generate():
    return list(range(0,100))

def solve(a):
    if a % 5 == 0 and a % 3 == 0:
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return a
