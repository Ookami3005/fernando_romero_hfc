#!/usr/bin/python
# Hacking Fight Club

import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib

arbol = ET.parse('nmap.xml')
raiz = arbol.getroot()

def obtenerTiempoInicio():
    cadena = ""
    hora = int(raiz.get('start'))
    fecha = datetime.fromtimestamp(hora)
    return fecha

def obtenerHosts(estado):
    dicc = {
        True:'up',
        False:'down'
    }

    hosts = 0
    for host in raiz.findall('host'):
        status = host.find('status')
        direccion = host.find('address').get('addr')
        if status.get('state') == dicc[estado]:
            hosts += 1
    return hosts

def obtenerHostsConPuerto(num):
    hosts = 0
    for host in raiz.findall('host'):
        puertos = host.find('ports')
        if puertos != None:
            for puerto in puertos.findall('port'):
                if int(puerto.get('portid')) == num:
                    hosts += 1
    return hosts

def obtenerHostsConNombresDominio():
    hosts = 0
    for host in raiz.findall('host'):
        puertos = host.find('ports')
        if puertos != None:
            for puerto in puertos.findall('port'):
                servicio = puerto.find('service')
                if servicio.get('name')=='domain':
                    hosts += 1
    return hosts


def obtenerHostsConHoneypots():
    hosts = 0
    for host in raiz.findall('host'):
        puertos = host.find('ports')
        if puertos != None:
            for puerto in puertos.findall('port'):
                servicio = puerto.find('service')
                if servicio.get('name')=='honeypot':
                    hosts += 1
    return hosts


def obtenerHostsConServidorHTTP(marca):
    hosts = 0
    for host in raiz.findall('host'):
        puertos = host.find('ports')
        if puertos != None:
            for puerto in puertos.findall('port'):
                servicio = puerto.find('service')
                if servicio.get('name')=='http' and servicio.get('product') == marca:
                    hosts += 1
    return hosts

def hashearArchivo(opcion):
    hash = ""
    lector = open('nmap.xml','r')
    contenido = lector.read().encode("utf-8")
    lector.close()
    if opcion:
        hash = hashlib.md5(contenido).hexdigest()
    else:
        hash = hashlib.sha1(contenido).hexdigest()
    return hash

def informacionRecopilada():
    resultado = "El mapeo se ejecuto en: %s" % obtenerTiempoInicio()
    resultado += "\n\nEstado de los hosts:\n"
    resultado += "Hosts prendidos: %s\n" % obtenerHosts(True)
    resultado += "Hosts prendidos: %s\n" % obtenerHosts(False)
    resultado += "\nPuertos:\n"
    resultado += "Puertos con el puerto 22: %s\n" % obtenerHostsConPuerto(22)
    resultado += "Puertos con el puerto 53: %s\n" % obtenerHostsConPuerto(53)
    resultado += "Puertos con el puerto 80: %s\n" % obtenerHostsConPuerto(80)
    resultado += "Puertos con el puerto 443: %s\n" % obtenerHostsConPuerto(443)
    resultado += "\nDominios:\n"
    resultado += "Hosts con nombres de dominio: %s\n" % obtenerHostsConNombresDominio()
    resultado += "\nServidores HTTP:\n"
    resultado += "Hosts con Honeypots: %s\n" % obtenerHostsConHoneypots()
    resultado += "Hosts con Apache: %s\n" % obtenerHostsConServidorHTTP('Apache httpd')
    resultado += "Hosts con Nginx: %s\n" % obtenerHostsConServidorHTTP('nginx')
    resultado += "\nHashes:\n"
    resultado += "MD5: %s\n" % hashearArchivo(True) 
    resultado += "SHA1: %s" % hashearArchivo(False) 
    return resultado

info = informacionRecopilada()
escritor = open('reporte.txt','w')
escritor.write(info)
print(info)
