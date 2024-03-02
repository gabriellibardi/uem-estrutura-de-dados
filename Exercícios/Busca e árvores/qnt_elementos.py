from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esquerda: Arvore
    valor: int
    direita: Arvore 

Arvore = No | None

def insere(t: Arvore, valor: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção do *valor* em *t*.
    Se o *valor* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.

    Exemplo
    >>> r = None
    >>> r = insere(None, 10)
    >>> r
    No(esquerda=None, valor=10, direita=None)
    '''
    if t is None:
        return No(None, valor, None)
    else:
        if valor < t.valor:
            t.esquerda = insere(t.esquerda, valor)
        elif valor > t.valor:
            t.direita = insere(t.direita, valor)
        else: # val == t.val
            pass
        return t

def qnt_elementos(t: Arvore) -> int:
    '''
    Devolve a quantidade de elementos da árvore binária *t*

    Exemplos:
    >>> t = None
    >>> qnt_elementos(t)
    0
    >>> t = No(None, 3, None)
    >>> qnt_elementos(t)
    1
    >>> t = insere(t, 19)
    >>> t = insere(t, 32)
    >>> t = insere(t, 1)
    >>> t = insere(t, 12)
    >>> qnt_elementos(t)
    5
    '''
    if t is None:
        return 0
    else:
        return 1 + qnt_elementos(t.esquerda) + qnt_elementos(t.direita)
