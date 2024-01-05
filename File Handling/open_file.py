
file = open("data\sample.txt", 'r') #file name and mode

# content = file.read() # reads entire file
#content = file.read(10) #reads 10 bytes/chars
content = file.readline() #reads one line
print(content)
file.close() # close the file when opened else any other file open for same
# file will throw an error
