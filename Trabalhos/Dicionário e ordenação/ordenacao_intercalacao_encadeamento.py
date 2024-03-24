from __future__ import annotations
from dataclasses import dataclass

# Dupla: Gabriel Libardi Lulu e Vitor da Rocha Machado
# RAs: 134728 e 132769

@dataclass
class No:
    valor: int
    prox: Lista

Lista = No | None

def ordena(lst: Lista) -> Lista:
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplo

    >>> arranjo(ordena(lista([5, 2, 4, 6, 1, 3])))
    [1, 2, 3, 4, 5, 6]

    Testes de propriedade
    A seguir, listas com tamanhos n = 0, 1, ..., 10,
    são geradas com os elementos 0, 1, ..., n. Para
    cada lista todas as suas permutações são usadas
    para testar o algoritmo de ordenação.
    >>> from itertools import permutations
    >>> for n in range(0, 11):
    ...     for p in permutations(range(n)):
    ...         lst = lista(list(p))
    ...         lst = ordena(lst)
    ...         assert lst == lista(list(range(n)))
    '''
    # TODO: implementar o algoritmo de ordenação!
    
    # Divisão

    j = lst # Atribuição é realizada antes devido ao mypy
    if j is None or j.prox is None:
        return j
    else:
        for _ in range(tamanho(j) // 2 - 1):
            j = j.prox
        direita = j.prox
        j.prox = None
        esquerda = lst

        # Conquista
        
        esquerda = ordena(esquerda)
        direita = ordena(direita)

        # Combinação

        return intercalacao(esquerda, direita)

def tamanho(lst: Lista) -> int:
    '''
    Retorna o tamanho de um encademanto.

    Exemplos:
    >>> p = None
    >>> tamanho(p)
    0
    >>> p = No(10, None)
    >>> tamanho(p)
    1
    >>> p = No(15, No(10, None))
    >>> tamanho(p)
    2
    '''
    tam = 0
    if lst is not None:
        tam += 1
        j = lst
        while j.prox is not None:
            tam += 1
            j = j.prox
    return tam

def intercalacao(a: Lista, b: Lista) -> Lista:
    '''
    A partir de dois encadeamentos *a* e *b* em ordem não decrescente,
    retorna um encadeamento intercalando os elementos dos dois de forma
    que o novo fique também em ordem não decrescente.

    Exemplos:
    >>> p = No(1, No(4, No(7, None)))
    >>> q = No(3, No(7, None))
    >>> intercalacao(p, q.prox.prox)
    No(valor=1, prox=No(valor=4, prox=No(valor=7, prox=None)))
    >>> intercalacao(p, q.prox)
    No(valor=1, prox=No(valor=4, prox=No(valor=7, prox=No(valor=7, prox=None))))
    >>> intercalacao(p, q)
    No(valor=1, prox=No(valor=3, prox=No(valor=4, prox=No(valor=7, prox=No(valor=7, prox=None)))))
    '''
    if a is None:
        return b
    elif b is None:
        return a
    else:
        if a.valor <= b.valor:
            inter = No(a.valor, None)
            inter.prox = intercalacao(a.prox, b)
        else: # a.valor > b.valor
            inter = No(b.valor, None)
            inter.prox = intercalacao(a, b.prox)
        return inter

def lista(a: list[int]) -> Lista:
    '''
    Cria uma Lista com os elementos de *lst*.

    Exemplo
    >>> arranjo(lista([5, 1, 4]))
    [5, 1, 4]
    '''
    # cria um sentinela
    inicio = No(0, None)
    p = inicio
    for x in a:
        p.prox = No(x, None)
        p = p.prox
    # descarta o sentinela
    return inicio.prox


def arranjo(lst: Lista) -> list[int]:
    '''
    Cria um arranjo com os elementos de *lst*.
    '''
    a = []
    while lst is not None:
        a.append(lst.valor)
        lst = lst.prox
    return a
