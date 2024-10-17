from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class figurinhaE:
    Numero: int
    Quantidade: int

class colecaoE:
    def __init__(self, total: int):
        self.tam = 0
        self.tam_max = total
        self.elementos: list[figurinhaE | None] = [None] * self.tam_max

    def vaziaE(self):
        "Verifica se há figurinhas na coleção"
        return self.tam == 0
    
    def cheiaE(self):
        "Verifica se a coleção já está completa"
        return self.tam == self.tam_max

    def inserefigurinhaE(self, x: figurinhaE):
        """Insere uma nova figurinha x à coleção. Tipo FigurinhaE, pois, ao abrir um pacote novo, podemos receber figurinhas repetidas"""
        if self.vaziaE() == False: #se não for a primeira figurinha
            i = 0
            while (self.elementos[i] != None) and (self.elementos[i].Numero < x.Numero):  #enquanto não acabar a coleção e os números forem menores que a nova
                i += 1
            
            if (self.elementos[i] != None) and (self.elementos[i].Numero == x.Numero): #verifica se o loop parou porque a figurinha já está na coleção (repetida) 
                self.elementos[i].Quantidade += x.Quantidade #Soma-se à quantidade - não aumenta o tamanho da lista
            
            #Caso o loop pare porque não foi encontrada uma figurinha maior que a nova (== None), a nova figurinha será a última da coleção (i == self.tam)

            else: #desloca as figurinhas maiores que x abrindo o espaço para ela onde a primeira figurinha maior que ela estava (i de interrupção do loop).
                for t in range(self.tam, i, -1):
                    self.elementos[t] = self.elementos[t - 1]
                self.elementos[i] = deepcopy(x) #adiciona a nova no espaço i
                self.tam += 1  #aumenta o tamanho da lista, pois uma nova figurinha foi adicionada
        
        elif self.cheiaE():
            return print("Sua coleção já está completa :)! Essa figurinha não faz parte das colecionaveis :|")

        else: #adiciona a primeira figurinha na posição 0 - lista vazia
            self.elementos[self.tam] = deepcopy(x)
            self.tam += 1

    def removeE(self, x: int):
        """Remove uma figurinha de número x da coleção. Tipo int, pois queremos remover apenas uma figurinha (para trocar por exemplo)"""
        if not self.vaziaE(): #Se não estiver vazia.
            i = 0
            while (self.elementos[i] != None) and (self.elementos[i].Numero != x): #procura a figurinha de número x na coleção
                i += 1

            if i == self.tam: #Caso i seja igual ao tamanho, o loop foi interrompido porque a figurinha não foi encontrada (== None)
                return print("Você não tem essa figurinha (;")
            
            else:
                if self.elementos[i].Quantidade > 1: #Caso haja mais de uma única figurinha de número x (seja repetida)
                    self.elementos[i].Quantidade -= 1 #Remove-se uma figurinha repetida da quantidade
                
                else: #Caso haja apenas uma figurinha x, o colecionador é avisado para não retirá-la
                    return print("Você tem apenas uma figurinha", x, "na sua coleção")
        
        else: #Caso a coleção esteja vazia
            return print("Você não tem figurinhas :)")
    
    def string_presentesE(self):
        """Retorna uma lista com todas as figurinhas da coleção - em string"""
        string = "["
        for i in range(self.tam): #percorre a coleção
            if self.elementos[i].Quantidade != 0:
                string += str(self.elementos[i].Numero) + "; " #adiciona todas as figurinhas (os números) presentes à string
        string += "]"
        return string
    
    def string_repetidasE(self):
        """Retorna uma lista com as figurinhas repetidas da coleção e quantas são - em string"""
        string = "["
        for i in range(self.tam): #percorre todas as figurinhas
            if self.elementos[i].Quantidade > 1: #Se houver mais de uma figurinha, ou seja, se houver repetidas
                string += str(self.elementos[i].Numero) + " (" + str(self.elementos[i].Quantidade - 1) + "); "
                #A figurinha e o número de repetidas (quantidade - 1) são adicionadas à string
        string += "]"
        return string

    def busca(self, x: int) -> int:
        """Busca uma figurinha de número x e retorna sua posição i"""
        for i in range(self.tam):
            if self.elementos[i].Numero == x:
                return i
        return -1
        
    def trocaE(self, col: colecaoE):
        """realiza a troca de figurinhas entre duas coleções"""
        troca1 = colecaoE(self.tam) #Criação de duas listas auxiliares para as figurinhas que podem ser trocadas
        troca2 = colecaoE(col.tam) #figurinhas repetidas e que não estão presentes na outra coleção
        i = 0
        for i in range(self.tam): #percorre toda a coleção C1
            if (self.elementos[i].Quantidade > 1) and (col.busca(self.elementos[i].Numero) == -1):
            #se a figurinha for repetida em C1 (qtd > 1) e não estiver em C2 (busca == -1)
                troca1.inserefigurinhaE(self.elementos[i]) #adiciona-se nas possibilidades de troca de C1
        j = 0
        for j in range(col.tam): #percorre a coleção C2
            if (col.elementos[j].Quantidade > 1) and (self.busca(col.elementos[j].Numero) == -1):
            #se a figurinha for repetida em C2 (qtd > 1) e não estiver em C1 (busca == -1)
                troca2.inserefigurinhaE(col.elementos[j]) #adiciona-se nas trocas de C2
        
        print("Figurinhas para troca em C1:", troca1.string_presentesE())
        print("Figurinhas para troca em C2:", troca2.string_presentesE())
        #TROCA:
        if (not troca1.vaziaE()) and (not troca2.vaziaE()):
            t = 0 #contador para as possibilidades de troca (o "menor número possivel" determina as trocas)
            while (t != troca1.tam) and (t != troca2.tam):
                #enquanto t for diferente do "fim" das duas possibilidades de troca de C1 e C2
                self.inserefigurinhaE(figurinhaE(troca2.elementos[t].Numero, 1)) #adiciona-se em C1 uma figurinha de troca de C2
                col.removeE(troca2.elementos[t].Numero) #retira-se de C2 uma unidade repetida da mesma figurinha trocada
                col.inserefigurinhaE(figurinhaE(troca1.elementos[t].Numero, 1)) #adiciona-se em C2 uma figurinha de troca de C1
                self.removeE(troca1.elementos[t].Numero) #retira-se de C1 uma unidade repetid da mesma figurinha  trocada
                t += 1
        else:
            raise ValueError("Vocês dois não tem figurinhas para trocar entre si (;")