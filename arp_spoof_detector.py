import os 
import datetime
import time

def arp_table_extraction():
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    addresses = {}
    for line in arp_table_lines:
        if "ff-ff-ff-ff-ff-ff" in line or "ff:ff:ff:ff:ff:ff" in line:
            break
        if arp_table_lines.index(line) > 2:
            ip, mac, _type = line.split()
            addresses[ip] = mac 
    identify_duplication(addresses)

def identify_duplication(addresses):
    tmp_mac_lst = []
    print("Scanning...")
    time.sleep(3)
    for mac in addresses.values():
        if mac in tmp_mac_lst:
            print("Finished scanning")
            create_log(f'ARP Spoofed!! \n The offending MAC is: {mac}')
            break

def create_log(message):
    print("Generating logs...")
    time.sleep(3)
    date = datetime.datetime.now()
    with open("log.txt", "a")as log:
        log.write(message + "\n Date: {} \n\n".format(date))
    print("The event is logged in log.txt")


if __name__ == "__main__":
    arp_table_extraction()

input("\nPress 'Enter' to exit the program")
