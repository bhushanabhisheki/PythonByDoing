age = 34
print_str = f"You are {age}"
print(print_str) #use fstring function to add int to string

age=50
print(print_str) #updated var value not updated using fstring- limitation

name = "bhushan"
greeting = "How are you {} ?"  #creates a template format
print(greeting.format(name))  #pass the variable
name = "anuja"
print(greeting.format(name))

another_greeting = "Are you all right {name}?"
print(another_greeting.format(name="moksh")) #allows multiple params 

name = 'Jose'
friend = 'Rolf'
phrase = name + ' is friends with ' + friend
print(phrase)

description = "{} is {age} years old."  #allowed
print(description.format("Bob", age=30)) 