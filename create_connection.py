import socket
from socket import *



def main():
    s = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'
    port = 443
    result = s.connect_ex((host, port))
    print('Result is {}'.format(result))
    s.close()

if __name__ == '__main__':
    main()
