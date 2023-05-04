import socket

# Define the range of IP addresses to scan
ip_range = ""
start_port = 1
end_port = 1000

# Loop through all IP addresses in the range and all ports in the range
for ip in range(1, 255):
    for port in range(start_port, end_port + 1):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)

        # Attempt to connect to the IP address and port
        try:
            result = s.connect_ex((ip_range + str(ip), port))
            if result == 0:
                print(f"Port {port} is open on {ip_range}{ip}")
        except:
            pass

        # Close the socket object
        s.close()
