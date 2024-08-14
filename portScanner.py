import sys
import socket
from datetime import datetime

#Defining Target
if len(sys.argv) ==2:
    #Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid amount of arguments.")
    print("Syntax is portScanner.py <ip>")
    exit()

#Banner
print("\n")
print("#" * 50)
print("Scanning target " + target)
print("Time Started "  + str(datetime.now()))
print("#" * 50)
print("\n")


try:
    for port in range(81,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns error indicator
        
        print("Checking port: " + str(port))

        if result ==0:
            print("Port {} open".format(port))
        
        s.close()

    print("Finished Scanning")

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved")
    sys.exit()

except socket.error:
    print("\nHCouldn't connect to serverß")
    sys.exit()
    

