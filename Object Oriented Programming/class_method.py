class Student:
  #class variable 
  category = 'Student'

  #class method
  @classmethod #decorator is required for class method 
  def get_category(cls): #should use cls for class methods
    print(cls.category)

Student.get_category() #should be invoked on class only

