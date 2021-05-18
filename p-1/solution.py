def multi_3_and_5(start_n):
  sum = 0
  for x in range(start_n - 1, 0, -1):
    if x % 3 == 0 or x % 5 == 0:
      sum += x
  return sum 

print( 
  multi_3_and_5(10),
  multi_3_and_5(100),
  multi_3_and_5(1000) 
)
