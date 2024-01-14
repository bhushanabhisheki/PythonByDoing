class Car:
  def __init__(self, brand):
    self.brand = brand
    self.steering = self.Steering()

  @staticmethod
  def drive():
    print("Drive")

  class Steering:
    @staticmethod
    def rotate():
      print("rotate")


Car.drive()
Car.Steering.rotate()