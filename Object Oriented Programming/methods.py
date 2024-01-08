class Product:
  quantity = 200

  def __init__(self,name, price):
    self.name = name
    self.price = price

  def summer_discount(self, discount_percent):
    self.price = int(self.price) - (int(self.price) * discount_percent/100)


p1 = Product('phone', '300')
print(p1.name, p1.price)
p1.summer_discount(10)
print(p1.price)

Product.summer_discount(p1, 10)
print(p1.price)
