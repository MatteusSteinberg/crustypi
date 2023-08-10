import time
from requests import post
from insertion import get_data, delete_data
from decouple import config
import datetime

apiUrl = config('API')
token = config('TOKEN')

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

    result = post(url, json=docs, headers={'Authorization': f'Bearer {token}'})
    
    print(f"Timestamp: {dt_string}")
    print(f"Data sent to {apiUrl}, status code: {result.status_code}")