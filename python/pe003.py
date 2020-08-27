#
# Project Euler: https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# (Solution:6857)
#
import math

def solve(n):
  largestPrime = -1

  while n % 2 == 0:
    largestPrime = 2
    n >>= 1     #this covers all of the even positive integers

  # this covers the odd positve integers
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
      largestPrime = i
      n = n / i

  #if n is prime and greater than 2, return n
  if n > 2:
      largestPrime = n

  return int(largestPrime)


print(solve(600851475143))
