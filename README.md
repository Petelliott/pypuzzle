# pyPuzzle
## about
pypuzzle allows you create programming puzzles that can be played by anyone.
it is written in python3.x and is available under the MIT License.

## server
pypuzzle-server serves puzzles from the puzzles directory. if it does not exist
it will be created on startup.
#### puzzle format
a puzzle contains two methods: generate() and solve()

generate() gives a list of arguments that are used to test the puzzle
```python
def generate():
    return list(range(0,100))
```
solve() is the solution for one of the values from generate()
```python
def solve(a):
    if a % 5 == 0 and a % 3 == 0:
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return a
```
## doing a puzzle
doing a puzzle is simple. create a function that would solve the puzzle then  
```python
import pypuzzle

def func(a):
    if a % 5 == 0 and a % 3 == 0:
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return a

pypuzzle.challenge("http://localhost:9000/fizzbuzz",func)
```
alternatively, the `@solution(url)` decorator can be used
```python
from pypuzzle import solution

@solution("http://localhost:9000/fizzbuzz")
def func(a):
    if a % 5 == 0 and a % 3 == 0:
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return a

func()
```
