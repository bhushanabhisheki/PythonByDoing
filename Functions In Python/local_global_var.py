

def print_stats():
  count =20 #local variable
  print(count)

#print(count)## NameError: name 'count' is not defined
count =10 #global variable
print_stats()
print(count)


number = 10

def add_number():
  global number #without this number = number + 1 will throw error 
  number = number + 1
  print(number)

add_number()