user_input = input("choose one of two options (p/q):")

user_options = ['p','q']
# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...
while user_input in user_options:
    if user_input == "p":
        print("Hello")
    elif user_input == "q":
        break
    user_input = input("choose one of two options (p/q):")