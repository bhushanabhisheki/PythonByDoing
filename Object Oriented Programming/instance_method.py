class Student: 
  def __init__(self, name):
    self.name = name

  #instance method
  def hello(self):  #always to be invoked on object
    print("Hello " + self.name)
  

student1 = Student('john')
student1.hello() #always to be invoked on object
