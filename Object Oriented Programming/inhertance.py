class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def print_data(self):
    print(f"Name : {self.name} Price : {self.price}")

  def get_data(self):
    self.name = input("Enter the name of the product : ")
    self.price = input("Enter the price of the product : ")


class DigitalProduct(Product):
  # pass #means block of code is empty
  def __init__(self,link):
    self.link = link
  
  def get_link(self):
    self.link = input("Enter the product link : ")

  def print_link(self):
    print(self.link)

p1 = DigitalProduct("")
p1.get_data()
p1.print_data()
p1.get_link()
p1.print_link()

