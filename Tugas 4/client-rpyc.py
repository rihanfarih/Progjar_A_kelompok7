#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_client.py
# RPyC client

import rpyc
import time

def main():
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    #fileobj = open('testfile.txt')
    #linecount = proxy.root.line_counter(fileobj, noisy)
    #print('The number of lines in the file was', linecount)
    pilihan = " "
    while(pilihan != "quit"):
        pilihan=input("Input command: ")
        msg=pilihan.split()
        if(msg[0] == "ls"):
            if(len(pilihan) == 2):
                proxy.root.ngelist1(cetak)
            else:
                msg2 = ' '.join(msg[1:])
                proxy.root.ngelist2(msg2, cetak)

        elif(msg[0] == "count"):
            msg2 = ' '.join(msg[1:])
            proxy.root.itung(msg2, cetak)
        elif(msg[0] == "put"):
            msg2 = ' '.join(msg[1:])
            proxy.root.put(msg2, cetak)
        elif(msg[0] == "get"):
            msg2 = ' '.join(msg[1:])
            proxy.root.get(msg2, cetak)
        elif(msg[0] == "quit"):
            proxy.root.quit(cetak)
            time.sleep(2)
            proxy.close()
        else:
            print("No Command, please retry\n==========================\n")
    

def noisy(string):
    print('Noisy:', repr(string))

def cetak(string):
    print(string)

if __name__ == '__main__':
    main()