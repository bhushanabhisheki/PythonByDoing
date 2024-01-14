class Student:
  #static method do not have access to class or instance members
  category = 'Student'

  def __init__(self, name):
    console.log(f'name= ${name}')

  @staticmethod
  def add(a, b):  #static method do not have access to class or instance members
    return a + b  #mainly used as utility functions
  
print(Student.add(4,5)) 