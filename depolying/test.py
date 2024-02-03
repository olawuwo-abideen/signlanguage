import requests


#url = 'http://localhost:8080/2015-03-31/functions/function/invocations'


data = {
    'url': 'https://raw.githubusercontent.com/Olawuwo2000/sign-language/main/img_3455.jpg'
}

result = requests.post(url, json=data).json()
print(result)
