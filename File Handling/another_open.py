# avoid closing of the file
with open('data\sample.txt','r') as file:
  contents = file.read()
  print(contents)
