with open('data/sample.txt', 'r') as file:
  # line1 = file.readline()
  lines = file.readlines()

# print(lines)
for line in lines:
  print(line.strip()) #strip removes /n or white space