# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:27:05 2020

@author: Camila Oliveira Cardoso
"""
import numpy as np
import pytest


def Fatorial(numero_inteiro):
    '''
    

    Parameters
    ----------
    numero_inteiro : recebe um número do tipo inteiro
    Returns
    -------
    produto : devolve o fatorial do número inteiro inserido do tipo inteiro

    '''
    produto = 1
    while numero_inteiro > 1:
        produto = produto * numero_inteiro
        numero_inteiro -= 1
    return produto

def Media(lista):
    '''
    

    Parameters
    ----------
    lista : é uma lista com valores do tipo inteiro ou ponto flutuante.

    Returns
    -------
    Devolve a média dos elementos contidos na lista, do tipo ponto flutuante.

    '''
    soma = 0
    for index in range(len(lista)):
        soma = soma + lista[index]
        
    return soma/len(lista)


vetor = [] #cria-se um vetor vazio

# O for percorre o vetor inserindo os respectivos valores 
for index in range(10):
    if index % 2 == 0:
        vetor.append((3 ** index) + 7 * Fatorial(index))
    else:
        vetor.append((2 ** index) + 4 * np.log(index))
        
        
# Imprime o maior valor do vetor, sua posição e a média dos valores do vetor
print("O maior valor do vetor é",max(vetor), "e está na posição",  vetor.index(max(vetor)),
      "\n A média dos valores contidos no vetor é:%.2f"  % Media(vetor) )


def test_Media():
    assert Media([-2,-5,1,2]) == -1