# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:48:10 2019

@author: CHIKE
"""

nombres=[]
x=int(input("Ingresa cantidad de nombres a guardar: "))
for i in range (x):
    nom=input("Ingrese nombre:")
    nombres.append(nom)
print("Los nombres guardados en la lista son",nombres)
print("El tamaño de la lista es",len(nombres))
#impresion de lista recorriendola
print("impresion de lista recorriendola")
for i in nombres:
    print(i)
supr=(input("Ingresa nombre a eliminar de la lista: "))
if supr in nombres:
    nombres.remove(supr)
    print("La lista despues de eliminar",nombres)
    print("El tamaño de la lista ahora es de",len(nombres))
else:
    print("El elemento no esta en la lista")
