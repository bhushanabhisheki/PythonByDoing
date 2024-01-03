def product(**keywargs):
  print(keywargs) #{'name': 'iphone', 'price': '700'}
  for key,value in keywargs.items():
    print(key + ': ' + value)

product(name="iphone", price="700")
#product(name="ipad", price="300", description="this is ipad")