#Import request

import requests

# define the api url
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userid" : 1
}

# send get request with parameters
response = requests.get(url, params=params)

print("Statuscode:" , response.status_code)
print("Request URL :", response.url)

data = response.json()

for post in data:
    print("Post ID" , post["id"])
    print("Post Title" , post["title"])
    print("-----------------------")


#post request
#send information to an api

new_post = {
    "title": "Learning Python",
    "body" : "We are learnign GET and POST request",
    "userID": 1
}

response = requests.post(url, json=new_post)
print("Post status code:", response.status_code)