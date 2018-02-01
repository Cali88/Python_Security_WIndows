import socket
from utils import timefunc

class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = [];

    def __repr__(self):
        return 'Scanner: {}'.format(self.ip)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.000001)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def add_port(self, port):
        self.open_ports.append(port)

    def write(self, filepath):
        openports = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(openports))

@timefunc
def main():
    ip = '127.0.0.1'
    scanner = Scanner(ip)
    scanner.scan(1, 65535)
    scanner.write('./open_ports')
    print(scanner.open_ports)



if __name__ == '__main__':
    main()
