import time
from requests import post
from insertion import get_data, delete_data
from decouple import config

apiUrl = config('API')
token = config('TOKEN')

while True:
    time.sleep(10)
    if token is str and token.__len__() > 1:
        print("No token yet.")
        continue

    docs = get_data()
    delete_data()

    url = apiUrl + '/api/measurements'
    jsonData = docs

    post(url, docs, headers={'Authorization': f'bearer {token}'})