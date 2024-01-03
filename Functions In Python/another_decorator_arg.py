def decorator(func):
  def wrapper(*args, **kwargs):
    print("wrapper")
    func(*args, **kwargs)
    print("wrapper end")
  return wrapper

@decorator
def choclate():
  print("choclate")

@decorator
def cake(name):
  print("cake " + name)

choclate()
cake("mine")