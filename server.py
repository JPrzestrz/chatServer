import socket
import threading

HOST = '127.0.0.1' # IP address of the server
PORT = 5555 # Port number to listen on
BUFFER_SIZE = 1024 # Maximum message size

clients = {} # Dictionary of connected clients

def broadcast(message, sender):
    """Function to broadcast a message to all connected clients."""
    for client, client_sock in clients.items():
        if client_sock != sender:
            client_sock.sendall(message)

def handle_client(client_sock, address):
    """Function to handle a client connection."""
    username = client_sock.recv(BUFFER_SIZE).decode('utf-8')
    clients[username] = client_sock
    print(f"Client {username} connected from {address}")
    broadcast(f"{username} joined the chat", client_sock)
    while True:
        message = client_sock.recv(BUFFER_SIZE).decode('utf-8')
        if message.startswith('/quit'):
            break
        broadcast(message, client_sock)
    client_sock.close()
    del clients[username]
    broadcast(f"{username} left the chat", None)

def start_server():
    """Function to start the server program."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started on {HOST}:{PORT}")
        while True:
            client_sock, address = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_sock, address))
            client_thread.start()

            # Wait for input from the administrator to shut down the server
            shutdown_input = input("Enter /quit to shut down the server\n")
            if shutdown_input == '/quit':
                print("Shutting down the server gracefully...")
                for client_sock in clients.values():
                    client_sock.sendall("/quit".encode('utf-8'))
                s.close()
                break

if __name__ == '__main__':
    start_server()