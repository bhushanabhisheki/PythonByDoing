def decorator(func):
  def wrapper():
    print("wrapper")
    func()
    print("wrapper end")
  return wrapper

@decorator
def choclate():
  print("choclate")

@decorator
def cake():
  print("cake")

choclate()
cake()