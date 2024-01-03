scores = [1,2,3,4,5]

def sum(numbers):
  sum =0
  for item in numbers:
    sum += item 
  return sum

print(sum(scores)) 

#return list
ids = [1,2,3,4,5,6,3,8,2,10, 10, 10]
def remove_duplicates(numbers):
  new_list = []
  for number in numbers:
    if(number not in new_list):
      new_list.append(number)
  return new_list

print(remove_duplicates(ids))
