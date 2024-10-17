from __future__ import annotations

#DEFINIÇÃO DA CLASSE TabelHash:
class TabelaHash:
    def __init__(self, tam_max: int):
        self.tam_max = tam_max
        self.elementos = [None] * self.tam_max
    
    def hash(self, chave: int) -> int:
        '''Define o endereço h = chave % n (n é o tamanho da tabela)'''
        return chave % self.tam_max
    
    def __EndereçamentoAberto__(self, h: int) -> int:
        '''Método de Endereçamento Aberto -> Procura a próxima posição vazia para colocar o elemento'''
        endereço = h
        while (endereço != self.tam_max - 1) and (self.elementos[endereço] != None): #enquanto a posição não for vazia e não chegarmos ao fim da tabela
            endereço += 1 #vamos para a próxima posição.
        if self.elementos[-1] != None: #caso a tabela acabe e nenhuma posição vazia seja encontrada (nem a última).
            endereço = 0 #reiniciamos a busca agora do INÍCIO da tabela.
            while (self.elementos[endereço] != None) and (endereço != h): #procura-se uma posição vazia ou voltar ao índice inicial.
                endereço += 1
            if endereço == h: #caso o índice retorne ao h inicial.
                raise ValueError("Tabela Hash Cheia") #a tabela está cheia e não há como adicionar novos elementos
        return endereço

    def inserir(self, chave: int, x):
        '''Coloca um novo elemento na tabela'''
        h = self.hash(chave) #acha o endereço para inserção daquela chave
        if self.elementos[h] == None: #se não houver nenhum elemento naquele endereço
            self.elementos[h] = x #coloca o novo
        else: #se já houver um elemento aquele endereço, há uma colisão.
            h = self.__EndereçamentoAberto__(h) #transforma em um novo endereço pelo método do endereçamento aberto
            self.elementos[h] = x #coloca o elemento no novo endereço definido (próximo disponível)
    
    def retirar(self, chave: int):
        '''Remove o elemento x da tabela'''
        h = self.hash(chave)
        self.elementos[h] = None #deixa a posição do elemento vazia.

#TESTANDO A TABELA HASH COM ENCADEAMENTO ABERTO PARA COLISÕES:

def entradas():
    tabelaSC = TabelaHash(10)
    tabelaSC.inserir(230, 'Ameixa') # h = 0
    tabelaSC.inserir(23, 'Goiaba') # h = 3
    tabelaSC.inserir(52, 'Banana') # h = 2
    tabelaSC.inserir(67, 'Morango') # h = 7
    print("Tabela Sem Colisões:", tabelaSC.elementos)
entradas()

def entradas():
    tabelaCC = TabelaHash(7)
    tabelaCC.inserir(28, 'Praia') #h = 4
    tabelaCC.inserir(25, 'Areia') #h = 3
    tabelaCC.inserir(66, 'Ondas') #h = 3 -> Colisão: Pelo endereçamento aberto, procura a próxima vazia (h = 6).
    print("Após colisão em h = 5:", tabelaCC.elementos)
entradas()

def entradas():
    tabelaCheia = TabelaHash(4)
    tabelaCheia.inserir(775, 4) # h = 3
    tabelaCheia.inserir(6, 3) # h = 2
    tabelaCheia.inserir(18, 1) # h = 2 -> Colisão: busca a próxima vazia (h = 0)
    tabelaCheia.inserir(37, 2) # h = 1
    print("Tabela Cheia:", tabelaCheia.elementos)
    tabelaCheia.inserir(20, 5) #tabela já cheia
entradas()