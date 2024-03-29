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
        >>> a = Colecao(10)
        >>> b = Colecao(11)

        >>> a.troca_maxima(b)
        Traceback (most recent call last):
        ...
        ValueError: O tamanho das coleções é diferente.

        >>> a = Colecao(5)
        >>> b = Colecao(5)
        >>> a.str_possuidas()
        '[]'
        >>> a.str_repetidas()
        '[]'
        >>> b.str_possuidas()
        '[]'
        >>> b.str_repetidas()
        '[]'
        >>> a.troca_maxima(b)
        >>> a.str_possuidas()
        '[]'
        >>> a.str_repetidas()
        '[]'
        >>> b.str_possuidas()
        '[]'
        >>> b.str_repetidas()
        '[]'

        >>> a.insere(1)
        >>> a.insere(2)
        >>> a.str_possuidas()
        '[1, 2]'
        >>> a.str_repetidas()
        '[]'
        >>> a.troca_maxima(b)
        >>> a.str_possuidas()
        '[1, 2]'
        >>> a.str_repetidas()
        '[]'
        >>> b.str_possuidas()
        '[]'
        >>> b.str_repetidas()
        '[]'

        >>> b.insere(3)
        >>> b.insere(5)
        >>> b.str_possuidas()
        '[3, 5]'
        >>> b.str_repetidas()
        '[]'
        >>> a.troca_maxima(b)
        >>> a.str_possuidas()
        '[1, 2]'
        >>> a.str_repetidas()
        '[]'
        >>> b.str_possuidas()
        '[3, 5]'
        >>> b.str_repetidas()
        '[]'

        >>> b.insere(5)
        >>> b.str_possuidas()
        '[3, 5]'
        >>> b.str_repetidas()
        '[5 (1)]'
        >>> a.troca_maxima(b)
        >>> a.str_possuidas()
        '[1, 2]'
        >>> a.str_repetidas()
        '[]'
        >>> b.str_possuidas()
        '[3, 5]'
        >>> b.str_repetidas()
        '[5 (1)]'

        >>> a.insere(1)
        >>> a.insere(2)
        >>> a.insere(2)
        >>> b.insere(3)
        >>> b.insere(4)
        >>> a.str_possuidas()
        '[1, 2]'
        >>> a.str_repetidas()
        '[1 (1), 2 (2)]'
        >>> b.str_possuidas()
        '[3, 4, 5]'
        >>> b.str_repetidas()
        '[3 (1), 5 (1)]'
        >>> a.troca_maxima(b)
        >>> a.str_possuidas()
        '[1, 2, 3, 5]'
        >>> a.str_repetidas()
        '[2 (1)]'
        >>> b.str_possuidas()
        '[1, 2, 3, 4, 5]'
        >>> b.str_repetidas()
        '[]'
        '''
        # Certifica que as duas coleções possuem o mesmo tamanho
        if len(self.figurinhas) != len(colecao.figurinhas):
            raise ValueError('O tamanho das coleções é diferente.')
        else:
            trocaveis_a = self.__trocaveis(colecao)
            trocaveis_b = colecao.__trocaveis(self)
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

    def __trocaveis(self, colecao_comparada: Colecao) -> array[int]:
        '''
        Cria um array do tamanho da coleção com as suas figurinhas que podem
        ser trocadas em relação a *coleção_comparada*.
        As figurinhas do array serão ordenadas pelo seu índice.
        '''
        trocaveis = array(len(self.figurinhas), 0)
        i = 0
        for figurinha in range(len(self.figurinhas)):
            if self.figurinhas[figurinha] >= 2 and \
                colecao_comparada.figurinhas[figurinha] == 0:
                trocaveis[i] = figurinha + 1
                i += 1
        return trocaveis
