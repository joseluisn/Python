# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 08:52:35 2019

@author: JOSE LUIS NOVOA
"""
class Person:
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def printFullName(self):
        print("Tu nombre es ",self.firstName,"",self.lastName)
nombres=[]
apellidos=[]

x=int(input("Ingresa cantidad de nombres a guardar: "))
for i in range (x):
    nom=input("Ingresa tu nombre")
    nombres.append(nom)
    ape=input("Ingresa tu apellido")
    apellidos.append(ape)

personName=Person()
personName.setFullName(nombres,apellidos)
personName.printFullName()