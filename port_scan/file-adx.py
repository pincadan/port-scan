import socket

def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage
host = "example.com"
start_port = 1
end_port = 1024
scan_ports(host, start_port, end_port)