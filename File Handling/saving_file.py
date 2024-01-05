while True:
  with open('names.txt','a') as file:
    name = input("Enter the name to be added : ")
    file.write(name.capitalize() + '\n')
    choice = input("Do you want to add more y/n? : ")
    if(choice == 'n'):
      break
