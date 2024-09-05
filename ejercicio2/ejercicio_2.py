#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice

calificacion_alumno = {}
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
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))

def separaAprobadosReprobados():
    aprobados = []
    reprobados = []
    for alumno in calificacion_alumno:
        if(calificacion_alumno[alumno] >= 7):
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)
    return [tuple(aprobados),tuple(reprobados)]

def promedioAlumnos():
    suma = 0
    for alumno in calificacion_alumno:
        suma += calificacion_alumno[alumno]
    return suma / len(calificacion_alumno)

def conjuntoCalificaciones():
    calificaciones = []
    for alumno in calificacion_alumno:
        calificaciones.append(calificacion_alumno[alumno])
    return set(calificaciones)



asigna_calificaciones()
imprime_calificaciones()

listaTuplas = separaAprobadosReprobados()
print("Los aprobados son: "+str(listaTuplas[0]))
print("Los reprobados son: "+str(listaTuplas[1]))
print("\nEl promedio de las calificaciones es: "+str(promedioAlumnos()))
print("El conjunto de calificaciones es "+str(conjuntoCalificaciones()))

