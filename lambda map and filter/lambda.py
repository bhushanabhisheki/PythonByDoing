
sum = (lambda x,y:  x + y)(22,3) #anonymous function
print(sum)

sum = (lambda x=10,y=20:  x + y)()#anonymous function with key args
print(sum)
