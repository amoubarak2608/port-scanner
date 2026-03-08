# import the socket library
import socket
# import the time library
import time

# common ports and their service names
common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy"
}

# ask the user for a target hostname and store it in a variable called target
target = input("Enter the target hostname: ")

# convert target to an IP using socket.gethostbyname() and store it in a variable called ip
ip = socket.gethostbyname(target)

# print the target and ip so the user knows what's being scanned
print("Target: " + target)
print("IP Address: " + ip)

# create a function called scan_port that takes host and port as parameters
    # this is where the port checking logic will go
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        return False
    except:
        return False

# loop through ports 1 to 101
    # inside the loop, call scan_port and print if the port is open
start_time = time.time()
for port in range(1, 101):
    if scan_port(ip, port):
        service = common_ports.get(port, "Unknown Service")
        print("Port " + str(port) + " is open. Service: " + service)
end_time = time.time()
print("Scan completed in " + str(round(end_time - start_time)) + " seconds.")