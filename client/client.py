import socket

HOST = 'server'  # specoifies the host to connect to
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #create socket object
    s.connect((HOST, PORT))       # Connects to the server at the specified host and port.
    s.sendall(b"Hello from client!")    # Sends a message to the server
    data = s.recv(1024)          # Receives data from the server
    print(f"Received: {data.decode()}")    #prints received data
