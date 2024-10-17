from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class figurinhaD:
    Numero: int | None #considerado como a chave, só se pode ter um nó com x número
    Quantidade: int | None

class no:
    def __init__(self, x: figurinhaD):
        self.dado: figurinhaD = x
        self.prox: no | None = None

class coleçãoD:
    def __init__(self):
        """Uso de lista com sentinela - não hánecessidade de movimentação dos ponteiros primeiro e último"""
        self.primeiro = no(figurinhaD(None,None))
        self.ultimo = self.primeiro
    
    def vaziaD(self) -> bool:
        """Verifica se a coleção tem figurinhas"""
        return self.primeiro.prox == None #True
    
    def novafigurinhaD(self, x: figurinhaD):
        """Insere uma figurinha na coleção - repetida ou nova"""
        nova = no(x)
        if not self.vaziaD(): #caso hajam figurinhas na coleção
            ptr = self.primeiro.prox
            if ptr.dado.Numero < x.Numero: #se a nova figurinha for maior que a primeira da coleção
                while (ptr.prox != None) and (ptr.prox.dado.Numero < nova.dado.Numero):
                    ptr = ptr.prox #avança na coleção se as figurinhas presentes forem menores que a nova.
                
                if (ptr.prox != None) and (ptr.prox.dado.Numero == x.Numero): #caso o número da nova figurinha seja igual a próxima (uma figurinha repetida)
                    ptr.prox.dado.Quantidade += x.Quantidade #adiciona-se à quantidade.
                
                else: #caso rode até o final (== None) ou a figurinha seguinte (.prox) não tenha mesmo número
                    nova.prox = ptr.prox #adiciona-se uma nova figurinha a coleção. Em ordem: ptr -> nova -> ptr.prox
                    ptr.prox = nova
                    if nova.prox == None: #caso a figurinha seja a última
                        self.ultimo = nova #o ponteiro último aponta para ela

            elif ptr.dado.Numero == x.Numero: #caso ela seja igual à primeira figurinha
                ptr.dado.Quantidade += x.Quantidade #adiciona-se uma unidade à quantidade dela
                
            else: #caso o número da nova seja menor, adiciona-a antes da primeira, a "nova" primeira após a sentinela
                nova.prox = ptr
                self.primeiro.prox = nova

        else: #caso esteja vazia, adiciona-se a primeira figurinha após a sentinela
            self.primeiro.prox = nova

    def removeD(self, x: int):
        """Remove uma figurinha da coleção - desde que esta seja repetida"""
        if not self.vaziaD(): #se a coleção não estiver vazia
            ptr = self.primeiro.prox
            while (ptr != None) and (ptr.dado.Numero != x): #procura-se o nó de número igual ao da figurinha procurada
                ptr = ptr.prox
            
            if ptr == None: #se a figurinha não for encontrada ao fim da coleção (== None)
                return print("Você já não tem essa figurinha (;")
            
            else: #caso o nó de mesmo número seja encontrado
                if ptr.dado.Quantidade > 1: #se a figurinha for repetida (houver mais de uma unidade naquele nó)
                    ptr.dado.Quantidade -= 1 #diminui-se uma unidade ao removê-la
                
                else: #se ela for única (a única unidade naquele nó - daquele número)
                    return print("Essa figurinha não pode ser removida, você só tem uma :)")
        
        else: #se a coleção estiver vazia, não há figurinhas
            raise ValueError("Você não tem nenhuma figurinha :)")

    def string_presentes(self):
        string = '[' #início da string
        ptr = self.primeiro.prox
        while ptr != None: #enquanto não chegar ao fim da lista
            string = string + str(ptr.dado.Numero) + '; ' #adiciona somente o número da figurinha
            ptr = ptr.prox

        string += ']' #fim da string
        return string
    
    def string_repetidas(self):
        string = '[' #início da string
        ptr = self.primeiro.prox
        while ptr != None:
            if ptr.dado.Quantidade > 1: #se houver mais de uma figurinha (pelo menos uma repetida)
                string = string + str(ptr.dado.Numero) + '(' + str(ptr.dado.Quantidade - 1) + '); '
                #(quantidade - 1) retira a figurinha que completa a coleção e mantém só as restantes.
            ptr = ptr.prox
        string += ']' # fim  da string
        return string

    def busca_chave(self, x: int) -> no:
        """Busca a figurinha de número x e retorna seu nó (se estiver presente) ou None (se não estiver)"""
        ptr = self.primeiro.prox
        while (ptr != None) and (ptr.dado.Numero != x):
            ptr = ptr.prox
        return ptr

    def trocaD(self, col: coleçãoD):
        """Realiza a troca máxima de figurinhas entre duas coleções (o número mínimo de repetidas que não estão na outra)"""
        ptr1 = self.primeiro.prox
        troca1 = coleçãoD() #coleção auxilia para as figurinhas repetidas de C1 que faltam em C2
        while ptr1 != None: #até o fim da coleção
            #busca_chave verifica se a figurinha de C1 já está em C2 (!= None) ou falta (== None).
            if ptr1.dado.Quantidade > 1 and (col.busca_chave(ptr1.dado.Numero) == None):
                troca1.novafigurinhaD(ptr1.dado) #a figurinha de C1 é adicionada às trocas se o número NÃO estiver em C2
            ptr1 = ptr1.prox

        ptr2 = col.primeiro.prox
        troca2 = coleçãoD() #coleção auxiliar p/ figurinhas de C2 que NÃO estão em C1.
        while ptr2 != None:
            #busca_chave verifica se a figurinha de C2 já está em C1 (!= None) ou falta (== None).
            if ptr2.dado.Quantidade > 1 and (self.busca_chave(ptr2.dado.Numero) == None):
                troca2.novafigurinhaD(ptr2.dado) #adiciona-se as figurinhas repetidas que NÃO estão em C1.
            ptr2 = ptr2.prox 
        print("Figurinhas para troca em C1:", troca1.string_presentes())
        print("Figurinhas para troca em C2:",troca2.string_presentes())
        #TROCA:
        if (not troca1.vaziaD()) and (not troca2.vaziaD()): #se houverem figurinhas para serem trocadas
            p1 = troca1.primeiro.prox #ponteiro da coleção auxiliar C1
            p2 = troca2.primeiro.prox #ponteiro da coleção auxiliar C2
            #quando o menor entre p1 e p2 chegar ao fim de suas figurinhas, as trocas param (menor número de trocas)
            while (p1 != None) and (p2 != None):
                self.removeD(p1.dado.Numero) #tira-se uma repetida de C1
                col.novafigurinhaD(figurinhaD(p1.dado.Numero, 1)) #adiciona-a a C2 (1 unidade)
                col.removeD(p2.dado.Numero) #remove-se uma repetida de C2
                self.novafigurinhaD(figurinhaD(p2.dado.Numero, 1)) #adiciona-se a C1 (1 unidade)
                p1 = p1.prox
                p2 = p2.prox
        else:
            raise ValueError("Vocês dois não tem figurinhas para trocar entre si (;")