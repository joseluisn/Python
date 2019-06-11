# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:13:41 2019

@author: CHIKE
"""
x=float(input("Ingresa el 1er numero: "))
y=float(input("Ingresa el 2er numero: "))
z=float(input("Ingresa el 3er numero: "))

print('El numero mas grande ingresado es: ',max(x,y,z))
print('La suma de %.1f + %.1f + %.1f=%.1f'%(x,y,z,x+y+z))
print('La resta de %.2f - %.2f - %.2f=%.2f'%(x,y,z,x-y-z))
input('presione cualquier tecla para salir')
