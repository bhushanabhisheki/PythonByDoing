#dictionary stores the data in key/value pairs 
#useful when you are looking for data based on key 
#cannot have duplicate keys in dictionary
#maintains the order in which data was added after 3.7 python version, prior no order

friend_ages ={"rolf":23, "adam":34, "Anne":32}
print(friend_ages["rolf"])

friend_ages["Bob"] = 20 #adding element to dictionary
friend_ages["rolf"] = 25 #change element


#list of tuples
friends = [("Rolf", 24), ("Anne", 24), ("Jin", 24)]
friend_ages= dict(friends)
print(friend_ages) #{'Rolf': 24, 'Anne': 24, 'Jin': 24}