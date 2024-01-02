#dictionary stores the data in key/value pairs 
#useful when you are looking for data based on key 
#cannot have duplicate keys in dictionary
#maintains the order in which data was added after 3.7 python version, prior no order

#dictionaries are mutable , content can be changed
friend_ages ={"rolf":23, "adam":34, "Anne":32}
friend_id={1:'rolf', 2:'adam', 3:'anne'} #key as integer allowed
print(friend_ages["rolf"])
#print(friend_ages["test"]) #KeyError: 'test'

friend_ages["Bob"] = 20 #adding element to dictionary
friend_ages["rolf"] = 25 #change element


#list of tuples
friends = [("Rolf", 24), ("Anne", 24), ("Jin", 24)]
friend_ages= dict(friends)
print(friend_ages) #{'Rolf': 24, 'Anne': 24, 'Jin': 24}

people = dict(
  bhushan=32,
  anuja=23,
  moksh=2
)
print(people) #{'bhushan': 32, 'anuja': 23, 'moksh': 2}
people['test'] = 5
print(people) #{'bhushan': 32, 'anuja': 23, 'moksh': 2, 'test': 5}
del people['test'] #deletes the element
print(people) #{'bhushan': 32, 'anuja': 23, 'moksh': 2}
