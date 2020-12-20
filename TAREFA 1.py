# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:12:49 2020

@author: Camila Oliveira Cardoso
"""

contador = 0 # Contador atualiza o número de vezes em que um número satisfaz o critério

"""
A variável numero_teste percorre apenas números pares a partir de 50, pois 
não existem multiplos pares em comum com 49 e 37 no intervalo de 1 a 50.
"""

for numero_teste in range (50,5*(10**6),2):
    if (numero_teste % 49 == 0) and (numero_teste % 37 == 0):
        contador += 1
print("Existem",contador,"números pares, multiplos de 49 e 37 simultaneamente!")
