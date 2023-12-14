
friend = ['bhushan', 'anuja', 'moksh'] #list or array

"""preffered to have data in list homogeneous 
but friend = ['bhushan',3, 'anuja'] is valid/allowed"""

print(friend[0])

print(len(friend)) #print length of the list/array
friend.append('sample') #append new element to the list/array
friend.remove('bhushan') #remove the element from the list/array, need exact match

print(friend)

friend_with_age = [['bhushan',12], ['anuja',4], ['moksh',2]]
print(friend_with_age[2][0]) 

grades = [80,75,90,100]
avarage = sum(grades)/len(grades)
print(avarage)

friends = ['bhushan','anuja', 'moksh']
comma_seperated =",".join(friends)
print(f"my friends are {comma_seperated}")