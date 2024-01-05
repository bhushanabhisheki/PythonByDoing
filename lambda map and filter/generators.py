#generator functions returns iterators
#generators do not allow indexing like list
#generators not stored in memory like list
#generators contains yield  instead of return

def function():
  counter =0
  while counter <=10:
    yield counter #returns generator object
    counter = counter + 1

print(list(function()))

def even_generator(x):
  for i in range(x):
    if(i% 2 == 0):
      yield i

print(list(even_generator(11)))