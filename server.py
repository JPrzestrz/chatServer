import socket
import threading

HOST = '127.0.0.1' # IP address of the server
PORT = 5555 # Port number to listen on

clients = {} # Dictionary to store connected clients and their usernames

def handle_client(conn, addr):
    """Function to handle communications with a client."""
    print(f"New connection from {addr}")
    conn.sendall("Enter your username: ".encode('utf-8'))
    username = conn.recv(1024).decode('utf-8').strip()
    print(f"{addr} chose the username '{username}'")
    clients[conn] = username # Add the client and their username to the dictionary
    broadcast(f"{username} has joined the chat.")
    while True:
        data = conn.recv(1024) # Receive up to 1024 bytes of data
        if not data:
            break
        message = data.decode('utf-8')
        print(f"{username}: {message}")
        broadcast(f"{username}: {message}")
    conn.close()
    del clients[conn] # Remove the client from the dictionary
    broadcast(f"{username} has left the chat.")

def broadcast(message):
    """Function to broadcast a message to all connected clients."""
    for client, username in clients.items():
        client.sendall(message.encode('utf-8'))

def start_server():
    """Function to start the server and listen for incoming connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept() # Wait for a client to connect
            # Create a new thread to handle the client's communications
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == '__main__':
    start_server()
