# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:31:48 2019

@author: CHIKE
"""

x=int(input("Ingresa 1er numero: "))
y=int(input("Ingresa 2do numero: "))
if x<y:
    print("%d es menor que %d"%(x,y))
elif x>y:
    print("%d es mayor que %d"%(x,y))
elif x==y:
    print("%d es igual que %d"%(x,y))
print ("La suma de %d + %d es:%d"%(x,y,x+y))
print ("La multiplicacion de %d * %d es:%d"%(x,y,x*y))
print ("La division de %d / %d es:%d"%(x,y,x/y))
print ("El residuo de %d / %d es:%d"%(x,y,x%y))