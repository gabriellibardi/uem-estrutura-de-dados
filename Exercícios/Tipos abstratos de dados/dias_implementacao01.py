from enum import Enum

class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = 0
    SEG = 1
    TER = 2
    QUA = 3
    QUI = 4
    SEX = 5
    SAB = 6

class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''
    lista_dias: list[bool]

    def __init__(self):
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''
        self.lista_dias = [False] * 7

    def alterna(self, d: Dia):
        '''
        Alterna a pertinencia do dia *d* no conjunto *dias*, isto é, se *d* está
        em *dias*, *d* é removido. Se *d* não está em *dias, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['sex']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['seg', 'sex']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['seg']
        '''
        self.lista_dias[d.value] = not self.lista_dias[d.value]


    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que estão no
        conjunto de dias *d*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''
        abreviacoes = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        dias_ativos = list()
        for i in range(7):
            if self.lista_dias[i]:
                dias_ativos.append(abreviacoes[i])
        return dias_ativos
