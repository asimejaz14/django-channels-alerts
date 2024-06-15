from time import sleep

import requests
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()



while True:
    # Generating random full name and country
    random_name = fake.name()
    random_country = fake.country()

    # Data to be sent in the POST request
    data = {
        "data": {
            "name": random_name,
            "country": random_country
        }
    }

    # URL to send the POST request to
    url = "http://127.0.0.1:8000/bank/data"

    # Sending the POST request
    response = requests.post(url, json=data, timeout=60)

    # Printing the server's response
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    sleep(1)

