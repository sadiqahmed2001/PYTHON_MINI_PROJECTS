import time
import random

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

class TrafficSignal:
    def __init__(self):
        self.green_duration = 10  # duration of green signal in seconds
        self.red_duration = 5     # duration of red signal in seconds

    def change_signal(self):
        print("Traffic signal changed to GREEN")
        time.sleep(self.green_duration)
        print("Traffic signal changed to RED")
        time.sleep(self.red_duration)

class IoT_Sensor:
    def __init__(self):
        pass

    def detect_vehicle(self):
        # Simulate vehicle detection
        return random.choice([True, False])

class TrafficControlSystem:
    def __init__(self):
        self.traffic_signal = TrafficSignal()
        self.iot_sensor = IoT_Sensor()

    def control_traffic(self):
        while True:
            if self.iot_sensor.detect_vehicle():
                print("Vehicle detected")
                self.traffic_signal.change_signal()
            else:
                print("No vehicle detected")
                time.sleep(1)  # wait for 1 second before checking again

if __name__ == "__main__":
    traffic_system = TrafficControlSystem()
    traffic_system.control_traffic()
