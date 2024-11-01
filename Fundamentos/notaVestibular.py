#NOTA DO VESTIBULAR;

from dataclasses import dataclass
@dataclass
class Prova:
    código_candidato: str
    nota_redação: float
    respostas: list[int]
@dataclass
class Resultado:
    Código: str
    Nota: float

def somatorio_alternativas(s: int) -> list[int]:
    '''Calcula a lista de alternativas que somadas gera o somátorio *s*. Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16. Requer que *s* esteja no entre 0 e 31.
    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''
    alternativas = []
    alternativa = 1
    while s > 0:
    # verifica se alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
    # divide todas as alternativas que compõe
    # o somatório s por 2
        s = s // 2
    # procura a próxima alternativa
        alternativa = alternativa * 2
    return alternativas

#DEFINIÇÃO DOS DADOS: Recebe uma lista de somatórias - uma lista de números inteiros que representam as somas das alternativas de cada questão.
def alternativas(Somatorias: list[int]) -> list[list]:
    '''Transforma todas as somatórias da lista de resposta do candidato em uma lista de alternativas marcadas - modificando a lista passada por parâmetro.
    >>> alternativas([4, 10, 16, 5, 10])
    [[4], [2, 8], [16], [1, 4], [2, 8]]
    >>> alternativas([20, 0, 8, 26, 1])
    [[4, 16], [], [8], [2, 8, 16], [1]]
    '''
    i = 0
    while i != len(Somatorias): #Enquanto não percorrer toda a lista, continua.
        Somatorias[i] = somatorio_alternativas(Somatorias[i]) #transforma cada elemento i (soma) em seu equivalente de alternativas usando a função somatorio_alternativas.
        i += 1
    return Somatorias

#DEFINIÇÃO DOS DADOS: Recebe as informações ligadas a um candidato (tipo Prova) de modo a acessar sua nota de redação.
def possivel(Candidato: Prova) -> bool:
    '''Determina se um candidato pode ser avaliado ou não a partir de sua redação
    >>> possivel(Prova('19023', 65, [4, 10, 16, 5, 10]))
    True
    >>> possivel(Prova('19563', 0, [4, 10, 3, 5, 8]))
    False
    '''
    if Candidato.nota_redação == 0:
        return False
    else:
        return True

#DEFINIÇÃO DOS DADOS: Recebe uma lista de alternativas marcadas pelo candidato e uma lista de alternativas corretas (números inteiros)
def correção(Marcadas: list[int], Corretas: list[int]) -> int:
    '''Determina o número de alternativas corretas marcadas na questão em relação ao gabarito desta - o número de acertos.
    >>> correção([4], [1, 4, 16])
    1
    >>> correção([16], [2, 8])
    0
    >>> correção([16], [16])
    1
    >>> correção([2, 8], [1, 2, 4, 8])
    2
    >>> correção([1, 16], [2, 8, 16])
    0
    '''
    if len(Marcadas) == 0 or len(Corretas) == 0:
        return 0
    else: #Para múltiplas alternativas corretas e marcadas, deve-se comparar uma a uma até encontrar uma correspondência.
        if Marcadas[0] == Corretas[0]: #Se as primeiras alterrnativas marcada e correta forem iguais, passa-se a comprar as segundas alternativas entre si.
            return correção(Marcadas[1:], Corretas[1:]) + 1
        else: #Se a primeira alternativa marcada for diferente da primeira correta, deve-se comprar aquela mesma marcada a segunda correta. Assim, sucessivamente até encontrar uma correspondência.
            return correção(Marcadas, Corretas[1:]) #Caso a primeira alternativa marcada não faça parte das corretas, a questão será automaticamente zerada.
    
#DEFINIÇÃO DOS DADOS: Recebe uma lista de respostas marcadas em cada questão e uma lista de gabaritos para cada questão (cada questão corresponde a uma lista de alternativas - uma lista de listas.)
def pontuação(Respostas: list[list], Gabarito: list[list]) -> float:
    '''Calcula a pontuação atingida por um candidato na soma de todas as questões.
    >>> pontuação([[4], [2, 8], [16], [1, 4], [2, 8]], [[1, 4, 16], [2, 8], [8], [16], [1, 2, 4, 8]])
    11.0
    >>> pontuação([[1, 4, 16], [8], [8], [8], [2, 4, 8]], [[1, 4, 16], [2, 8], [8], [16], [1, 2, 4, 8]])
    19.5
    >>> pontuação([[1, 2, 4, 8], [8], [8], [2, 4, 8]], [[1, 4, 16], [2, 8], [8], [1, 2, 4, 8]])
    13.5
    >>> pontuação([[16], [1, 4], [], [1, 4], [2]], [[1, 2, 4, 16], [1, 2, 4], [], [4, 8], [2, 16]])
    14.5
    >>> pontuação([[1, 2], [4, 8], [16]], [[1, 2], [], [2, 16]])
    9.0
    '''
    total = 0
    for i in range(len(Gabarito)) and range(len(Respostas)):
        #Contagem de acertos por questão
        if len(Respostas[i]) > len(Gabarito[i]): #Caso o candidato tenha marcado um número de alternativas maior que o número de alternativas corretas, a questão é automaticamente zerada.
            acertos = 0
        else:
            acertos = correção(Respostas[i], Gabarito[i]) #Determina o número de alternativas corretas marcadas.
        
        #Soma da nota final das questões
        if len(Respostas[i]) == len(Gabarito[i]) == 0: #Se a resposta correta for 0 e o candidato não tiver marcado nenhuma alternativa (0), ele recebe a questão cheia.
            total += 6.0
        elif len(Respostas[i]) != 0 and len(Gabarito[i]) == 0: #Se o gabarito for 0 e o candidato marcar qualquer alternativa, a questão é zerada.
            total += 0.0
        else:
            total = total + ((6 / len(Gabarito[i])) * acertos) #Determina o valor de cada alternativa da questão e multiplica pelo número de corretas

    return total

#DEFINIÇÃO DOS DADOS: Recebe uma lista não ordenada de resultados individuais para cada candidato (tipo Resultado).
def ordem(Final: list[Resultado]) -> list[Resultado]:
    '''Ordena de acordo com a maior e a menor nota 
    >>> ordem([Resultado(Código='3211', Nota=97.0), Resultado(Código='5812', Nota=49.5), Resultado(Código='1234', Nota=109.5)])
    [Resultado(Código='1234', Nota=109.5), Resultado(Código='3211', Nota=97.0), Resultado(Código='5812', Nota=49.5)]
    >>> ordem([Resultado(Código='1234', Nota=120.0), Resultado(Código='5678', Nota=2.5), Resultado(Código='0910', Nota=109.5), Resultado(Código='1112', Nota=9.5), Resultado(Código='1314', Nota=102.2)])
    [Resultado(Código='1234', Nota=120.0), Resultado(Código='0910', Nota=109.5), Resultado(Código='1314', Nota=102.2), Resultado(Código='1112', Nota=9.5), Resultado(Código='5678', Nota=2.5)]
    '''
    i, j = 0, 0
    for i in range(len(Final)): #pega o elemento de índice 0 (i) na lista
        for j in range(i + 1, len(Final)): #pega o elemento de índice 1 (i + 1) na lista - o sucessor do elemento i.
            if Final[j].Nota > Final[i].Nota: #compara se o elemento sucessor é maior que o antecessor.
                Final[i], Final[j] = Final[j], Final[i] #Se sim, troca-os de posição dois a dois.
    
    return Final

#DEFINIÇÃO DOS DADOS: Recebe uma lista de candidatos do vestibular (tipo Prova) e o gabarito das questões do vestibular (em forma de soma).
def final(Concorrentes: list[Prova], Somas: list[list]) -> list[Resultado]:
    '''Determina o desempenho e a classificação final de uma lista de concorrentes - listando-os do primeiro ao último colocado por nota.
    >>> final([Prova('3211', 80, [4, 10, 4, 16, 10]), Prova('7102', 0, [1, 2, 3, 4, 5]), Prova('1234', 90, [21, 8, 8, 8, 14]), Prova('5812', 32, [20, 0, 8, 16, 1]), Prova('9132', 0, [5, 4, 3, 2, 1])], [21, 10, 8, 16, 15])
    [Resultado(Código='1234', Nota=109.5), Resultado(Código='3211', Nota=97.0), Resultado(Código='5812', Nota=49.5)]
    '''
    resultado = []
    gabarito = alternativas(Somas) #Transforma cada somatória que compõe o gabarito (lista) em uma lista de alternativas individuais. 

    for i in range(len(Concorrentes)):
        if possivel(Concorrentes[i]) == True: #a função possivel infere se o Concorrente não zerou a redação antes de passá-lo para a próxima fase (Cálculo dos pontos). Caso tenha zerado, é imediatamente excluído.
            pontos = pontuação(alternativas(Concorrentes[i].respostas), gabarito) + Concorrentes[i].nota_redação #Cálculo dos pontos do Concorrente[i]
            #A função alternativas transforma a lista de somatorias (.respostas do Concorrente[i]) em uma lista de alternativas.
            #A lista de alternativas gerada é usada juntamente com o gabarito (já transformado) na função pontuação - que determina a nota do concorrente nas questões.
            #Por fim, soma-se o resultado das questões a nota tirada na redação de modo a formar a pontuação final do candidato.
            resultado.append(Resultado(Concorrentes[i].código_candidato, pontos))
    
    resultado_final = ordem(resultado) #Ordena a lista de concorrentes de forma que o de maior pontuação tenha índice 0 (seja o primeiro da lista). 

    return resultado_final
