from pathlib import Path
p = Path('.') # current working directory
print(p,'is the current working directory ')
home = p.home()
print(home)
doc_path = home / 'documents'
print(doc_path)
print(doc_path.parent) # just above the parent of existing folder 