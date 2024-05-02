import random
from datetime import datetime, timedelta
from faker import Faker
from django.utils import timezone

import os
import django
from django.conf import settings


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Benchmark.settings')

# Configure Django settings
django.setup()

from bank.models import BankLogs, BankLogsUTC
fake = Faker()

# Define the start date and end date for generating data
start_date = datetime(2024, 3, 15)
end_date = start_date + timedelta(days=9)  # 10 days of data

# Define the number of rows per day
rows_per_day = 100000

# Generate and insert dummy data
data_list = []
for _ in range(rows_per_day):
    name = fake.company()
    location = fake.address()
    city = fake.city()
    country = fake.country()

    # Create and save the BankLogs instance
    data_list.append(BankLogs(
        created_at=timezone.now(),
        updated_at=timezone.now(),
        name=name,
        location=location,
        city=city,
        country=country
    ))

BankLogs.objects.bulk_create(data_list)


print("Dummy data insertion completed.")
