#!/usr/bin/python

import time
import random
from datetime import datetime, timedelta
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import WriteType

URL = "http://localhost:8086"
TOKEN = "YOUR_API_TOKEN"
ORG = "YOUR_ORG"
BUCKET = "YOUR_BUCKET"

TOTAL_POINTS = 100_000
BATCH_SIZE = 5_000

def generate_data():
    start_time = datetime.utcnow() - timedelta(days=1)
    
    locations = ["server_room", "warehouse", "factory_floor"]
    
    for i in range(TOTAL_POINTS):
        point_time = start_time + timedelta(seconds=i)
        
        p = Point("sensor_data") \
            .tag("location", random.choice(locations)) \
            .tag("host", f"host_{random.randint(1, 5)}") \
            .field("temperature", round(random.uniform(20.0, 30.0), 2)) \
            .field("humidity", round(random.uniform(40.0, 60.0), 2)) \
            .time(point_time)
        
        yield p

def main():    
    client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)

    write_options = WriteOptions(
        batch_size=BATCH_SIZE,
        flush_interval=10_000,
        jitter_interval=2_000,
        retry_interval=5_000,
        max_retries=5,
        max_retry_delay=30_000,
        exponential_base=2
    )

    write_api = client.write_api(write_options=write_options)

    start_process = time.time()

    for point in generate_data():
        write_api.write(bucket=BUCKET, org=ORG, record=point)

    write_api.close() 
    client.close()

    end_process = time.time()
    print(f"--- Finished in {end_process - start_process:.2f} seconds ---")

if __name__ == "__main__":
    main()