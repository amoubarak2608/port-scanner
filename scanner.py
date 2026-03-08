# import the socket library
import socket

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
for port in range(1, 101):
    if scan_port(ip, port):
        print("Port " + str(port) + " is open.")