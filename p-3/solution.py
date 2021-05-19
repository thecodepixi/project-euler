import math

def check_prime(num):
  prime = True
  i = 2
  while i < num:
    if num % i == 0:
      prime = False
    i += 1
  return prime 

def largest_prime_factor(n):
  i = int(math.sqrt(n))
  while i > 2:
    if n % i == 0 and i % 2 != 0 and check_prime(i):
      return i
    i -= 1
  return i
      
print(largest_prime_factor(600851475143))
