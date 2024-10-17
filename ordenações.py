import time
import random
#Sequências utilizadas:
arr100 = [random.randint(i, 100) for i in range(1, 101)]
arr1000 = [random.randint(i, 1000) for i in range(1, 1001)]
arr10000 = [random.randint(i, 10000) for i in range(1, 10001)]
arr1000000 = [random.randint(i, 1000000) for i in range(1, 1000001)]

print("----Tempos de Execução: Ordenação Por SELEÇÃO----")
def ordenação_seleção(arranjo: list):
    n = len(arranjo) #tamanho da lista
    for i in range(n):
        minimo = i #define o índice atual como o de menor valor
        for j in range(i + 1, n):
            if arranjo[minimo] > arranjo[j]: #se o próximo elemento for menor que o atual
                minimo = j #ele é o menor possível
            #continua comparando com o resto da lista até identificar o menor de todos.
        guarda = arranjo[i] #guarda o valor do índice atual
        arranjo[i] = arranjo[minimo] #coloca o menor valor encontrado no índice atual
        arranjo[minimo] = guarda #coloca o valor do índice atual na antiga posição do menor valor encontrado.

#calcula o tempo de execução:
inS100 = time.time()
ordenação_seleção(arr100)
fimS100 = time.time()
print("Para 100 elementos:", {fimS100 - inS100})

inS1000 = time.time()
ordenação_seleção(arr1000)
fimS1000 = time.time()
print("Para 1000 elementos:", {fimS1000 - inS1000})

inS10000 = time.time()
ordenação_seleção(arr10000)
fimS10000 = time.time()
print("Para 10.000 elementos:", {fimS10000 - inS10000})

'''inS1000000 = time.time()
ordenação_seleção(arr1000000)
fimS1000000 = time.time()
print("Para 1.000.000 elementos:", {fimS1000000 - inicioS1000000})'''

print("----Tempos de Execução: Ordenação Por INSERÇÃO----")
def ordenação_inserção(arranjo: list):
    for i in range(1, len(arranjo)): #inicia do segundo elemento
        pivo = arranjo[i] #define-o como pivo de comparação
        j = i - 1 #compara o pivo com todos os elementos que vem antes dele
        while (j >= 0) and (pivo < arranjo[j]): #se o pivo for menor que o elemento que vem antes dele
            arranjo[j + 1] = arranjo[j] #move o elemento maior que o pivo uma posição para frente, "criando" um espaço
            j = j - 1 #passa a comparar com o elemento anterior (até acabarem os elementos que vem antes do pivô)
        arranjo[j + 1] = pivo #coloca o pivô na posição vazia

#reembaralha a sequência:
random.shuffle(arr100)
random.shuffle(arr1000)
random.shuffle(arr10000)

#calcula o tempo de execução:
ini100 = time.time()
ordenação_inserção(arr100)
fimi100 = time.time()
print("Para 100 elementos:", {fimi100 - ini100})

ini1000 = time.time()
ordenação_inserção(arr1000)
fimi1000 = time.time()
print("Para 1000 elementos:", {fimi1000 - ini1000})

ini10000 = time.time()
ordenação_inserção(arr10000)
fimi10000 = time.time()
print("Para 10.000 elementos:", {fimi10000 - ini10000})

'''ini1000000 = time.time()
ordenação_inserção(arr1000000)
fimi1000000 = time.time()
print("Para 1.000.000 elementos:", {fimi1000000 - ini1000000})'''

print("---------Tempos de execução: HEAPSORT----------")
def heapify(arranjo: list, n: int, i: int):
    maior = i #maior elemento - "raiz" da árvore
    left = 2 * i + 1 #filho esquerdo
    right = 2 * i + 2 #filho direito

    #5 7 8 2 9 6 4 : 7 <- 5 -> 8 / 2 <- 7 -> 9 / 6 <- 8 -> 4
    #posições:       [1] [0]  [2] [3]  [1]  [4] [5]  [2]  [6]

    if left < n and arranjo[maior] < arranjo[left]: #se o filho esquerdo for maior que a raiz
        maior = left #ele é a nova raiz

    if right < n and arranjo[maior] < arranjo[right]: #se o filho direito for maior que o maior (raiz ou esquerdo)
        maior = right #ele é a nova raiz

    if maior != i: #se a raiz mudar com a análise dos filhos
        arranjo[i], arranjo[maior] = arranjo[maior], arranjo[i] #troca-se a raiz antiga de lugar com o novo maior elemento
        heapify(arranjo, n, maior) #verifica-se a árvore de novo para determinar se os filhos da nova raiz são menores que ela.

def heapSort(arranjo: list):
    n = len(arranjo) #tamanho do arranjo

    for i in range((n//2 - 1), -1, -1): #a partir da metade do arranjo - 1, 
        heapify(arranjo, n, i) #verifica se os filhos (nós que vem dps) são menores

    for i in range(n-1, 0, -1): #ordena os elementos
        arranjo[i], arranjo[0] = arranjo[0], arranjo[i] #coloca o maior elemento (raiz, que foi deixada na posição 0) na última posição, empurrando todos pra frente
        heapify(arranjo, i, 0)

#reenbaralha a sequência
random.shuffle(arr100)
random.shuffle(arr1000)
random.shuffle(arr10000)
random.shuffle(arr1000000)

#calcula o tempo de execução:
inH100 = time.time()
heapSort(arr100)
fimH100 = time.time()
print("Para 100 elementos:", {fimH100 - inH100})

inH1000 = time.time()
heapSort(arr1000)
fimH1000 = time.time()
print("Para 1000 elementos:", {fimH1000 - inH1000})

inH10000 = time.time()
heapSort(arr10000)
fimH10000 = time.time()
print("Para 10.000 elementos:", {fimH10000 - inH10000})

inH1000000 = time.time()
heapSort(arr1000000)
fimH1000000 = time.time()
print("Para 1.000.000 elementos:", {fimH1000000 - inH1000000})

print("---------Tempos de Execução: MERGESORT----------")
def merge(esquerda: list, direita: list):
    ordenada = []
    i = 0 #percorre a divisão esquerda
    j = 0 #percorre a divisão direita
    while i < len(esquerda) and j < len(direita): #se nenhumas das subdivisões tiverem acabado
        if esquerda[i] < direita[j]: #se o elemento da esquerda for menor que o da direita
            ordenada.append(esquerda[i]) #coloca-se o esquerdo primeiro no arranjo
            i += 1 #move-se na sublista esquerda
        else: #se o da direita for maior
            ordenada.append(direita[j]) #coloca-se o direito
            j += 1 #move-se na subdireita invés da esquerda

    while i < len(esquerda): #caso uma das sublistas acabe
        ordenada.append(esquerda[i])
        i += 1
    while j < len(direita):
        ordenada.append(direita[j]) #adiciona-se o restante dos elementos da outra (que supõe-se já estarem ordenados)
        j += 1
    return ordenada #retorna a lista final = esquerda + direita

def merge_sort(arranjo: list):
    if len(arranjo) <= 1: #se estiver vazia ou um elemento só, não há o que ordenar
        return arranjo
    meio = len(arranjo) // 2 #divide o arranjo em duas partes
    
    esquerda = arranjo[:meio] #esquerda
    direita = arranjo[meio:] #direita (a divisão impar deixa um elemento a mais na direita)
    esquerda = merge_sort(esquerda) #repete as divisões até restar um único elemento em cada sublista criada
    direita = merge_sort(direita) #repetindo até que todas as sublistas atendam len(arr) == 1.
    
    return merge(esquerda, direita) #começa a juntar as sublistas

#reembaralha a sequência
random.shuffle(arr100)
random.shuffle(arr1000)
random.shuffle(arr10000)
random.shuffle(arr1000000)

#calcula o tempo de execução:
inM100 = time.time()
merge_sort(arr100)
fimM100 = time.time()
print("Para 100 elementos:", {fimM100 - inM100})

inM1000 = time.time()
merge_sort(arr1000)
fimM1000 = time.time()
print("Para 1000 elementos:", {fimM1000 - inM1000})

inM10000 = time.time()
merge_sort(arr10000)
fimM10000 = time.time()
print("Para 10.000 elementos:", {fimM10000 - inM10000})

inM1000000 = time.time()
merge_sort(arr1000000)
fimM1000000 = time.time()
print("Para 1.000.000 elementos:", {fimM1000000 - inM1000000})