from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esquerda: Arvore
    valor: int
    direita: Arvore 

Arvore = No | None

def cria_abb(lista: list[int]) -> Arvore:
    '''
    Cria uma Árvore Binária de Busca (ABB) balanceada a partir
    de uma *lista* de inteiros.
    Requer que *lista* possua valores distintos em ordem crescente.

    Exemplos:
    >>> cria_abb([])
    >>> cria_abb([15])
    No(esquerda=None, valor=15, direita=None)
    >>> cria_abb([1, 2, 3, 4, 5, 6])
    No(esquerda=No(esquerda=No(esquerda=None, valor=1, direita=None), valor=2, direita=No(esquerda=None, valor=3, direita=None)), valor=4, direita=No(esquerda=No(esquerda=None, valor=5, direita=None), valor=6, direita=None))
    '''
    if lista == []:
        return None
    else:
        meio = (len(lista)) // 2
        return No(cria_abb(lista[:meio]), lista[meio], cria_abb(lista[meio + 1:]))
 