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
    lista_dias: list(Dia)

    def __init__(self):
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''
        self.lista_dias = list()

    def alterna(self, d: Dia):
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

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
        if d in self.lista_dias:
            self.lista_dias.remove(d)
        else:
            self.lista_dias.append(d)

    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

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
        abreviacoes_base = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        abreviacoes_desordenadas = []
        abreviacoes_ordenadas = []
        for dia in self.lista_dias:
            abreviacoes_desordenadas.append(dia.name.lower())
        for abreviacao in abreviacoes_base:
            if abreviacao in abreviacoes_desordenadas:
                abreviacoes_ordenadas.append(abreviacao)
        return abreviacoes_ordenadas
