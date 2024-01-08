class Product:
  quantity = 400

  def __init__(self, name, price): #__ methods should not be called directly
    self.name = name
    self.price = price

# p1 = Product() TypeError: __init__() missing 2 required positional arguments: 'name' and 'price'

p1 = Product('phone', '300')
print(p1.name, p1.price)
Product.quantity = 500
print(p1.quantity)

p2 = Product('laptop', '900')
print(p2.name, p2.price)
print(p2.quantity)