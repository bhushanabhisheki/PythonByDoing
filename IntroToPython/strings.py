my_string = "Hello World!" # single quote allowed 
                           #start and end quote type should match
                        
print(my_string)

string_with_quotes = "This is a 'test string" #vice versa allowed 

string_with_same_quote = "Sample string contains \" character" #use escape

multi_line_string = """this is a multi-line string
                      that spans over 
                      multiline comments"""

print(multi_line_string)

"""
can be used for multi-line comments 
as and when required
and it wont throw any error
"""

name = "Bhushan"
greeting  = "Hello " + name
print(greeting)

age = 34
#show_age = "My age is " + age #throw and error
show_age = "My age is " + str(age)
print(show_age)

