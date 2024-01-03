def choclate():
  print("choclate")

def decorator(func):
  def wrapper():
    print("wrapper")
    func()
    print("wrapper end")
  return wrapper

decorator(choclate)()