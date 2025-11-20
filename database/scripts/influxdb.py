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

# First value of the array is the default value and the next is the delta
# In a case of [100,10], the value can variate from 90 to 110
POSSIBLE_COMPONENTS = {
    "cpu": {
        "temperature":       [333, 20],    # Kelvin → (~60°C ± 20°C)
        "power_consumption": [0, 300],     # Watts
        "current":           [25, 25],     # Amperes
        "impact_force":      [0, 20]       # Newtons
    },
    "proximity_sensor": {
        "distance":          [100, 80],    # cm
        "power_consumption": [2, 1],       # Watts
        "current":           [0.5, 0.2]    # Amperes
    },
    "impact_sensor": {
        "impact_force":      [0, 2000],    # Newtons
        "sensitivity":       [5, 2],       # arbitrary sensitivity scale
        "power_consumption": [1, 1]
    },
    "gps_chip": {
        "signal_strength":   [75, 10],     # dB-Hz
        "power_consumption": [1.5, 0.5],   # Watts
        "current":           [0.8, 0.2],   # Amperes
        "satellite_count":   [7, 5]        # number of satellites tracked
    },
    "accelerometer": {
        "acceleration":      [0, 5],       # m/s²
        "temperature":       [300, 10],    # Kelvin
        "power_consumption": [1, 0.5]
    },
    "power_supply_unit": {
        "voltage":           [230, 20],    # Volts (AC)
        "current":           [15, 10],     # Amperes
        "power_output":      [3000, 500],  # Watts
        "temperature":       [320, 30]
    },
    "temperature_sensor": {
        "temperature":       [298, 50],    # Kelvin (25°C ± 50°C)
        "power_consumption": [0.5, 0.2]
    },
    "humidity_sensor": {
        "humidity":          [50, 40],     # %
        "power_consumption": [0.5, 0.3]
    },
    "front_light": {
        "luminosity":        [800, 400],   # lumens
        "power_consumption": [50, 20],     # Watts
        "temperature":       [320, 40]     # heat generated
    },
    "engines": {
        "rpm":               [3000, 2000], # revolutions/min
        "temperature":       [360, 40],
        "power_output":      [5000, 1500],
        "vibration":         [5, 3]        # arbitrary scale
    },
    "breaks": {
        "temperature":       [350, 100],
        "pressure":          [80, 40],     # psi
        "response_time":     [0.2, 0.1]    # seconds
    },
    "tires": {
        "temperature":       [330, 30],
        "pressure":          [220000, 20000],  # Pascals (~32 psi)
        "wear_level":        [20, 15],     # % wear
        "traction":          [7, 3]        # arbitrary scale (higher = better)
    }
}



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




