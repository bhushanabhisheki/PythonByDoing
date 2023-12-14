name="bhushan"
age= 30
welcome_string = "Welcome {}, your age is {}"
print(welcome_string.format(name, age))
#print(welcome_string.format(name)) 
#IndexError: Replacement index 1 out of range for positional args tuple

#age= int("a34")#ValueError: invalid literal for int() with base 10: 'a34'
#print(age * 12)