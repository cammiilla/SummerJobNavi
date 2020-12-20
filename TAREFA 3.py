# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:15:08 2020

@author: Camila Oliveira Cardoso
"""

contador = 0 # Variável que auxilia na contagem da quantidade de loopings no while
dic_alunos_notas = {} # Dicionário que armazena os nomes dos alunos com as respectivas notas
maior_nota = 0 # Variável que armazena a maior nota
melhor_aluno = ''


while contador < 5 :
    nome = input("Digite o nome do aluno: \n")
    nota = float(input("Digite a nota do aluno: \n"))
    dic_alunos_notas[nome] = nota
    contador += 1
    if nota > maior_nota:
        maior_nota = nota # Se a variável nota for maior que a variável maior_nota, maior_nota adquire seu valor
        melhor_aluno = nome
        

print("O/A aluno(a)", melhor_aluno, "conseguiu a nota mais alta da turma que foi:", maior_nota )

    
