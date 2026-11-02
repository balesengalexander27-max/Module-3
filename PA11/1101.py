# Access the web and fetch internet resources

# Import requests library
import requests

# define API endpoint (combination of domain and path)
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status code ", response.status_code)

data = response.json()

# Display all users
print(data)

for user in data:
    print(user["name"])