import time
import random
import socket

def generate_plc_data():
    temperature = 25  # Initial temperature
    wattage = 10  # Initial wattage
    switch_state = 1  # Initial switch state (ON)

    # Define the temperature range and rate of change
    temperature_min = 20
    temperature_max = 40
    temperature_rate = 1  # Rate of change per second

    # Define the wattage range and spike limit
    wattage_min = 3
    wattage_max = 25
    wattage_spike_limit = 2

    # Generate data for 1 hour
    end_time = time.time() + 3600  # 1 hour from now

    while time.time() < end_time:
        # Generate temperature data with a steady up or down change
        temperature += random.choice([-1, 1]) * temperature_rate
        temperature = max(temperature_min, min(temperature, temperature_max))

        # Generate wattage data with random spikes
        wattage += random.choice([-1, 1]) * wattage_spike_limit
        wattage = max(wattage_min, min(wattage, wattage_max))

        # Generate switch state data (ON/OFF)
        switch_state = random.choice([0, 1])

        # Format the data as a string in S7Comm format
        data = f"Temperature: {temperature} C, Wattage: {wattage} W, Switch State: {switch_state}"

        # Send the data to the receiver machine
        sender_sock.sendall(data.encode())

        # Wait for 1 second before generating the next data point
        time.sleep(1)

# Define the IP address and port of the receiver machine
receiver_ip = '10.10.10.1'
receiver_port = 55551

# Create a socket and connect to the receiver machine
sender_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender_sock.connect((receiver_ip, receiver_port))

# Generate and send simulated S7Comm data
generate_plc_data()
