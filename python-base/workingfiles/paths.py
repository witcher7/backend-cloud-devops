# from pathlib import Path
# p = Path('.') # current working directory
# print(p,'is the current working directory ')
# home = p.home()
# print(home)
# doc_path = home / 'documents'
# print(doc_path)
# print(doc_path.parent) # just above the parent of existing folder 

# ### if the file does not exists

# from pathlib import Path 
# crazy_path = Path.home() / 'I' / 'dont' / 'exist.csv'
# print(crazy_path)

# if crazy_path.exists():
#  with open(crazy_path, "r") as f:
#      print(f.read())
# else: 
#    print("The file does not exist")

## The iterdir method generates an iterator for files and folders within a directory, facilitating easy traversal
# of these items 

## this allows us to iterate over each item( file or folder) one at a time 
from pathlib import Path
path = Path.home() 
for item in path.iterdir():
   if item.is_file() and item.suffix == '.txt':
      print(item.name,'is a text file.')
   
   if item.is_dir():
      print(item.name,"is a directory")
   
   if 'word' in item.names.lower():
      print(item.name,"The word is there inside the file") 