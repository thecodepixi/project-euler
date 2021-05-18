def multi_3_and_5(start_n) 
  sum = 0

  (start_n - 1).downto(0).each do |n|
    if n % 3 == 0 || n % 5 == 0 
      sum += n
    end 
  end 

  return sum 
end 

p multi_3_and_5 10
p multi_3_and_5 100
p multi_3_and_5 1000