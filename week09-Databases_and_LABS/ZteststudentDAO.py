from ZstudentDAO import studentDAO


# SO, with Flask, to create we just need the below line:
# We put in the data wet get passed up from the json (appserver file i think)
#create
latestid = studentDAO.create(('mark', 45)) # When we want to create we call this

# find by id
result = studentDAO.findByID(latestid); # needs to be made into json object (tuple atm)same for 
                                        # update, get all and delete
print (result)

#update
studentDAO.update(('Fred',21,latestid)) # last entry
result = studentDAO.findByID(latestid);
print (result)

# get all 
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

# delete
studentDAO.delete(latestid)
