def fib_total(max)
  total = 0
  a, b = 0, 1
  while a < max
    if a % 2 == 0 
      total += a 
    end 
    a, b = b, a + b
  end 
  total
end 

p fib_total(4_000_000)
