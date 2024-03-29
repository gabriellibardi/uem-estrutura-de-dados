from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    proximo: No | None
    
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
    figurinhas: No | None
    tamanho_max: int

    def __init__(self, quantidade_total: int):
        '''
        Cria uma coleção de figurinhas com a *quantidade_total*
        de figurinhas do álbum.

        Requer *quantidade_total* > 0
        '''
        self.figurinhas = None
        self.tamanho_max = quantidade_total
    
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
        # A figurinha não faz parte do álbum
        if figurinha < 1 or figurinha > self.tamanho_max:
            raise ValueError(f'A figurinha {figurinha} não faz parte do álbum.')
        # A coleção está vazia
        elif self.figurinhas is None:
            self.figurinhas = No(figurinha, None)
        # A figurinha nova é menor que a primeira da coleção
        elif self.figurinhas.item > figurinha:
            self.figurinhas = No(figurinha, self.figurinhas)
        # A figurinha nova é maior que a primeira da coleção
        else:
            c = self.figurinhas
            while c.proximo is not None and c.proximo.item < figurinha:
                c = c.proximo
            c.proximo = No(figurinha, c.proximo)

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
        # A figurinha não faz parte do álbum
        if figurinha < 1 or figurinha > self.tamanho_max:
            raise ValueError(f'A figurinha {figurinha} não faz parte do álbum.')
        # A coleção está vazia
        elif self.figurinhas is None:
            raise ValueError(f'A figurinha {figurinha} não está na coleção.')
        # Confere se a figurinha a ser removida está na primeira posição
        elif figurinha == self.figurinhas.item:
            self.figurinhas = self.figurinhas.proximo
        else:
            c = self.figurinhas
            while c.proximo is not None and figurinha > c.proximo.item:
                c = c.proximo
            # A figurinha não está na coleção
            if c.proximo is None or figurinha != c.proximo.item:
                raise ValueError(f'A figurinha {figurinha} não está na coleção.')
            # A figurinha está na coleção e será removida
            else:
                c.proximo = c.proximo.proximo

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
        if self.figurinhas is not None:
            c = self.figurinhas
            item_atual = 0
            while c.proximo is not None:
                if c.item != item_atual: # Remove as repetições
                    string += str(c.item) + ', '
                    item_atual = c.item
                c = c.proximo
            # Último item da colecão
            if c.item != item_atual:
                string += str(c.item)
            else:
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
        if self.figurinhas is not None:
            c = self.figurinhas
            item_atual = 0
            repeticoes = 0
            while c.proximo is not None:
                # Item se repete
                if c.item == item_atual:
                    repeticoes += 1
                # Trocou de item
                else:
                    if repeticoes >= 1:
                        string += str(item_atual) + ' (' + str(repeticoes) + '), '
                    item_atual = c.item
                    repeticoes = 0
                c = c.proximo
            # Último item da coleção repetido
            if c.item == item_atual:
                repeticoes += 1
                string += str(item_atual) + ' (' + str(repeticoes) + ')'
            # Último item vindo depois de uma repetição
            elif repeticoes >= 1:
                string += str(item_atual) + ' (' + str(repeticoes) + ')'
            # Último item vindo depois de um item sem repetição
            else:
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
        a = self
        b = colecao
        if self.tamanho_max != colecao.tamanho_max:
            raise ValueError('O tamanho das coleções é diferente.')
        else:
            if a.figurinhas is not None and b.figurinhas is not None:
                repetidas_a = a.__repetidas()
                repetidas_b = b.__repetidas()
                # Caso as duas coleções possuam figurinhas repetidas
                if repetidas_a is not None and repetidas_b is not None:
                    a.__remove_nao_trocaveis(repetidas_b)
                    b.__remove_nao_trocaveis(repetidas_a)
                    trocaveis_a = repetidas_a.figurinhas
                    trocaveis_b = repetidas_b.figurinhas
                    if trocaveis_a is not None and trocaveis_b is not None:
                        # Enquanto uma das coleções trocáveis não chegar ao fim
                        while trocaveis_a.proximo is not None and trocaveis_b.proximo is not None:
                            a.insere(trocaveis_b.item)
                            b.remove(trocaveis_b.item)
                            b.insere(trocaveis_a.item)
                            a.remove(trocaveis_a.item)
                            trocaveis_a = trocaveis_a.proximo
                            trocaveis_b =trocaveis_b.proximo
                        # Última figurinha
                        a.insere(trocaveis_b.item)
                        b.remove(trocaveis_b.item)
                        b.insere(trocaveis_a.item)
                        a.remove(trocaveis_a.item)

    def __repetidas(self) -> Colecao:
        '''
        Cria uma nova colecao com as figurinhas repetidas da *colecao*
        '''
        c = self.figurinhas
        assert c is not None
        repetidas = Colecao(self.tamanho_max)
        item_atual = 0
        ja_repetida = False
        while c.proximo is not None:
            if c.item == item_atual and not ja_repetida:
                repetidas.insere(c.item)
                ja_repetida = True
            elif c.item != item_atual:
                item_atual = c.item
                ja_repetida = False
            c = c.proximo
        # Última figurinha
        if c.item == item_atual and not ja_repetida:
            repetidas.insere(c.item)
        return repetidas
    
    def __remove_nao_trocaveis(self, repetidas: Colecao):
        '''
        Remove as figurinhas não trocaveis da coleção de *repetidas* em
        comparação com outra *colecao*
        '''
        rep = repetidas.figurinhas
        c = self.figurinhas
        if rep is not None and c is not None:
            while rep.proximo is not None:
                # Conferir se o item das repetidas atual está na coleção
                while c.proximo is not None and rep.item > c.proximo.item:
                    c = c.proximo
                if c.proximo is not None and rep.item == c.proximo.item:
                    repetidas.remove(rep.item)
                rep = rep.proximo
