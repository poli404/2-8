from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    chave: int
    valor: float

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.dado: item = dado

class arvore:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        return self.raiz == None

    def preOrdem(self, no: no):
        if no != None:
            print(no.dado)
            self.preOrdem(no.esq)
            self.preOrdem(no.dir)

    def inOrdem(self, no: no):
        if no != None:
            self.inOrdem(no.esq)
            print(no.dado)
            self.inOrdem(no.dir)

    def posOrdem(self, no: no):
        if no != None:
            self.posOrdem(no.esq)
            self.posOrdem(no.dir)
            print(no.dado)

    def busca_no(self, n: no, chave: int) -> no | None:
        if n == None:
            return None
        elif chave > n.dado.chave: #se o número procurado for maior
            return self.busca_no(n.dir, chave) #compara-se com o próximo nó a direita
        elif chave < n.dado.chave: #se o número for menor
            return self.busca_no(n.esq, chave) #compara-se com o próximo a esquerda
        else: #se for igual
            return n #retorna-se o nó

    def busca(self, ch: int) -> item | None:
        no = self.busca_no(self.raiz, ch) #inicia-se a busca pelo número
        if no != None: #caso o nó seja encontrado
            return no.dado #retorna-se seus dados
        else: #caso o nó não seja encontrado (no == None)
          return None

    def insere(self, x: item):
        self.raiz = self.insere_no(self.raiz, x) #inicia-se a procura da posição de inserção do nó pela raiz

    def insere_no(self, n: no, x: item) -> no | None:
        if n == None: #ao "localizar" o lugar vazio para o nó
            n = no(deepcopy(x)) #adiciona-se o nó ao "fim" da árvore
        elif x.chave > n.dado.chave: #caso o novo nó seja maior
            n.dir = self.insere_no(n.dir, x) #procura-se mais a direita - insere-se mais a direita
        elif x.chave < n.dado.chave: #caso o nó seja menor
            n.esq = self.insere_no(n.esq, x) #procura-se mais a esquerda - insere-se mais a esquerda
        return n

    def maior(self, n: no):
        if n.dir == None: #caso o nó não possua subárvore direita
            return n #ele é o maior nó possível da árvore
        else: #caso ele o possua
            return self.maior(n.dir) #procura-se o maior nó da árvore indo cada vesz mais a direita

    def remove(self, x: int):
        self.raiz = self.remove_no(self.raiz, x) #inicia-se a busca pelo elemento a ser remvido pela raiz

    def remove_no(self, n: no, chave: int) -> no | None:
        if n != None: #caso não seja o fim da árvore - caso o nó ESTEJA na árvore;
            if n.dado.chave < chave: #se o nó procurado for maior
                n.dir = self.remove_no(n.dir, chave) #procura-se-o mais a direita
            elif n.dado.chave > chave: #caso seja menor
                n.esq = self.remove_no(n.esq, chave) #procura-se-o mais a esquerda (define-se o próximo nó como o próximo do próximo de forma a remover o nó quando encontrado)
            else:
                if (n.esq != None) and (n.dir != None): #caso o nó tenha dois filhos
                    antecessor = self.maior(n.esq) #procura-se o maior nó em sua subárvore esquerda
                    n.dado = antecessor.dado #define-se o dado do nó a ser retirado como o do elemento mais a direita da esquerda - apagando o antigo dado
                    self.remove_no(n.esq, antecessor.dado.chave) #remove-se o nó
                elif n.esq == None: #caso só tenha um filho a direita
                    n = n.dir #ele se torna o nó a direita
                else: #caso só tenha filho a esquerda
                    n = n.esq #ele se torna o nó a esquerda
        return n #se n == None, o nó não estava na árvore

    #Lista de exercícios
    def conta_nos(self, no: no):
        """Conta o número total de nós de uma árvore"""
        if no == None: #se acabar a árvore
            return 0 #não soma-se nada
        else: #se houver um nó
            return 1 + self.conta_nos(no.esq) + self.conta_nos(no.dir) #soma-se o nó a todos os outros a sua esquerda e a sua direita.
    
    def mostra_folhas(self, no: no):
        """esq - raiz - dir"""
        if no != None: #Se o nó existir
            if (no.dir == None) and (no.esq == None): #caso o nó não possua nenhuma subárvore
                print(no.dado) #imprime-se o  nó
            else: #caso ele possua subárvores.
                self.mostra_folhas(no.esq) #primeiro visitamos a esquerda
                self.mostra_folhas(no.dir) #depois visitamos a direita - InOrdem
    
    #QUESTÃO 1 - Segundo Trabalho:
    def mostra_nos(self, no: no, lista: list):
        """Coloca todos os nós da árvore em uma lista em Pré-ordem"""
        if no != None:
            self.mostra_nos(no.esq, lista) #coloca os nós à esquerda na lista
            lista.append(no.dado.chave) #coloca o no na lista
            self.mostra_nos(no.dir, lista) #coloca os nós à direita na lista
        return lista

    #QUESTÃO 2 - Segundo Trabalho:
    def altura_no(self, no: no):
        """Calcula a altura de um no"""
        if no == None: #se a árvore acabar
            return 0 #soma-se 0
        else: #soma-se o nível do nó à maior altura, à sua maior suabárvore.
            return 1 + max(self.altura_no(no.dir), self.altura_no(no.esq))
    
    def galho(self, no: no, lista: list):
        "Identifica os elementos que formam maior galho da árvore e o colocam em uma lista sequencialmente"
        if no != None:
            if self.altura_no(no.dir) > self.altura_no(no.esq): #se a subárvore direita for maior
                lista.append(no.dado.chave) #adiciona-se o nó-raiz a lista
                self.galho(no.dir, lista) #segue-se a lista pela direita
            else: #se a subárvore esquerda for maior
                lista.append(no.dado.chave) #adiciona-se o nó-raiz a lista
                self.galho(no.esq, lista) #segue-se pela subárvore esquerda
