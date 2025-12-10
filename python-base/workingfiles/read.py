file = open('jokes.txt', "r")
content = file.read()
print(content)
# read method reads all the lines
file.close()
# it is always important to close the file to release system resources 
# readlines the file line by line 
with open('jokes.txt', "r") as file:
 lines = file.readlines()
 for line in lines:
  print(line.strip())
