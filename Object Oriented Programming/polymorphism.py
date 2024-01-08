# + is addition as well as string concatination
#len for string length, number of items in list

#metod overriding 
#method of the inherited class overrides the parent method
class Food:
  def type(self):
    print("food")

class Fruit(Food):
  def type(self):
    print("fruit")

apple = Fruit()
print(apple.type())