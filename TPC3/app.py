import random

#Funções
def criar_lista_aleatória (tamanho):
    lista = []
    i = 0
    while i < tamanho:
        lista.append(random.randrange(1,101))
        i = i + 1
    return lista

def criar_lista_manual (tamanho):
    lista = []
    i = 0
    while i < tamanho:
        elemento=int(input(f"Introduza o elemento {i+1} :"))
        lista.append(elemento)
        i = i + 1
    return lista

def somar_lista (lista):
    soma=0
    for numero in lista:
        soma = soma + numero
    return soma 

def media_lista (lista):
    return somar_lista(lista)/len(lista)

def maior_elemento(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def menor_elemento(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

def ordem_crescente(lista):
    lista_copiada=lista.copy()
    lista_copiada.sort()
    return lista == lista_copiada

def ordem_decrescente(lista):
    lista_copiada=lista.copy()
    lista_copiada.sort()
    lista_copiada.reverse()
    return lista == lista_copiada

def procurar_numero(lista , elem):
    if elem in lista:
        return lista.index(elem)
    else:
        return -1

#Programa Principal

lista_de_numeros = []
opção = ""

while opção != "0":
    print("\n-----------------------------------------")
    print("   Aplicação de Manipulação de Listas")
    print("-----------------------------------------")
    print("(1) Criar Lista Aleatória")
    print("(2) Criar Lista Manualmente")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente?")
    print("(8) Está ordenada por ordem decrescente?")
    print("(9) Procurar um elemento")
    print("(0) Sair")
    print("-----------------------------------------")

    opção = input("Escolha uma opção: ")

    if opção == "1":
        tamanho = int(input("Quantos elementos quer na lista?: "))
        lista_de_numeros = criar_lista_aleatória (tamanho)
        print("Lista criada:" ,lista_de_numeros)
    
    elif opção == "2":
        tamanho=int(input("Quantos elementos quer na lista?: "))
        lista_de_numeros = criar_lista_manual (tamanho)
        print("Lista criada:" ,lista_de_numeros )

    elif opção == "3":
        print("Soma: ", somar_lista(lista_de_numeros))

    elif opção == "4":
        print("Média: ", media_lista(lista_de_numeros))

    elif opção == "5":
        print("O maior elemento da lista é: ", maior_elemento(lista_de_numeros))

    elif opção == "6":
        print("O menor elemento da lista é: ", menor_elemento(lista_de_numeros))

    elif opção == "7":
        if ordem_crescente(lista_de_numeros):
            print("A lista está ordenada por ordem crescente")
        else:
            print("A lista não está ordenada por ordem crescente")

    elif opção == "8":
        if ordem_decrescente(lista_de_numeros):
            print("A lista está ordenada por ordem decrescente")
        else:
            print("A lista não está ordenada por ordem decrescente")
        
    elif opção == "9":
        elemento=int(input("Qual o elemento que quer procurar?:"))
        posição=(procurar_numero(lista_de_numeros,elemento))
        print("O elemento está na posição:", posição)

    elif opção == "0":
        print("A sair... A lista final é: " ,lista_de_numeros)

    else: 
        print("Opção inválida!")