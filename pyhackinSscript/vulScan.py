#! /bin/python3
import portScanner

targets_ip = input("[+]* Enter Target To scan For Vurnerable open Ports: ")
port_numbers = int(input("[+] * Enter Amount Of Ports You want to scan: "))
vul_file = input("[+]* Enter Path To The File With Vulnerable Software: ")
print("\n")

target = portScanner.PortScan(targets_ip, port_numbers)
target.Scan()

with open(vul_file, "r") as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
    for line in file.readlines():
        if line.strip() in banner:
            print(
                '"[!!!] VULNERABLE BANNER:" '
                + banner
                + '"ON PORT:" '
                + str(target.open_potrs[count])
            )
