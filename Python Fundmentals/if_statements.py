friend = "bhushan"
username = input("Enter the username : ")

if (friend == username): #python always sends the condition to bool function 
                         #so if 5: would also work 
  print("Hello Friend") #block statements needs to have same indentation
  print("next steps")
else:
  print("Hello Stranger")
print("outside if")
  #print("sdfsfd") #IndentationError: unexpected indent