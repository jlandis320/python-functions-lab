# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
    
#     For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
  result = sum(range(n + 1))
  print(result)

sum_to(10)
