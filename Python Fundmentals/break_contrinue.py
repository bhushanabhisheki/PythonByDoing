cars = ["ok","ok","ok","faulty","ok","ok","ok","faulty","ok","ok","ok","ok"]

print("break example")
for status in cars:
  if(status == "faulty"):
    print("stopping the production line")
    break
  print(status)

print("continue example")
for status in cars:
  if(status == "faulty"):
    print("found faulty cars")
    continue
  print(status)