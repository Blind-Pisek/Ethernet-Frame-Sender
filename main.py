import socket
import time

CONFIG_FILE_PATH = "config.txt"
MESSAGE_FILE_PATH = "message.txt"

CONFIG_FILE = open(CONFIG_FILE_PATH, mode ="r",
                    encoding = "utf-8")

MESSAGE_FILE = open(MESSAGE_FILE_PATH, mode ="r",
                    encoding = "utf-8")


UDP_IP = CONFIG_FILE.readline().rstrip("\n")
UDP_PORT = int( CONFIG_FILE.readline() )
SERVER_ADDRESS = (UDP_IP , UDP_PORT)

INTERNET_SOCKET = socket.socket( socket.AF_INET,     # Internet
                                 socket.SOCK_DGRAM ) # UDP

DELAY = int( CONFIG_FILE.readline() )
MS_DELAY = DELAY/1000

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("Sending frame delay in ms: %s" % MS_DELAY)

FRAMES = []

for LINE in MESSAGE_FILE:
    ELEMENT = LINE[:-1]
    FRAMES.append( ELEMENT )


while True:
    for FRAME in FRAMES:
        print(FRAME)
        INTERNET_SOCKET.sendto( bytes(FRAME, "utf-8"),
                                SERVER_ADDRESS )
        time.sleep(MS_DELAY)
    print("Sending again!!!")

CONFIG_FILE.close()
MESSAGE_FILE.close()