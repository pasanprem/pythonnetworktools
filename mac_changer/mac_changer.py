#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface. Use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC. Use --help for more information.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac)
    # The necessary shell commands
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)