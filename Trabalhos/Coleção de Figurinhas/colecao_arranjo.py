from __future__ import annotations
from ed import array

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
    >>> d.str_repetidas()
    '[]'
    '''

    figurinhas: array[int] # Quantidade de cada figurinha representada pelo seu índice

    def __init__(self, quantidade_total: int) -> None:
        '''
        Cria uma coleção de figurinhas com a *quantidade_total*
        de figurinhas do álbum.

        Requer *quantidade_total* > 0
        '''
        self.figurinhas = array(quantidade_total, 0)
    
    def insere(self, figurinha: int):
        '''
        Insere a *figurinha* na coleção.

        Requer que 1 <= *figurinha* <= tamanho da coleção

        Exemplos:
        >>> c = Colecao(50)
        >>> c.insere(9)
        >>> c.insere(38)
        >>> c.insere(9)
        >>> c.str_possuidas()
        '[9, 38]'
        >>> c.str_repetidas()
        '[9 (1)]'
        >>> c.insere(99)
        Traceback (most recent call last):
        ...
        ValueError: A figurinha 99 não faz parte do álbum.
        '''
        if figurinha < 1 or figurinha > len(self.figurinhas):
            raise ValueError(f'A figurinha {figurinha} não faz parte do álbum.')
        else:
            self.figurinhas[figurinha - 1] += 1

    def remove(self, figurinha: int):
        '''
        Remove a *figurinha* da coleção.

        Requer que 1 <= *figurinha* <= tamanho da coleção
        Requer que *figurinha* faça parte da coleção.

        Exemplos:
        >>> c = Colecao(100)
        >>> c.insere(49)
        >>> c.insere(21)
        >>> c.str_possuidas()
        '[21, 49]'
        >>> c.remove(21)
        >>> c.str_possuidas()
        '[49]'
        >>> c.remove(0)
        Traceback (most recent call last):
        ...
        ValueError: A figurinha 0 não faz parte do álbum.
        >>> c.remove(33)
        Traceback (most recent call last):
        ...
        ValueError: A figurinha 33 não está na coleção.
        '''
        if figurinha < 1 or figurinha > len(self.figurinhas):
            raise ValueError(f'A figurinha {figurinha} não faz parte do álbum.')
        elif self.figurinhas[figurinha - 1] <= 0:
            raise ValueError(f'A figurinha {figurinha} não está na coleção.')
        else:
            self.figurinhas[figurinha - 1] -= 1

    def str_possuidas(self) -> str:
        '''
        Gera uma representação em string das figurinhas presentes na coleção,
        sem considerar repetições.

        Exemplos:
        >>> c = Colecao(100)
        >>> c.insere(21)
        >>> c.insere(1)
        >>> c.insere(33)
        >>> c.insere(1)
        >>> c.str_possuidas()
        '[1, 21, 33]'
        '''
        string = '['
        for i in range(len(self.figurinhas)):
            if self.figurinhas[i] > 0:
                string += str(i + 1) + ', '
        if string[-1] != '[':
            string = string[:-2]
        return string + ']'

    def str_repetidas(self) -> str:
        '''
        Gera uma representação em string das figurinhas repetidas da coleção,
        indicando a quantidade de repetições.

        Exemplos:
        >>> c = Colecao(100)
        >>> c.insere(21)
        >>> c.insere(1)
        >>> c.insere(33)
        >>> c.insere(1)
        >>> c.insere(33)
        >>> c.insere(33)
        >>> c.str_repetidas()
        '[1 (1), 33 (2)]'
        '''
        string = '['
        for i in range(len(self.figurinhas)):
            if self.figurinhas[i] > 1:
                string += str(i + 1) + ' (' + str(self.figurinhas[i] - 1) + '), '
        if string[-1] != '[':
            string = string[:-2]
        return string + ']'
    
    def troca_maxima(self, colecao: Colecao):
        '''
        Realiza uma troca entre a coleção e outra *coleção*, trocando o 
        máximo de figurinhas repetidas possíveis entre as coleções.
        As figurinhas trocadas são escolhidas por ordem.

        Requer que as duas coleções possuam o mesmo tamanho.

        Exemplos:
        >>> x = Colecao(100)
        >>> x.insere(93)
        >>> x.insere(32)
        >>> x.insere(32)
        >>> x.insere(32)
        >>> x.insere(12)
        >>> x.insere(12)
        >>> x.insere(4)
        >>> x.insere(4)
        >>> x.str_possuidas()
        '[4, 12, 32, 93]'
        >>> x.str_repetidas()
        '[4 (1), 12 (1), 32 (2)]'

        >>> y = Colecao(50)
        >>> y.insere(21)
        >>> y.insere(21)
        >>> y.str_possuidas()
        '[21]'
        >>> y.str_repetidas()
        '[21 (1)]'

        >>> z = Colecao(100)
        >>> z.insere(31)
        >>> z.insere(31)
        >>> z.insere(2)
        >>> z.insere(2)
        >>> z.str_possuidas()
        '[2, 31]'
        >>> z.str_repetidas()
        '[2 (1), 31 (1)]'

        >>> x.troca_maxima(y)
        Traceback (most recent call last):
        ...
        ValueError: O tamanho das coleções é diferente.

        >>> x.troca_maxima(z)
        >>> x.str_possuidas()
        '[2, 4, 12, 31, 32, 93]'
        >>> x.str_repetidas()
        '[32 (2)]'
        >>> z.str_possuidas()
        '[2, 4, 12, 31]'
        >>> z.str_repetidas()
        '[]'
        '''
        # Certifica que as duas coleções possuem o mesmo tamanho
        if len(self.figurinhas) != len(colecao.figurinhas):
            raise ValueError('O tamanho das coleções é diferente.')
        else:
            # Percorre as duas coleções e coloca as cartas que podem 
            # ser trocadas em arranjos.
            trocaveis_a = array(len(self.figurinhas), 0)
            trocaveis_b = array(len(self.figurinhas), 0)
            indice_a = 0
            indice_b = 0
            for figurinha in range(len(self.figurinhas)):
                if self.figurinhas[figurinha] >= 2 and colecao.figurinhas[figurinha] == 0:
                    trocaveis_a[indice_a] = figurinha + 1
                    indice_a += 1
                elif colecao.figurinhas[figurinha] >= 2 and self.figurinhas[figurinha] == 0:
                    trocaveis_b[indice_b] = figurinha + 1
                    indice_b += 1
            # Percorre os arranjos de cartas trocáveis até um deles 
            # chegar à zero (esse não possui mais cartas trocáveis).
            restam_trocas = True
            i = 0
            while restam_trocas and i < len(trocaveis_a):
                if trocaveis_a[i] != 0 and trocaveis_b[i] != 0:
                    self.insere(trocaveis_b[i])
                    self.remove(trocaveis_a[i])
                    colecao.insere(trocaveis_a[i])
                    colecao.remove(trocaveis_b[i])
                else:
                    restam_trocas = False
                i += 1
