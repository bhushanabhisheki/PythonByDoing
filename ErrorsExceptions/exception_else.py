n = int(input("Enter Numerator"))
d = int(input("Enter Denoinator"))
result =0
try:
  result = n/d
except ZeroDivisionError:
  print("Cannot divide a number by zero")
else:
  print(result) # code block executed when exception doesnt occur
  
