# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:07:46 2020

@author: Sajal
"""


import subprocess

a = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

for i in a:
    results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    try:
        print ("{:<30}|  {:<}".format(i,results[0]))
    except indexError:
         print ("{:<30}|  {:<}".format(i,""))