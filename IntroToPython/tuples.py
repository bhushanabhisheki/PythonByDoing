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