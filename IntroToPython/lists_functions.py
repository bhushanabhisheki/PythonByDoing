fruits = ['apple','mango','peach','orange','watermelon','grape']

print(len(fruits)) #length of list

fruits.insert(1,'pineapple') #insert at index and the element specified
print(fruits) #['apple', 'pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape']

fruits.append('test') #append the element at last
print(fruits) #['apple', 'pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape', 'test']

fruits.append(['guava', 'apricot']) #append list as element
print(fruits) #['apple', 'pineapple', 'mango', 'peach', 'orange', 'watermelon', 'grape', 'test', ['guava', 'apricot']]


fruits = ['apple','mango','peach','orange','watermelon','grape']
fruits.extend(['guava', 'apricot'])#append extracted elements
print(fruits) #['apple', 'mango', 'peach', 'orange', 'watermelon', 'grape', 'guava', 'apricot']

fruits.remove("orange")
print(fruits) #['apple', 'mango', 'peach', 'watermelon', 'grape', 'guava', 'apricot']

#fruits.remove("tin") #ValueError: list.remove(x): x not in list
fruits.pop() #removes last element
print(fruits) #['apple', 'mango', 'peach', 'watermelon', 'grape', 'guava']

print(fruits.index('peach')) #print index

scores = [12,45,22,5,67,23,56,78,23,56,78,64]
print(max(scores))
print(min(scores))