# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 17:45:26 2025

@author: dtrej
"""

'''
Suponga que se toman 3 muestras de un sensor de temperatura colocado en un
motor de cierta maquina, se desea saber si el promedio de dicha temperatura
sobrepasa los 100°C, esta a punto de sobrepasarlo o es menor o igual a 80°C
además mostrar en la consola la temperatura promedio
'''

T1 = float(input("Ingrese la primera medicion: "))
T2 = float(input("Ingrese la segunda medicion: "))
T3 = float(input("Ingrese la tercera medicion: "))

promedio = (T1 + T2 + T3) / 3

print("El promedio de las 3 mediciones es: ", promedio, "°C", sep="")

print("La temperatura promedio sobrepasa los 100°C: ", promedio > 100)
print("La temperatura promedio esta a ounto de sobrepasar los 100°C: ", 80 < promedio < 100)
print("La temperatura promedio es menor o igual a 80°C: ", promedio <= 80)