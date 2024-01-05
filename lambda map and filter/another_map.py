numbers=["1","2","3","4","5","6","7","8","9"]
numbers_list = list(map(int, numbers))
print(numbers_list)

prices = [100,200,300,400,500] 

discount_list =  list(map(lambda x:x- x*5/100, prices))
print(discount_list)

names = ['bhushan','anuja','moksh']
cap_names = list(map(str.capitalize, names))
print(cap_names)