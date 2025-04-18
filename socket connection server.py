import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432      # Port to listen on

server_socket = None
try:
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER] Listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"[SERVER] Connected by {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print("[SERVER] Client disconnected.")
                break
            print(f"[SERVER] Received: {data.decode()}")
            conn.sendall(f"Echo: {data.decode()}".encode())

except Exception as e:
    print(f"[SERVER] Error: {e}")

    if server_socket:
        server_socket.close()
        print("[SERVER] Socket closed.")
    print("[SERVER] Socket closed.")
"hello server"
print("[SERVER] Goodbye!")
exit()
