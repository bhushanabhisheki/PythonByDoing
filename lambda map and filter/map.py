
numbers = [1, 2, 3, 4, 5]

def square(x):
  return x*x

square_list = list(map(square, numbers)) #python 3 returns object 
  # hence use list 
print(square_list)

celcius_tempretures = [25,30,15,10,35]
# def fahrenheit(x):
  # return (x* 9/5) + 32

far_list = list(map(lambda x:(x* 9/5) + 32,celcius_tempretures))
print(far_list)