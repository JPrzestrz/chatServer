import socket
import threading

HOST = '127.0.0.1' # IP address of the server
PORT = 5555 # Port number to connect to

def receive_messages(sock):
    """Function to receive messages from the server."""
    while True:
        data = sock.recv(1024) # Receive up to 1024 bytes of data
        if not data:
            break
        message = data.decode('utf-8')
        print(message)
        print("> ", end='', flush=True)

def start_client():
    """Function to start the client program."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")
        username = input("Enter your username: ")
        s.sendall(username.encode('utf-8'))
        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=receive_messages, args=(s,))
        receive_thread.start()
        # Start the main loop
        while True:
            print("> ", end='', flush=True)
            message = input()
            s.sendall(f" {message}".encode('utf-8'))
            print("\033[A\033[K> ", end='', flush=True)

if __name__ == '__main__':
    start_client()
