file = open('jokes.txt', "r")
content = file.read()
print(content)
# read method reads all the lines
file.close()
# it is always important to close the file to release system resources 
# readlines the file line by line 
with open('jokes.txt', "r") as file: # it will make sure the file will closed after running the code
 lines = file.readlines()
 for line in lines:
  print(line.strip())

## To write in a file
with open('pyfile.txt', 'w') as f:
    # Comment:    # write method overrides whatever is written
    f.write('Roses are red,\n')
    f.write('Violets are blue,\n')
    f.write('And How are you!?,\n')
# end overwrite file

addition_lines = ['Stars up above,\n', "Wisper WOrds of love,\n"]
## To add data in existing file then we use append mode
with open("pyfile.txt", "a") as f:
   f.write("The sun is bright,\n")
   f.write("On this lovely day,\n")
   f.writelines(addition_lines)


### to read csv file
import csv 
with open("file.csv", "r") as csv_file:
  csv_reader = csv.reader(csv_file)
  for  row in csv_reader:
    print(row)
     