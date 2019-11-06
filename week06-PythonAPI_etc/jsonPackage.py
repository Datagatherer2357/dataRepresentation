# Gareth Duffy - g00364693
# dataRepresentation wk 6 

import json

data =  {
    'name':'joe',
    'age':21,
    "student": True
    }
#print(data)

# We want to convert to JSON:
file = open("simple.json",'w')
#json.dump(data,file, indent=4) # indent adds more whitespace
                                # Very handy for big files
jsonString = json.dumps(data)   # IF dont want in file,put it in a string: pass in the object
                                # and pass to server
print(jsonString)