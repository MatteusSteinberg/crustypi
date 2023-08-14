import time
from requests import post
from insertion import get_data, delete_data, create_table
from decouple import config
from datetime import datetime
from threading import Thread

apiUrl = config('API')
token = config('TOKEN')

create_table()

def send_data(url, json, dt_string):
    result = post(url, json=json, headers={'Authorization': f'Bearer {token}'})
    print(f"Timestamp: {dt_string}")
    print(f"Data sent to {apiUrl}, status code: {result.status_code}")

while True:
    time.sleep(10)
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    if token is str and token.__len__() > 1:
        print("No token yet.")
        continue

    docs = get_data()
    delete_data()

    url = apiUrl + '/api/measurements'
    jsonData = docs

    Thread(target=send_data, args=(url, docs, dt_string)).start()