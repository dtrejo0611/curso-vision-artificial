# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 17:56:55 2025

@author: dtrej
"""

"""
Realiza un sistema de login
"""

USUARIO_REG = "David"
CONTRASEÑA_REG = "12345"

usuario = input("Ingresa el usuario: ")
contraseña = input("Ingresa la contraseña: ")

condicion = (USUARIO_REG == usuario) and (CONTRASEÑA_REG == contraseña)

print("Haz logrado entrar al sistema: ", condicion)