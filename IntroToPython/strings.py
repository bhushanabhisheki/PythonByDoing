my_string = "Hello World!" # single quote allowed 
                           #start and end quote type should match
                        
print(my_string)

string_with_quotes = "This is a 'test string" #vice versa allowed 

string_with_same_quote = "Sample string contains \" character" #use escape

string_with_quotes = "Hello, it's me"
another_with_quotes = 'He said, "You were amazing" yesterday'
yet_another_with_quotes = "Hello, it\"s me"
yet_another_with_quotes = 'He said, \'You were amazing\' yesterday'

multi_line_string = """this is a multi-line string
                      that spans over 
                      multiline comments"""

print(multi_line_string)

"""
can be used for multi-line comments 
as and when required
and it wont throw any error
"""

name = "Bhushan" # can use ' mark, start and end quotation should match
greeting  = "Hello " + name
print(greeting)

age = 34
#show_age = "My age is " + age #throw and error
show_age = "My age is " + str(age)
print(show_age)

