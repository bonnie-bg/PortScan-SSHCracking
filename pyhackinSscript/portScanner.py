#! /bin/python3
import socket
from IPy import IP


class PortScan:
    banner = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    # scan ip addresses
    def Scan(self):
        # coverted_ip = check_ip(self.target)
        # print("\n" + "[-_0 Scanning Target] " + str(target))
        for port in range(1, port_num):
            # self.Scan_Port(coverted_ip, port)
            self.Scan_Port(port)

    # convert domain name to ip address
    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            # return ip address of domain name
            return socket.gethostbyname(self.target)

    # return information from port in bits encoded decoded sa banner.decode()
    """ def Get_banner(s):
        return s.recv(1024)
    """
    # scan ports
    def Scan_Port(self, port):
        try:
            coverted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeoutet(0.5)
            socket.connect((coverted_ip, port))
            self.open_ports.append(port)
            # to retive information from port number opened
            try:
                banner = sock.recv(1024).decode().strip("\n").split("\r")
                # print("[+] Port" + str(port) + " : " + str(banner.decode().strip("\n")))
                self.banner.append(banner)

            except:
                # print("[+] Port" + str(port))
                self.banner.append("")
            socket.close()
        except:
            # """print("[-] Port' + str(port) +' is Closed")"""
            pass


# portscan = PortScan()
# run if only portScanner run
if __name__ == "__main__":
    targets = input(
        "[+] Enter IP address Of Terget/s To scan (split multiple targets with ,): "
    )
    port_num = int(input("[+] Enter port range number to scan : "))
    if "," in targets:
        for ip_add in targets.split(","):
            Scan(ip_add.strip(""), port_num)

    else:
        Scan(targets, port_num)
