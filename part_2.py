import threading
from socket import *
import time

BroadcastAddress = '192.168.0.255'
broadcastPort = 5051
saved_messages = {}
def Sender():
    message = input('For Sending : Enter your first and last name: And yor message. For peers sending\n')
    line_num = "1D"
    PeerSend = socket(AF_INET, SOCK_DGRAM) #Creating UDP connection
    PeerSend.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #Enabling broadcasting
    PeerSend.sendto(line_num.encode(), (BroadcastAddress, broadcastPort))
    PeerSend.sendto(message.encode(), (BroadcastAddress, broadcastPort))
    PeerSend.close()

def Receiver():
    PeerReceive = socket(AF_INET, SOCK_DGRAM) #Creating UDP connection
    PeerReceive.bind(('', broadcastPort))
    counter = ""
    string_list= []
    print(f"For Listening on broadcast messages on {BroadcastAddress}:{broadcastPort}...")
    while True:
        message, PeerAddress = PeerReceive.recvfrom(2048)
        if len(message.decode()) == 2:
            string_list.append(message.decode())
            counter = message.decode()

        else:
            length = len(string_list)
            display(message.decode(),f"{length}D")


def display(message , counter):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # Find the index of the first occurrence of ":"
    colon_index = message.find(":")
    # Extract the First and Last name
    name = message[:colon_index]
    saved_messages[counter] = message[colon_index + 1:]
    if counter == "1D":
        print(f"Peer {name}\n")
    print(f"{counter}- received a message from {name} at {current_time}\n")
    while counter == "3D":
        num = input("Enter a number line\n")
        print(f"{saved_messages[num]}\n")


if __name__ == "__main__":
    t1 = threading.Thread(target=Sender)
    t2 = threading.Thread(target=Receiver)
    t1.start()
    t2.start()
    t1.join()
    t2.join()