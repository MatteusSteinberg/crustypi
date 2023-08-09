import time
from requests import post
from insertion import get_data, delete_data

while True:
    time.sleep(10)

    docs = get_data()
    delete_data()

    url = 'https://www.w3schools.com/python/demopage.php'
    jsonData = docs

    post(url, docs)