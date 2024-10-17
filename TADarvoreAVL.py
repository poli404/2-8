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
        self.altura: int = 1 #facilitar o balanceamento
        self.dado: item = dado

class arvore_avl:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        return self.raiz == None
    
    def preOrdem(self, no: no): #função de fora do TAD AVL
        if no != None:
            print(no.dado)
            self.preOrdem(no.esq)
            self.preOrdem(no.dir)

    def insere(self, x:item):
        self.raiz = self.insere_no(self.raiz, x)
    
    def busca(self, ch:int) -> item | None:
        no = self.busca_no(self.raiz, ch)
        if no != None:
            return no.dado
        else:
            return None
    
    def remove(self, chave: int) -> bool:
        self.raiz = self.remove_no(self.raiz, chave)

    def busca_no(self, n: no, chave:int) -> no | None:
        if n == None:
            return None
        elif chave > n.dado.chave:
            return self.busca_no(n.dir, chave)
        elif chave < n.dado.chave:
            return self.busca_no(n.esq, chave)
        else:
            return n
        
    def insere_no(self, n: no , x: item) -> no | None:
        if n == None:
            n = no(deepcopy(x))
        elif x.chave > n.dado.chave:
            n.dir = self.insere_no(n.dir,x)
        elif x.chave < n.dado.chave:
            n.esq = self.insere_no(n.esq,x)
        if n != None:
            n.altura = self.altura_no(n) #define a altura do novo nó após inserção
        return self.balanceia(n) #balanceia a árvore

    def maior(self, n: no) -> no:
        if n.dir == None:
            return n
        else:
            return self.maior(n.dir)
    
    def remove_no(self, n: no, chave: int) -> no | None:
        if n != None:
            if n.dado.chave < chave:
                n.dir = self.remove_no(n.dir, chave)
            elif n.dado.chave > chave:
                n.esq = self.remove_no(n.esq, chave)
            else:
                if n.esq != None and n.dir != None:
                    antecessor = self.maior(n.esq)
                    n.dado = antecessor.dado
                    n.esq = self.remove_no(n.esq, antecessor.dado.chave)
                elif n.esq == None:
                    n = n.dir
                else:
                    n = n.esq
        return self.balanceia(n) #balanceamento da árvore após a remoção
    
    def altura_no(self, n:no) -> int:
        altura_sad = 0 #altura da subárvore direita
        altura_sae = 0 #altura da subárvore esquerda
        altura_no = 0 #altura do nó n
        if n != None: #se não for o fim da árvore
            if n.dir != None: #se houver nó-filho à direita
                altura_sad = n.dir.altura #a altura da subárvore direita é a altura do nó-filho direito
            if n.esq != None: #se houver nó-filho à esquerda
                altura_sae = n.esq.altura #a altura da subárvore esquerda é a altura do nó-filho esquerdo
            altura_no = max(altura_sae,altura_sad) + 1 #a altura do nó é considerada a da subárvore mais alta (max) acrescida dele mesmo (+1).
        return altura_no #retorna a altura do nó
    
    def rotacao_esq(self, p: no) -> no:
        q = p.dir # p -> x = q
        p.dir = q.esq # p -> t <- x = q
        q.esq = p # p <- q
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q
    
    def rotacao_dir(self, p: no) -> no:
        q = p.esq # q = m <- p
        p.esq = q.dir # q = m -> n <- p
        q.dir = p # m = q -> p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q #nova raiz
    
    def rotacao_dupla_dir(self, p: no) -> no:
        q = p.esq # q = m <- p
        w = q.dir # q -> w = y
        q.dir = w.esq # q -> x <- w
        p.esq = w.dir # w -> z <- p
        w.esq = q # q <- w
        w.dir = p # w -> p
        
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        w.altura = self.altura_no(w)
        return w
    
    def rotacao_dupla_esq(self, p: no) -> no:
        q = p.dir # p -> x = q
        w = q.esq # w = r <- x = q
        q.esq = w.dir #
        p.dir = w.esq
        w.dir = q
        w.esq = p

        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        w.altura = self.altura_no(w)
        return w

    def balanceia(self, n: no) -> no:
        if n != None: #se a árvore não tiver acabado
            asd = self.altura_no(n.dir)
            ase = self.altura_no(n.esq)
            if asd > ase + 1 : #se a suárvore direita for mais alta (diferença de 2 ou mais nós)
                if self.altura_no(n.dir.esq) > self.altura_no(n.dir.dir): #analisa-se as subárvores da subávore mais alta
                    return self.rotacao_dupla_esq(n) #se a esquerda for maior, gira duas vezes pra esquerda
                else: #se a direita for maior
                    return self.rotacao_esq(n) #gira uma vez pra esquerda
            elif ase > asd + 1: #se a subárvore esquerda for maior
                if self.altura_no(n.esq.dir) > self.altura_no(n.esq.esq): #analisa as subárvores da subárvore
                    return self.rotacao_dupla_dir(n) #se a direita for maior, roda duas vezes pra direita
                else: #se a esquerda for maior
                    return self.rotacao_dir(n) #roda uma vez pra direita
            n.altura = self.altura_no(n) #define-se a nova altura do no após o balanceamento
        return n
    
    def string_ramo(self, n:no, nivel:int):
        s = '' #cria-se uma string
        s += '  '*nivel #adiciona-se um encadeamento dependedendo do nível do nó a partir da raiz (filhos tem 1 e netos 2 p.e.)
        s += '|____' #funciona como um alinhamento, deixar nós de mesmo nível alinhados
        if n != None: #se a árvore não acabar
            s += 'chave:' + str(n.dado.chave) +' - altura:'+ str(n.altura) +'\n' #adiciona o nó em uma linha da string
        else:
            s += '\n' #deixa como nulo/vazio o nó sem dados
        if n != None:
            str_esq = self.string_ramo(n.esq,nivel+1) #vai para a esquerda
            str_dir = self.string_ramo(n.dir,nivel+1) #vai para a direita
            s += str_esq + str_dir #adiciona os nós formados nas subárvores esquerda e direita a string
        return s

    def string(self):
        return self.string_ramo(self.raiz, 0) #inicia a string da árvore.