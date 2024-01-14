class Parent: 
  def __init__(self):
    self.parent_balance = 400

  def display_balance(self):
    print(f"Balance is {self.parent_balance}")

class Child(Parent):
  def __init__(self):
    super().__init__()
    self.child_balance = 800

  def display_balance(self):
    print(f"Child is {self.parent_balance + self.child_balance}")


mike=Child()
mike.display_balance()

