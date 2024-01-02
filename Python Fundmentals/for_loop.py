#run number of times and is identical to foreach in other languages

friends = ["rolf", "john", "anne"]

for friend in friends:
  print(friend)
#for loop can be used on list, set, tuple or dict as they are iterables

for _ in friends:   #_ is used placeholder and not being used as variable
  print("Hello World")

for index in range(2, 20, 3):
  print(index)  #2,5,8,11,14,17

students = [
  {"name":"bhushan", "grade":45},
  {"name":"anuja", "grade":67},
  {"name":"moksh", "grade":88},
  {"name":"test", "grade":22},
  ] 

for student in students:
  name = student["name"]
  grade = student["grade"]
  print(f"{name} has grade {grade}")

  family = {"bhushan":32, "anuja":23, "moksh":2}

  for person in family: #person will have the key
    print(f"{person} is of age {family[person]}")#32 23 2