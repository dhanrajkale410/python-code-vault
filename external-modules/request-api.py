import requests

r = requests.get('https://api.github.com/users/dhanrajkale410')

print(r.json())