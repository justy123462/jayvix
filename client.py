import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = None
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[CLIENT] Connected to {HOST}:{PORT}")

    while True:
        msg = input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        client_socket.sendall(msg.encode())
        response = client_socket.recv(1024)
        print(f"[CLIENT] Server responded: {response.decode()}")

except ConnectionRefusedError:
    print("[CLIENT] Connection failed. Server might be down.")
except Exception as e:
    print(f"[CLIENT] Error: {e}")

    if client_socket:
        client_socket.close()
    client_socket.close()
    print("[CLIENT] Disconnected.")
    exit()
print("[CLIENT] Goodbye!")
exit()
