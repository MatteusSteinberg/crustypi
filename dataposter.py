import time
from requests import post
from insertion import get_data, delete_data
from decouple import config

apiUrl = config('API')

while True:
    time.sleep(10)

    docs = get_data()
    delete_data()

    url = apiUrl + '/measures'
    jsonData = docs

    post(url, docs)