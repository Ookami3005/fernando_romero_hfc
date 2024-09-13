#!/usr/bin/python
# Hacking Fight Club

from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description="Escaner de puertos utilizando Scappy")
parser.add_argument("direccion", type=str, help="Dirección IP por escanear")
parser.add_argument("-p", "--puertos", dest="puertos", type=str, help="Opcional: Puertos por escanear en formato p,p,p,p")
args = parser.parse_args()

def escanear_puerto_syn(ip, puerto):
    paquete = IP(dst=ip)/TCP(dport=puerto, flags="S")
    respuesta = sr1(paquete, timeout=0.5, verbose=0)

    if respuesta is None:
        return "El puerto %s esta filtrado" % puerto
    elif respuesta.haslayer(TCP):
        if respuesta.getlayer(TCP).flags == 0x12: # SYN-ACK
            send(IP(dst=ip)/TCP(dport=puerto, flags="R"), verbose=0)
            return "El puerto %s esta abierto" % puerto
        elif respuesta.getlayer(TCP).flags == 0x14: # RST-ACK
            return "El puerto %s esta cerrado" % puerto
    return "El estado del puerto %s es desconocido" % puerto

target = args.direccion
if args.puertos:
    puertos = [int(i) for i in args.puertos.split(',')]
    for p in puertos:
        print(escanear_puerto_syn(target, p))
else:
    for i in range(1,65536):
        print(escanear_puerto_syn(target, i))
