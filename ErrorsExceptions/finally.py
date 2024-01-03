n = int(input("Enter Numerator"))
d = int(input("Enter Denoinator"))
result =0
try:
  result = n/d
except ZeroDivisionError:
  print("Cannot divide a number by zero")
else:
  print(result) # code block executed when exception doesnt occur
finally:
  # code executed whether exception thrown or not
  # example closing file or network connection 
  # code that must be executed
  print("code executed whether exception thrown or not")
