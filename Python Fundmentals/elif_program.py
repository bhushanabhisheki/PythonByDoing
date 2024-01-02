friends =['rolf','bob','anne']
family = ['jen','charlie']

user_name = input('Enter your username : ')
if user_name in family:
  print(f"{user_name} is a family member")
elif user_name in friends:
  print(f"{user_name} is a friend")
else:
  print(f"{user_name} is a stranger")