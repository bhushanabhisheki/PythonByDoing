short_tuple = "rolf", "bob" #() are not mandatory
clear_tuple = ("rolf", "bob") 
required_tuple = [("rolf", "bob")] #case where () required for tuple
not_a_tuple = "rolf" #string, incase you want tuple u need to have ("rolf",) 
another_tuple = "rolf", # cause of , it becomes a tuple and not string

friends = ("Rolf", "Bob" , "Anee")
#its not possible to append new element to tuple

#solution would be to add 
friends = friends + ("jen",)
print(friends) #created a new tuple 

print(friends[1]) #access the element of the tuple

#tuple are immutable - cannot change content of the tuple
#friends[1]="test"# not allowed
                 #TypeError: 'tuple' object does not support item assignment

#slicing of the tuple
print(friends[0:2]) #('Rolf', 'Bob')
#positive, Negative indexing works the same way 

#program execution/performance is faster for tuples compared to list
#tuples mostly used when data not required to be changed