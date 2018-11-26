import requests


files = {
    'file': open('1.jpg', 'rb')
}

r = requests.post(
    'http://127.0.0.1:5000/detector',
    files=files
)

print(r.status_code, r.text)