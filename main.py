import socket # for socket
import sys

ip = socket.gethostname('www.google.com')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socjet succesfully created!")
except socket.error as err:
    print(f"Socket creation failed with error: {err}")

