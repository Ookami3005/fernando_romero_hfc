#!/usr/bin/python
# Hacking Fight Club

import socket
import argparse

parser = argparse.ArgumentParser(description="Escaner de puertos utilizando Socket")
parser.add_argument("direccion", type=str, help="Dirección IP por escanear")
parser.add_argument("-p", "--puertos", dest="puertos", type=str, help="Opcional: Puertos por escanear en formato p,p,p,p")
args = parser.parse_args()

target = args.direccion
if args.puertos:
    puertos = [int(i) for i in args.puertos.split(',')]
    for p in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if (s.connect_ex((target, p)) == 0) :
            print("El puerto "+ str(p) +" esta abierto!")
        s.close()
else:
    for i in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if (s.connect_ex((target, i)) == 0) :
            print("El puerto "+ repr(i) +" esta abierto!")
        s.close()
