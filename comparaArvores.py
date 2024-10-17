from TADarvoreABB import *
a1 = arvore()
for ch in [7, 4, 5, 20, 1, 3, 2, 8]:
    a1.insere(item(ch, 0))

a2 = arvore()
for ch in [3, 2, 1, 5, 4, 8, 7, 40]:
    a2.insere(item(ch, 0))

a3 = arvore()
for ch in [3, 2, 1, 5, 4, 8, 7, 20]:
    a3.insere(item(ch, 0))

#QUESTÃO 1:
def iguais(a1: arvore, a2: arvore) -> bool:
    "Cria uma lista com as chaves da segunda árvore, e busca-os na primeira pela função do TAD busca_no()"
    if a1.conta_nos(a1.raiz) == a2.conta_nos(a2.raiz): #se as árvores tiverem a mesma quantia de nós
        nosa2 = [] #lista
        a2.mostra_nos(a2.raiz, nosa2) #Função no TAD que adiciona todas as chaves dos nós de a2 na lista nosa2.
        for i in nosa2:
            if a1.busca_no(a1.raiz, i) == None: #se a chave de a2 não for encontrada em a1
                return False #um dos elementos de a2 não faz parte de a1 e elas não têm os mesmos elementos
        return True #caso todos os nós sejam encontrados em a1, as árvores tem os mesmos elementos.
    else: #caso uma árvore tenha mais nós, ela, necessariamente, possuirá mais chaves que a outra, portanto, não terão os mesmos elementos.
        return False #retorna-se Falso

print("------------Mesmos Elementos------------")
print("A2 e A3 =", iguais(a2, a3)) #False - um único elemento diferente.
print("A1 e A3 =", iguais(a1, a3)) #True - mesmos elementos em ordem diferente.

#QUESTÃO 2:
def maior_galho(a1: arvore, l1: list) -> list:
    "Mostra o(s) maior(es) galho(s) de uma árvore. O caminho mais longo entre a raiz a folha mais distante dela"
    galho_esq = [a1.raiz.dado.chave] #lista para subárvore esquerda da raiz
    galho_dir = [a1.raiz.dado.chave] #lista para análise da subávore direita da raiz
    a1.galho(a1.raiz.esq, galho_esq) #Função no TAD: busca o maior galho na subárvore esquerda
    a1.galho(a1.raiz.dir, galho_dir) #Função no TAD: retorna o maior galho à direita
    if len(galho_dir) < len(galho_esq): #caso o galho esquerdo seja maior
        l1 = [galho_esq] #o galho esquerdo é mostrado
    elif len(galho_dir) > len(galho_esq): #caso o direito seja maior
        l1 = [galho_dir] #apenas o direito é mostrado
    else: #caso os galhos tenham mesmo tamanho
        l1 = [galho_esq, galho_dir] #ambos os galhos são mostrados
    return l1

a4 = arvore()

for i in [item(5, 2), item(4, 8), item(2, 3), item(3, 4), item(7, 3), item(6, 7), item(9, 5), item(8, 2)]:
    a4.insere(i) #árvore da folha de exercícios com valores repetidos, porém chaves diferentes.

print("-----------Maior caminho/galho----------")
l4 = []
print("Em A4:", maior_galho(a4, l4)) #árvore mostrada na folha de exercícios, porém as chaves são mostradas
l1 = []
print("Em A1:", maior_galho(a1, l1))