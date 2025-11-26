#!/usr/bin/env python3
import random
import copy
import multiprocessing
import time as t_lib
from datetime import datetime, timedelta, time
# influx
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# --- CONFIGURATION ---
URL = "http://localhost:8086"
TOKEN = "MyInitialAdminToken0=="
ORG = "YOUR_ORG"
BUCKET = "YOUR_BUCKET"

TRUCK_ID_RANGE = [0, 5] # Simulating truck IDs 0 to 4

# --- DATA TEMPLATES (CONSTANTS) ---

TEMPLATE_COMPONENTS = {
    "cpu": {
        "temperature":       [313, 353, 330],
        "power_consumption": [0, 300, 150],
        "current":           [0, 50, 25],
        "impact_force":      [0, 20, 10]
    },
    "proximity_sensor": {
        "distance":          [20, 180, 100],
        "power_consumption": [0, 3, 2],
        "current":           [0, 1, 0.5]
    },
    "impact_sensor": {
        "impact_force":      [0, 10_000, 0],
        "sensitivity":       [1, 100, 50],
        "power_consumption": [0, 5, 1]
    },
    "gps_chip": {
        "signal_strength":   [10, 55, 42],
        "power_consumption": [0, 2, 0.8],
        "current":           [0, 0.5, 0.1],
        "satellite_count":   [0, 24, 12]
    },
    "accelerometer": {
        "acceleration":      [0, 40, 9.8],
        "temperature":       [253, 343, 298],
        "power_consumption": [0, 1, 0.2]
    },
    "power_supply_unit": {
        "voltage":           [350, 450, 400],
        "current":           [0, 600, 120],
        "power_output":      [0, 200_000, 48_000],
        "temperature":       [293, 363, 330]
    },
    "temperature_sensor": {
        "temperature":       [243, 333, 293],
        "power_consumption": [0, 0.5, 0.1]
    },
    "humidity_sensor": {
        "humidity":          [0, 100, 65],
        "power_consumption": [0, 0.5, 0.1]
    },
    "front_light": {
        "luminosity":        [0, 8_000, 0],
        "power_consumption": [0, 150, 2],
        "temperature":       [253, 353, 293]
    },
    "engines": {
        "rpm":               [0, 12_000, 3_500],
        "temperature":       [293, 423, 350],
        "power_output":      [0, 150_000, 50_000],
        "vibration":         [0, 10, 2]
    },
    "breaks": {
        "temperature":       [273, 673, 300],
        "pressure":          [0, 3000, 0],
        "response_time":     [0.05, 1.0, 0.2]
    },
    "tires": {
        "temperature":       [263, 353, 310],
        "pressure":          [10_0000, 300_000, 220_000],
        "wear_level":        [0, 100, 15],
        "traction":          [1, 10, 8]
    }
}

TEMPLATE_ENVIRONMENT = {
    "temperature":  [283, 303, 293],
    "humidity":     [30, 90, 60],
    "luminosity":   [10_000, 30_000, 15_000]
}

TEMPLATE_VEHICLE_DATA = {
    "velocity":     [0, 9, 3],      # m/s
    "connectivity": [20, 200, 50]    # ms
}

TEMPLATE_BATTERY = {
    "current":      [0,200,100]
}

def generate_next_value(values_list):
    min_v, max_v, current_v = values_list
    step = (max_v - min_v) * 0.1
    change = random.uniform(-step, step)
    new_val = current_v + change
    return float(max(min_v, min(max_v, new_val)))


# --- TRUCK CLASS ---
class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.odometer = 0.0
        self.battery_level = 100.0
        
        self.components = copy.deepcopy(TEMPLATE_COMPONENTS)
        self.environment = copy.deepcopy(TEMPLATE_ENVIRONMENT)
        self.vehicle_data = copy.deepcopy(TEMPLATE_VEHICLE_DATA)
        self.battery_data = copy.deepcopy(TEMPLATE_BATTERY)

    def recharge(self):
        self.battery_level = 100.0
        self.battery_data = copy.deepcopy(TEMPLATE_BATTERY)

    def simulate_step(self, timestamp):
        """
        Updates the state of the truck and returns a list of InfluxDB Points.
        """
        points = []
        if self.battery_level <= 0.5:
            return points

        #? 1. Components Measurement
        for component_name, sensors in self.components.items():
            p = Point("components") \
                    .tag("truck_id", str(self.truck_id)) \
                    .tag("name", component_name) \
                    .time(timestamp)            
            for sensor_name, values in sensors.items():
                new_val = generate_next_value(values)
                values[-1] = new_val 
                p.field(sensor_name, new_val)
            
            points.append(p)

        #? 2. Environment Measurement
        p_env = Point("environment").tag("truck_id", str(self.truck_id)).time(timestamp)
        for sensor_name, values in self.environment.items():
            new_val = generate_next_value(values)
            values[-1] = new_val
            p_env.field(sensor_name, new_val)
        points.append(p_env)

        #? 3. Vihicle Measurement
        p_veh = Point("vehicle_data").tag("truck_id", str(self.truck_id)).time(timestamp)
        

        for sensor_name, values in self.vehicle_data.items():
            new_val = generate_next_value(values)
            values[-1] = new_val
            p_veh.field(sensor_name, new_val)
            

        self.odometer += random.uniform(1, 10)
        p_veh.field("odometer", self.odometer)
        
        points.append(p_veh)


        #? 4. Battery Measurement
        p_bat = Point("battery").tag("truck_id", str(self.truck_id)).time(timestamp)

        for sensor_name, values in self.battery_data.items():
            new_val = generate_next_value(values)
            values[-1] = new_val
            p_bat.field(sensor_name, new_val)
            
        if self.battery_level > 0:
            battery_down = random.uniform(0.001, 0.15) 
            self.battery_level -= battery_down
        else:
            self.battery_level = 0

        p_bat.field("battery_level", self.battery_level)
        points.append(p_bat)

        return points

# --- MAIN EXECUTION ---
def main():
    #! client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
    #! write_api = client.write_api(write_options=SYNCHRONOUS)

    fleet = [Truck(i) for i in range(TRUCK_ID_RANGE[0], TRUCK_ID_RANGE[1])]

    current_day = datetime(2025, 1, 1)
    end_date = datetime(2025, 2, 1)

    start_hour = time(6, 0, 0)
    end_hour = time(17, 0, 0)

    # print(f"Starting simulation for {len(fleet)} trucks...")

    while current_day <= end_date:
        current_time = datetime.combine(current_day.date(), start_hour)
        work_end = datetime.combine(current_day.date(), end_hour)
        
        # print(f"--- STARTING DAY: {current_day.date()} ---")
        while current_time <= work_end:
            
            batch_points = []
            
            for truck in fleet:
                truck_points = truck.simulate_step(current_time)
                if truck_points:
                    batch_points.extend(truck_points)
            
            # --- WRITE TO INFLUX ---
            if batch_points:
                # print(f"\n--- Time: {current_time} | Total Points: {len(batch_points)} ---")
                
                for p in batch_points:
                    print(p.to_line_protocol())
                #! write_api.write(bucket=BUCKET, org=ORG, record=batch_points)
            # else:
            #     print(f"Time: {current_time.time()} | All batteries empty.")

            current_time += timedelta(seconds=10)

        # print("End of shift. Recharging Fleet...")
        for truck in fleet:
            truck.recharge()
        current_day += timedelta(days=1)

if __name__ == "__main__":
    main()