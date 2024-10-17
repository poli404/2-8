#MONITORAMENTO DE NÍVEIS DE ESTOQUES:

from enum import Enum,auto
from dataclasses import dataclass
class TipoProduto(Enum):
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()
@dataclass
class Pedido:
    produto: TipoProduto
    quantidade: int
@dataclass
class Totalização:
    Bobina: int
    Chapa: int
    Painel: int

#DEFINIÇÃO DOS DADOS: uma lista de pedidos a serem "somados"/totalizados.
def totaliza_pedidos(pedidos: list[Pedido]) -> Totalização:
    '''Produz uma estrutura que totaliza a demanda de cada produto a partir de uma lista de pedidos.
    Exemplo:
    >>> totaliza_pedidos([Pedido('BOBINA', 100), Pedido('CHAPA', 50), Pedido('BOBINA', 30), Pedido('PAINEL', 20), Pedido('CHAPA', 15)])
    Totalização(Bobina=130, Chapa=65, Painel=20)
    >>> totaliza_pedidos([Pedido('CHAPA', 7), Pedido('CHAPA', 74), Pedido('BOBINA', 150), Pedido('PAINEL', 5), Pedido('PAINEL', 80)])
    Totalização(Bobina=150, Chapa=81, Painel=85)
    '''
    qtdB = 0
    qtdC = 0
    qtdP = 0
    i = 0
    for pedidos[i] in pedidos:
        if pedidos[i].produto == (TipoProduto.BOBINA).name:
            qtdB += pedidos[i].quantidade
        elif pedidos[i].produto == (TipoProduto.CHAPA).name:
            qtdC += pedidos[i].quantidade
        else:
            qtdP += pedidos[i].quantidade
    
    Total = Totalização(qtdB, qtdC, qtdP)

    return Total

#DEFINIÇÃO DOS DADOS: Recebe o total de produtos de cada tipo disponíveis no estoque da loja e o total de produtos demandados em determinada venda.
def ha_ruptura(estoque: Totalização, demanda: Totalização) -> list[TipoProduto]:
    '''Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos com ruptura do estoque (em que a demanda é maior que a disponibilidade em estoque).
    Exemplos:
    >>> ha_ruptura(Totalização(Bobina=100, Chapa=70, Painel=21), Totalização(Bobina=130, Chapa=65, Painel=20))
    ['BOBINA']
    >>> ha_ruptura(Totalização(Bobina=100, Chapa=70, Painel=10), Totalização(Bobina=130, Chapa=65, Painel=20))
    ['BOBINA', 'PAINEL']
    >>> ha_ruptura(Totalização(Bobina=130, Chapa=10, Painel=15), Totalização(Bobina=130, Chapa=65, Painel=20))
    ['CHAPA', 'PAINEL']
    >>> ha_ruptura(Totalização(Bobina=150, Chapa=70, Painel=21), Totalização(Bobina=130, Chapa=65, Painel=20))
    []
    '''
    lista = []
    if estoque.Bobina < demanda.Bobina:
        lista.append((TipoProduto.BOBINA).name)
    if estoque.Chapa < demanda.Chapa:
        lista.append((TipoProduto.CHAPA).name)
    if estoque.Painel < demanda.Painel:
        lista.append((TipoProduto.PAINEL).name)
    return lista

#------------------------------------------------- RELATÓRIOS DE VENDAS ---------------------------------------------------

@dataclass
class NotaDeVenda:
    Vendedor: str
    Pedido: Pedido #Inclui produto e quantidade.
    Valor: float

#ANÁLISE: A partir de um relatório de vendas, calcular o lucro líquido obtido e a receita total desse.
#DEFINIÇÃO DOS DADOS: Um relatório de vendas - uma lista das diferentes notas de venda.
def relatório(Notas: list[NotaDeVenda]) -> float:
    '''Determina a receita e o lucro líquido a partir do relatório de vendas.
    Exemplos:
    >>> relatório([NotaDeVenda('VEND1', Pedido('BOBINA', 100), 55.5), NotaDeVenda('VEND2', Pedido('CHAPA', 50), 45.5), NotaDeVenda('VEND3', Pedido('BOBINA', 30), 59.9), NotaDeVenda('VEND1', Pedido('CHAPA', 15), 48.0), NotaDeVenda('VEND2', Pedido('PAINEL', 20), 80.0)])
    A receita é de R$ 11942.0
    O lucro líquido é de R$ 1342.0
    >>> relatório([NotaDeVenda('VEND2', Pedido('BOBINA', 100), 55.5), NotaDeVenda('VEND3', Pedido('CHAPA', 50), 45.5), NotaDeVenda('VEND4', Pedido('PAINEL', 20), 80.0)])
    A receita é de R$ 9425.0
    O lucro líquido é de R$ 925.0
    >>> relatório([NotaDeVenda('VEND4', Pedido('CHAPA', 50), 45.5), NotaDeVenda('VEND1', Pedido('PAINEL', 35), 82.0)])
    A receita é de R$ 5145.0
    O lucro líquido é de R$ 520.0
    '''
    i = 0
    LucroB = 0
    LucroC = 0
    LucroP = 0
    receita = 0
    for Notas[i] in Notas:
        if Notas[i].Pedido.produto == TipoProduto.BOBINA.name:
            LucroB = LucroB + (Notas[i].Valor * Notas[i].Pedido.quantidade) - (50 * Notas[i].Pedido.quantidade)
        elif Notas[i].Pedido.produto == TipoProduto.CHAPA.name:
            LucroC = LucroC + (Notas[i].Valor * Notas[i].Pedido.quantidade) - (40 * Notas[i].Pedido.quantidade)
        else: #Notas[i].Pedido.produto == TipoProduto.PAINEL.name:
            LucroP = LucroP + (Notas[i].Valor * Notas[i].Pedido.quantidade) - (75 * Notas[i].Pedido.quantidade)
        
        receita += (Notas[i].Valor * Notas[i].Pedido.quantidade)
    lucro = LucroB + LucroC + LucroP
    
    print("A receita é de R$", receita)
    print("O lucro líquido é de R$", lucro)

#ANÁLISE: Determina o lucro individual de cada vendedor (essa função e a função melhores são corelacionadas. Esta é utilizada a partir da retirada de uma lista dos vendedores presentes no relatório de vendas montada em melhores).
#DEFINIÇÃO DOS DADOS: o relatório de vendas (já utilizado anteriormente) e a denominção de um vendedor.
def lucro_vendedor(Notas: list[NotaDeVenda], vendedor: str) -> float:
    '''Calcula o lucro de um determinado vendedor baseado no relatório de notas de venda.
    Exemplos:
    >>> lucro_vendedor([NotaDeVenda('VEND1', Pedido('BOBINA', 100), 55.5), NotaDeVenda('VEND4', Pedido('CHAPA', 50), 45.5), NotaDeVenda('VEND3', Pedido('BOBINA', 30), 59.9), NotaDeVenda('VEND1', Pedido('CHAPA', 15), 48.0), NotaDeVenda('VEND2', Pedido('PAINEL', 20), 80.0)], 'VEND2')
    1600.0
    >>> lucro_vendedor([NotaDeVenda('VEND1', Pedido('BOBINA', 100), 55.5), NotaDeVenda('VEND4', Pedido('CHAPA', 50), 45.5), NotaDeVenda('VEND3', Pedido('BOBINA', 30), 59.9), NotaDeVenda('VEND1', Pedido('CHAPA', 15), 48.0), NotaDeVenda('VEND2', Pedido('PAINEL', 20), 80.0)], 'VEND1')
    6270.0
    '''
    i = 0
    lucro = 0
    for Notas[i] in Notas:
        if Notas[i].Vendedor == vendedor:
            lucro += (Notas[i].Pedido.quantidade * Notas[i].Valor)
    return lucro

#ANÁLISE: Determinar os três melhores vendedores a partir de seus lucros em um relatório de vendas.
#DEFINIÇÃO DOS DADOS: o relatório de vendas (já utilizado anteriormente).
def melhores(Notas: list[NotaDeVenda]) -> list:
    '''Determina os três melhores vendedores a partir de um relatório de notas
    Exemplo:
    >>> melhores([NotaDeVenda('VEND1', Pedido('BOBINA', 100), 55.5), NotaDeVenda('VEND4', Pedido('CHAPA', 50), 45.5), NotaDeVenda('VEND3', Pedido('BOBINA', 30), 59.9), NotaDeVenda('VEND1', Pedido('CHAPA', 15), 48.0), NotaDeVenda('VEND2', Pedido('PAINEL', 20), 80.0)])
    Os três vendedores que mais apresentaram lucros no relatório foram: ['VEND1', 'VEND4', 'VEND3']
    >>> melhores([NotaDeVenda('VEND4', Pedido('BOBINA', 100), 50.0), NotaDeVenda('VEND1', Pedido('CHAPA', 10), 50.0), NotaDeVenda('VEND3', Pedido('BOBINA', 40), 55.0), NotaDeVenda('VEND2', Pedido('PAINEL', 15), 78.0), NotaDeVenda('VEND4', Pedido('CHAPA', 100), 48.0)])
    Os três vendedores que mais apresentaram lucros no relatório foram: ['VEND4', 'VEND3', 'VEND2']
    >>> melhores([NotaDeVenda('VEND2', Pedido('CHAPA', 20), 47.0), NotaDeVenda('VEND5', Pedido('BOBINA', 30), 55.0), NotaDeVenda('VEND3', Pedido('CHAPA', 15), 48.0), NotaDeVenda('VEND1', Pedido('PAINEL', 30), 90.0), NotaDeVenda('VEND4', Pedido('BOBINA', 20), 60.0)])
    Os três vendedores que mais apresentaram lucros no relatório foram: ['VEND1', 'VEND5', 'VEND4']
    '''
    i = 0
    vendedores = []
    lucros = []
    for i in range(len(Notas)): #Cria uma lista 'vendedores' com todos os vendedores presentes no relatório inserido.
        if Notas[i].Vendedor not in vendedores:
            vendedores.append(Notas[i].Vendedor)
    
    i = 0
    for i in range(len(vendedores)): #cria uma lista 'lucros' com os lucros totais de cada vendedor a partir da função externa lucro_vendedor. Os lucros na lista compartilham mesmo índice que seus respectivos vendedores na lista de vendedores.
        resp = lucro_vendedor(Notas, vendedores[i])
        lucros.append(resp)

    i = 0
    for i in range(len(lucros)): #Ordena a lista de lucros e a lista de vendedores, de forma que os correspondentes vendedor-lucro_do_vendedor permaneçam com o mesmo índice.
        for i in range(len(vendedores)):
            if lucros[i] > lucros[(i - 1)]:
                lucros.insert(0, lucros[i]) # Após a comparação, ordena a lista de lucros de cada vendedor
                lucros.pop((i + 1))
                vendedores.insert(0, vendedores[i]) # Ordena, conjuntamente à lista de lucros, a lista de vendedores. Mantendo a corresponência.
                vendedores.pop((i + 1))
    
    print("Os três vendedores que mais apresentaram lucros no relatório foram:", vendedores[0:3])