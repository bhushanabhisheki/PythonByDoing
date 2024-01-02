
cars =["ok","ok","ok","ok","ok","ok","ok","ok","ok"]

#else to be at same indentation level as for/while
#if the loop completely run through all the elements 
# without encountering a break or error
for status in cars:
  if status == "faulty":
    print("stoppping the production line")
    break
  print(f"care status is {status}")
  print("shipping new car to customer")
else:
  print("all cars built successfully. No faulty cars.")