from ed import array

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(50)
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    valores: array[str]
    # O índice do elemento que está no topo da pilha
    topo: int
    # A capacidade máxima de valores que a pilha armazena
    capacidade: int

    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.valores = array(capacidade, '')
        self.topo = -1

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos
        na pilha seja menor que MAX_TAM.
        '''
        assert self.topo < self.capacidade - 1
        self.topo = self.topo + 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha(100)
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'
        '''
        assert not self.vazia()
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha(20)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1

    def cheia(self) -> bool:
        '''
        Devolve True se a pilha está cheia, False caso contrário.

        Exemplos
        >>> p = Pilha(100)
        >>> p.cheia()
        False
        >>> p.empilha('coelho')
        >>> p.cheia()
        False
        >>> for i in range(p.capacidade - 1):
        ...    p.empilha('lebre')
        >>> p.cheia()
        True
        '''
        return self.topo == self.capacidade - 1