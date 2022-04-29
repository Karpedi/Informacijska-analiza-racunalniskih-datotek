'''
* Copyright (c) 2021 University of Ljubljana, Faculty of Electrical Engineering.
* All rights reserved. Licensed under the Academic Free License version 3.0.
* 
* 
*
* Program izracuna entropijo podatkov.  Program zaženemo tako, da pokličemo python prva.py in sledimo nadaljnim
navodilom, torej odtipkati moramo ime datoteke in pa število od 1 do 5!
'''

import math

datoteka= input("Vnesi ime datoteke : ") 
dolzinaNiza_branje = input('Vtipkaj dolzino niza od 1 do 5: ')
filejz = datoteka #"tu pridejo različne datoteke glede na to kaj smo vpisali na začetku"

f = open(filejz, 'rb') #odpre filejz --> bere po bytih
besede = f.read() #vrnemo besedilo v obliki bytov
n = int(dolzinaNiza_branje)
abeceda = {}

#sestavimo abecedo
for i in range(len(besede)-n):
        key = besede[i:i+n]

        if key in abeceda:
            abeceda[key] += 1
        else:
            abeceda[key] = 1

#izracunamo entropijo [Shannonova entropija ]
entropija = 0
for _,j in abeceda.items():
    entropija = entropija + (1.0*j/len(besede))*math.log(1.0*j/len(besede), 2)

entropija = -entropija/n
print("Datoteka: %s" %filejz)            
print("entropija: %s" %entropija)  