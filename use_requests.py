import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success | Response = {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')
print('Program Ended')


