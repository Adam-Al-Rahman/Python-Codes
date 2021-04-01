#!/usr/bin/env python3

import subprocess
import random
import optparse
import re




def get_address():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", help="Interface to change it Mac address", dest="interface")
    parser.add_option("-m", "--mac", help="New Mac Address", dest="new_mac")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify mac address, use --help for more info")
    return options,arguments

def change_mac(interface,new_mac):

    print("[+] Changed Mac address for" + " " + interface + " " + "is" + " " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["airmon-ng", "check", "kill"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_address_change_result = re.search(br"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_change_result:
        return mac_address_change_result.group(0)
    else:
        print("Could not find the mac address. Please check it out.")

address =  [ "00:11:22:33:44:56", "00:11:22:33:44:57" , "00:11:22:33:44:58" ,"00:11:22:33:44:59"  ]
asking_which = input("Do you changed mac address in linux terminal (y/n) : ")


if asking_which.casefold() == "y":
    (options,arguments) = get_address()
    current_mac = get_current_mac_address(options.interface)
    print("Current mac: "+ str(current_mac))
    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac_address(options.interface)
    if current_mac == options.new_mac:
        print("The mac address does not changed")
    else:
        print("[+] The mac address successfully changed to: "+ str(current_mac))

elif asking_which == "n":
    ask = input("Shall I change (y/n) : ")
    if ask == "y":
        change_mac(input("For which interface : "),random.choice(address))
    else:
        exit()



