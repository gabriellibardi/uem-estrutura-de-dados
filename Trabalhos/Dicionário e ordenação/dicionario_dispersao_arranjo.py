from dataclasses import dataclass

# Dupla: Gabriel Libardi Lulu e Vitor da Rocha Machado
# RAs: 134728 e 132769

@dataclass
class Item:
    chave: str
    valor: int

class Dicionario:
    '''
    Uma coleção de chaves únicas associadas com valores.

    Exemplos:

    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.get('Jorge')
    25
    >>> d.get('Bia')
    40
    >>> d.get('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.get('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.get('Jorge') is None
    True
    >>> d.remove('Ana')
    >>> d.num_itens()
    1

    Testes:

    O teste a seguir cria uma lista com uma permutação dos números de 0 a 99 e
    cria um dicionário adicionando cada número (string) como chave associada
    com o próprio número.

    Em seguida, para cada número da lista o get é executado para verificar se a
    associação está correta. Depois a associação é removida e todas as outras
    associações são verificadas.

    >>> import random
    >>> lst = list(range(100))
    >>> random.shuffle(lst)
    >>> d = Dicionario()
    >>> # Faz associação
    >>> for valor in lst:
    ...     d.associa(str(valor), valor)
    >>> for i in range(len(lst)):
    ...     # Associação original
    ...     assert d.get(str(i)) == i
    ...     # Modifica a associação e verifica
    ...     d.associa(str(i), 2 * i)
    ...     assert d.get(str(i)) == 2 * i
    ...     # Remove a associação e verifica
    ...     d.remove(str(i))
    ...     assert d.get(str(i)) is None
    ...     # As associações que não foram removidas permanecem as mesmas?
    ...     for j in range(i + 1, len(lst)):
    ...         assert d.get(str(j)) == j
    '''

    tabela: list[list[Item]]
    qtd_itens: int

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.

        Exemplos:
        >>> d = Dicionario()
        >>> d.num_itens()
        0
        '''
        self.tabela = [[] for _ in range(10)]
        self.qtd_itens = 0

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.

        Exemplos:
        >>> d = Dicionario()
        >>> d.associa('vitor', 17)
        >>> d.num_itens()
        1
        >>> d.associa('gabriel', 15)
        >>> d.associa('fratus', 25)
        >>> d.num_itens()
        3
        '''
        return self.qtd_itens

    def associa(self, chave: str, valor: int) -> None:
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.

        Exemplos:
        >>> d = Dicionario()
        >>> d.associa('vitor', 17)
        >>> d.get('vitor')
        17
        >>> d.associa('vitor', 20)
        >>> d.get('vitor')
        20
        '''
        indice = hash(chave) % len(self.tabela)
        presente = False
        i = 0
        while not presente and i < len(self.tabela[indice]):
            if self.tabela[indice][i].chave == chave:
                self.tabela[indice][i].valor = valor
                presente = True
            i += 1
        if not presente:
            self.tabela[indice].append(Item(chave, valor))
            self.qtd_itens += 1
        
        if self.qtd_itens > 50 and self.qtd_itens / len(self.tabela) > 10:
            self._redispersao([[] for _ in range(len(self.tabela) * 2)])

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        
        Exemplos:
        >>> d = Dicionario()
        >>> d.associa('vitor', 17)
        >>> d.get('vitor')
        17
        >>> d.get('julia') # None
        '''
        indice = hash(chave) % len(self.tabela)
        for elem in self.tabela[indice]:
            if elem.chave == chave:
                return elem.valor
        return None

    def remove(self, chave: str) -> None:
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.

        >>> d = Dicionario()
        >>> d.associa('vitor', 17)
        >>> d.associa('gabriel', 15)
        >>> d.num_itens()
        2
        >>> d.remove('vitor')
        >>> d.num_itens()
        1
        >>> d.remove('julia')
        >>> d.num_itens()
        1
        '''
        indice = hash(chave) % len(self.tabela)
        if len(self.tabela[indice]) > 0:
            presente = False
            i = 0
            while not presente and i < len(self.tabela[indice]):
                if self.tabela[indice][i].chave == chave:
                    presente = True
                i += 1
            if presente:
                self.tabela[indice].pop(i - 1)
                self.qtd_itens -= 1
        
        if self.qtd_itens > 50 and self.qtd_itens / len(self.tabela) < 5:
            self._redispersao([[] for _ in range(len(self.tabela)//2)])
    
    def _redispersao(self, tabela: list[list[Item]]) -> None:
        '''
        Faz a redispersão dos elementos de um dicionário em *tabela*.

        Testes:

        Como são testes, os valores internos acerca da implementação são acessados, para
        facilitar o processo, já que essa função não é utilizada pelo usuário.

        >>> d = Dicionario()
        >>> len(d.tabela)
        10
        >>> for n in range(101):
        ...     d.associa(str(n), n)
        >>> len(d.tabela)
        20
        >>> for n in range(101):
        ...     d.remove(str(n))
        >>> len(d.tabela)
        10
        '''
        for lista in self.tabela:
            for par in lista:
                novo_indice = hash(par.chave)%len(tabela)
                tabela[novo_indice].append(par)
        self.tabela = tabela
