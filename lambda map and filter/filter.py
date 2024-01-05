# numbers = [1,2,3,4,5,6,7,8,9,10]

# odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
# print(odd_numbers)

#prime numbers
numbers = [2,3,4,5,6,7,8,9,10,11,12,13]

def is_prime(number):
  if(number<2):
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

# prime_number = list(filter())
print(list(filter(is_prime, numbers)))

family = [
  {'name':'bhushan', 'age':32, 'grade':'A'},
  {'name':'anuja', 'age':23, 'grade':'C'},
  {'name':'moksh', 'age':2, 'grade':'B'},
  {'name':'john', 'age':12, 'grade':'A'},
  {'name':'Dave', 'age':24, 'grade':'A'}
]

filtered_family = list(filter(lambda member: member['age'] > 23 and member['grade'] == 'A',family))
print(filtered_family)