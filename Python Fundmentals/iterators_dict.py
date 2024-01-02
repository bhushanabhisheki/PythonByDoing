friend_ages= {"abd":12, "cde":34, "fgh":56, "ijk":78}

for name in friend_ages:
  print(name)

for age in friend_ages.values():
  print(age)

for name,age in friend_ages.items():
  print(f"{name} is {age} years old")

for item in friend_ages.items():
  print(item)