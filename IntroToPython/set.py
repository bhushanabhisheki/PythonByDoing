#sets do not contain duplicate elements 
#do not have order
art_friends ={"Rolf" , "Anne"} #use {} for sets
art_friends.add("Jen") #adds element at any random position, no order maintained
print(art_friends)

art_friends.add("Jen") #duplicate value not added, no remove
print(art_friends)

art_friends.remove("Jen") #remove element

number_set = set([1,2,3,4,5,6,7,8,9])
print(number_set)

number_set = {1,2,3,4,5,2,3,5,1}
print(number_set)

s = {'John', 12, 4.5, True} #set can have different data types
print(s)

empty_dict ={}
print(type(empty_dict))

empty_set = set() #cannot create empty set using {} as it creates dict
print(type(empty_set))


number_set = set([1,2,3,4,5,6,7,8,9])
print(number_set.discard(11)) #wont have program crash like remove method if element not found

print(number_set.pop()) #removes random element from set

number_set.clear()
print(number_set) #removes all elements from set