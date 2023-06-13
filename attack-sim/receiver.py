import socket
import time

# Define the IP address and port on which the receiver program will listen
receiver_ip = '10.10.10.1'
receiver_port = 55551

# Create a socket and bind it to the receiver IP and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((receiver_ip, receiver_port))

# Listen for incoming connections
sock.listen(1)

# Accept the incoming connection from the sender machine
sender_sock, sender_address = sock.accept()

# Continuously receive data from the sender machine
while True:
    data = sender_sock.recv(1024).decode()  # Assuming the data is encoded as a string

    # Process the received data here
    # Example: Append the received data to the file accessible by the web service
    try:
        with open('/home/student/data.txt', 'a') as file:
            file.write(data + '\n')
    except:
        time.sleep(1)
