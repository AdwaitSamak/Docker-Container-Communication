import socket

HOST = '0.0.0.0'   # Binds the server to accept connections from any device on the network.
PORT = 8080      # Uses port 8080 for the server.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #socket object created
    s.bind((HOST, PORT))      # Associates the socket with the specified host and port.
    s.listen()                 # Starts listening for incoming connections.
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()            # Waits for and accepts a client connection, returning the connection object (conn) and client address (addr)
    with conn:
        print(f"Connected by {addr}")           #until data is received from client, it decodes the data and prints it. Else, if data is empty, i.e client stopped sending data, it breaks
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(data)               # Echo back the data to client
