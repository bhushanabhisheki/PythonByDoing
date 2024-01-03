
def add(*args):
  sum =0
  print(args) #tuple (2, 3, 4)
  for item in args:
    sum += item
  return sum

print(add(2,3,4))