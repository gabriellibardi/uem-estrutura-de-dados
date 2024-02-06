from __future__ import annotations

class Colecao:
    '''
    Uma coleção de figurinhas ordenadas representadas por números inteiros.

    Exemplos:
    >>> c = Colecao(100)
    >>> c.str_possuidas()
    '[]'
    >>> c.str_repetidas()
    '[]'
    >>> c.insere(23)
    >>> c.insere(48)
    >>> c.insere(15)
    >>> c.str_possuidas()
    '[15, 23, 48]'
    >>> c.str_repetidas()
    '[]'
    >>> c.insere(23)
    >>> c.str_repetidas()
    '[23 (1)]'
    >>> c.insere(24)
    >>> c.insere(24)
    >>> c.insere(24)
    >>> c.insere(15)
    >>> c.insere(48)
    >>> c.remove(23)
    >>> c.remove(23)
    >>> c.str_possuidas()
    '[15, 24, 48]'
    >>> c.str_repetidas()
    '[15 (1), 24 (2), 48 (1)]'

    >>> d = Colecao(100)
    >>> d.insere(13)
    >>> d.insere(13)
    >>> d.insere(19)
    >>> d.insere(19)
    >>> d.str_possuidas()
    '[13, 19]'    
    >>> d.str_repetidas()
    '[13 (1), 19 (1)]'

    >>> c.troca_maxima(d)
    >>> c.str_possuidas()
    '[13, 15, 19, 24, 48]'    
    >>> c.str_repetidas()
    '[24 (1), 48 (1)]'
    >>> d.str_possuidas()
    '[13, 15, 19, 24]'    
    >>> c.str_repetidas()
    '[]'
    '''
    def __init__(self, quantidade_total: int):
        '''
        Cria uma coleção de figurinhas com a *quantidade_total*
        de figurinhas do álbum.

        Requer *quantidade_total* > 0
        '''
        raise NotImplemented
    
    def insere(self, figurinha: int):
        '''
        Insere a *figurinha* na coleção.

        Requer que 1 <= *figurinha* <= tamanho da coleção
        '''
        raise NotImplemented

    def remove(self, figurinha: int):
        '''
        Remove a *figurinha* da coleção.

        Requer que 1 <= *figurinha* <= tamanho da coleção
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

    def troca_maxima(self, colecao: Colecao):
        '''
        Realiza uma troca entre a coleção e outra *coleção*, trocando o 
        máximo de figurinhas repetidas possíveis entre as coleções.
        As figurinhas trocadas são escolhidas por ordem.

        Requer que as duas coleções possuam o mesmo tamanho.
        '''
        raise NotImplemented
