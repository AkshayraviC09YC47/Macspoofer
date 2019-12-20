#usr/bin/env python3

#This program has been created by Akshay Ravi
#This is a random mac changer

import os
import subprocess

os.system("clear")

banner='''
                                __                    __           
             /\/\   __ _  ___  / _\_ __   ___   ___  / _| ___ _ __ 
            /    \ / _` |/ __| \ \| '_ \ / _ \ / _ \| |_ / _ \ '__|
           / /\/\ \ (_| | (__  _\ \ |_) | (_) | (_) |  _|  __/ |   
           \/    \/\__,_|\___| \__/ .__/ \___/ \___/|_|  \___|_|   
                                  |_|                              
           --------------------------------------------------------
               Random Mac Address Spoofer Created By Akshay Ravi
           --------------------------------------------------------
'''

print(banner)

subprocess.call("macchanger -s eth0" , shell=True)
print("")

value=input(str("[*] Do you want to spoof yor MAC Address?[y/n]: "))

if value =="y":
  print("[*] Spoofing MAC Address.....")
  print("[*] Your new MAC Address:")
  print("")
  subprocess.call("macchanger -r eth0" , shell=True)
  print("")
  
  value1=input(str("[*] Do you want to reset yor MAC Address?[y/n]: "))
  if value1 == "y":
          print("[*] MAC Address has been reset sucessfully")
          print("")
          subprocess.call("macchanger -p eth0" , shell=True)
elif value =="n":
  print("[*] Thank you for using MAC Spoofer")
  exit(1)
  

