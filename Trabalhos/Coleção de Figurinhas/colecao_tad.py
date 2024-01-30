class Colecao:
    '''
    Uma coleção de figurinhas ordenadas representadas por números inteiros.

    Exemplos
    >>> c = Colecao()
    >>> c.str_possuidas()
    []
    >>> c.str_repetidas()
    []
    >>> c.insercao(23)
    >>> c.insercao(48)
    >>> c.insercao(15)
    >>> c.str_possuidas()
    [15, 23, 48]
    >>> c.str_repetidas()
    []
    >>> c.insercao(23)
    >>> c.str_repetidas()
    [23 (1)]
    >>> c.insercao(24)
    >>> c.insercao(24)
    >>> c.insercao(24)
    >>> c.insercao(15)
    >>> c.insercao(48)
    >>> c.remocao(23)
    >>> c.str_possuidas()
    [15, 24, 48]    
    >>> c.str_repetidas()
    [15 (1), 24 (2), 48 (1)]

    >>> d = Colecao()
    >>> d.insecao(13)
    >>> d.insecao(13)
    >>> d.insecao(19)
    >>> d.insecao(19)
    >>> d.str_possuidas()
    [13, 19]    
    >>> d.str_repetidas()
    [13 (1), 19 (1)]


    >>> troca_maxima(c, d)
    >>> c.str_possuidas()
    [13, 15, 19, 24, 48]    
    >>> c.str_repetidas()
    [24 (1), 48 (1)]
    >>> d.str_possuidas()
    [13, 15, 19, 24]    
    >>> c.str_repetidas()
    []
    '''
    def __init__(self, quantidade_total: int):
        '''
        Cria uma coleção de figurinhas com a *quantidade_total*
        de figurinhas do álbum.

        Requer *quantidade_total* > 0
        '''
        raise NotImplemented
    
    def insercao(self, figurinha: int):
        '''
        Insere a *figurinha* na coleção.

        Requer que 1 <= *figurinha* <= quantidade_total
        '''
        raise NotImplemented

    def remocao(self, figurinha: int):
        '''
        Remove a *figurinha* da coleção.

        Requer que *figurinha* faça parte da coleção.

        '''
        raise NotImplemented

    def str_possuidas(self) -> str:
        '''
        Gera uma representação em string das figurinhas presentes na coleção,
        sem considerar repetições.
        '''
        raise NotImplemented

    def str_repetidas(self) -> str:
        '''
        Gera uma representação em string das figurinhas repetidas da coleção,
        indicando a quantidade de repetições.
        '''
        raise NotImplemented

def troca_maxima(a: Colecao, b: Colecao):
    '''
    Realiza uma troca entre as coleções *a* e *b*, trocando o máximo de
    figurinhas repetidas possíveis entre as coleções.
    As figurinhas trocadas são escolhidas por ordem.
    '''
    raise NotImplemented