# Gareth Duffy - g00364693
# dataRepresentation wk 6  lab 01
# Gets all users following Andrew


import requests, json 

from xlwt import * # For excel writing

def getJSONFromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

data = getJSONFromUrl(url)
#print (data)
#Get the file name for the new file to write

filename = 'githubusers.json'

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# OR to do this in Excel:

# write to excel file
w = Workbook() # Create new workbook
ws = w.add_sheet('githubusers') # Add sheet called cars
row = 0; # @ row 0...
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
row += 1 # move onto row one by adding one
for git in data["githubusers"]:
    ws.write(row,0, git["login"]) # extract the reg attribute/store it in column 0
    ws.write(row,1,git["id"])
    ws.write(row,2,git["node_id"])
    ws.write(row,3,git["avatar_url"])
    row += 1

w.save('githubusers.xls')


 # MY JSON git hub:  {
    #     "login": "Datagatherer2357",
    #     "id": 36170749,
    #     "node_id": "MDQ6VXNlcjM2MTcwNzQ5",
    #     "avatar_url": "https://avatars1.githubusercontent.com/u/36170749?v=4",
    #     "gravatar_id": "",
    #     "url": "https://api.github.com/users/Datagatherer2357",
    #     "html_url": "https://github.com/Datagatherer2357",
    #     "followers_url": "https://api.github.com/users/Datagatherer2357/followers",
    #     "following_url": "https://api.github.com/users/Datagatherer2357/following{/other_user}",
    #     "gists_url": "https://api.github.com/users/Datagatherer2357/gists{/gist_id}",
    #     "starred_url": "https://api.github.com/users/Datagatherer2357/starred{/owner}{/repo}",
    #     "subscriptions_url": "https://api.github.com/users/Datagatherer2357/subscriptions",
    #     "organizations_url": "https://api.github.com/users/Datagatherer2357/orgs",
    #     "repos_url": "https://api.github.com/users/Datagatherer2357/repos",
    #     "events_url": "https://api.github.com/users/Datagatherer2357/events{/privacy}",
    #     "received_events_url": "https://api.github.com/users/Datagatherer2357/received_events",
    #     "type": "User",
    #     "site_admin": false
    # },