Here's a Python script that uses the socket library to scan for open ports on a given host.
This script defines a function scan_ports that takes a host IP address, start port, and end port as parameters. 
It then iterates over the specified range of ports and attempts to connect to each port using a TCP socket. 
If the connection is successful (result equals 0), it prints the port number. 
The script sets a timeout of 1 second for each connection attempt to avoid hanging indefinitely.
To use the script, you need to replace "example.com" with the actual host IP address you want to scan. 
You can also adjust the start_port and end_port variables to scan a different range of ports.
Please note that scanning ports is a privileged action and may require authorization or be blocked by certain firewalls and security measures. 
Additionally, scanning a large range of ports can be intrusive and may be detected as a potential security threat. 
It is important to use this script responsibly and within the bounds of acceptable use and ethical hacking practices.
