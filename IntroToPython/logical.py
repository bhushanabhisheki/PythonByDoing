age =5
result = age > 18 and age < 65
print(result)

result = age > 18 and age < 65
print(result)

#in case of and result is TRUE only when both are TRUE
#in case of or result is FALSE only when both are FALSE

print("About bool")
print(bool(0))
print(bool(12))

print(bool(''))
print(bool("HELLO"))

print(bool([]))
print(bool([1,2,3]))


default_greeting = 'there'
name = input("Enter your name (optional): ")
user_name = name or default_greeting
print(f"Hello, {user_name}")


default_age =30
age = input("Enter your age (optional): ")
user_age = age or default_age
print(f"User age is {user_age}")