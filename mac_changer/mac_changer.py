#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth1 down", shell=True)
subprocess.call("ifconfig eth1 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth1 up", shell=True)