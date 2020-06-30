#
# Project Euler: https://projecteuler.net/problem=2
#
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
# (Solution: 4613732)
#
def solve():
    soln = sum(in_series(fibonacci()))
    return soln

def fibonacci():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

def in_series(seq):
    for num in seq:
        if num > 4000000:
            break
        if not num % 2:
            yield num

print(solve())