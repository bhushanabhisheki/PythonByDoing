
art_friends = {"Rolf", "Anne" , "Jen"}
science_friends = {"Jen", "Charlie"}

print('john' in art_friends) #False
print('Rolf' in art_friends) #True

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science) # {"Rolf", "Anne" }
print(art_friends-science_friends) # - used for intersection


#symmetric difference - members not in both set
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both) #{'Rolf', 'Anne', 'Charlie'}
print(art_friends ^ science_friends) # ^ used for intersection

#intersaction - members in both set
in_both = art_friends.intersection(science_friends)
print(in_both) #{'Jen'}
print(art_friends & science_friends) # & used for intersection

#unite both sets without duplicaiton
all_friends = art_friends.union(science_friends)
print(all_friends) #{'Charlie', 'Anne', 'Jen', 'Rolf'}

print(all_friends | science_friends) # | used for union

