#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice

from poo1 import Alumno

calificacion_alumno = []
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = [
    'Angel Sánchez',
    'Esteban Arellanes',
    'Danna Márquez',
    'Fernando Romero',
    'Alberto Medel',
    'Luis Lira',
    'Obed Torres',
    'Oscar Caballero',
    'Oscar Ríos',
    'Stephany Marín',
    'Jonathan Valencia',
    'Valeria Ramírez',
    'Israel Villanueva',
    'Juan Legorreta']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno.append(Alumno(b,choice(calificaciones)))

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno.nombre,alumno.calificacion))

def separaAprobadosReprobados():
    aprobados = ()
    reprobados = ()
    for alumno in calificacion_alumno:
        if(alumno.calificacion >= 7):
            aprobados = aprobados + (alumno,)
        else:
            reprobados = reprobados + (alumno,)
    return [aprobados,reprobados]

def promedioAlumnos():
    suma = 0
    for alumno in calificacion_alumno:
        suma += alumno.calificacion
    return suma / len(calificacion_alumno)

def conjuntoCalificaciones():
    calificaciones = set()
    for alumno in calificacion_alumno:
        calificaciones.add(alumno.calificacion)
    return calificaciones


asigna_calificaciones()
imprime_calificaciones()

listaTuplas = separaAprobadosReprobados()
print("Los aprobados son: "+str(listaTuplas[0]))
print("Los reprobados son: "+str(listaTuplas[1]))
print("\nEl promedio de las calificaciones es: "+str(promedioAlumnos()))
print("El conjunto de calificaciones es "+str(conjuntoCalificaciones()))

