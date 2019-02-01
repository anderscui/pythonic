# coding=utf-8


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


fib = fibonacci()
elems = [next(fib) for _ in range(10)]
print(elems)
