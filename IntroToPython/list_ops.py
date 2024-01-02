a = [1,2,3]
b=[4,5,6]
print(a+b) #creates a new list [1, 2, 3, 4, 5, 6]
  #works like extend but creates a new list

print(a*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#nested list
nested_list = [1,2,3,[1,2,3],5,6]
print(nested_list[3][1]) #2 list within list [1,2,3]

#list are mutable - meaning we can modify content of the list
mutable_list = [1,2,3]
mutable_list[1] =100
print(mutable_list) #[1, 100, 3]

mutable_list[0:4] = [100,200,300]
print(mutable_list) #[100, 200, 300]



