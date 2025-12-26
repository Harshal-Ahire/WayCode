def getData():
    import requests
    x = requests.get('https://api.example.com/users')
    return x.json()

def calc(a, b):
    return a + b

user = {'name': 'John', 'age': 25}
print(user['name'])