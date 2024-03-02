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

def qnt_grau2(t: Arvore) -> int:
    '''
    Devolve a quantidade de nós na árvore binária *t* que possuem grau 2.
    Para o Nó possuir grau 2, ele precisa ter dois filhos.

    Exemplos:
    >>> t = None
    >>> qnt_grau2(t)
    0
    >>> t = No(None, 3, None)
    >>> qnt_grau2(t)
    0
    >>> t = insere(t, 19)
    >>> t = insere(t, 32)
    >>> qnt_grau2(t)
    0
    >>> t = insere(t, 1)
    >>> qnt_grau2(t)
    1
    >>> t = insere(t, 12)
    >>> t = insere(t, -12)
    >>> t = insere(t, -13)
    >>> t = insere(t, -8)
    >>> qnt_grau2(t)
    3
    '''
    if t is None:
        return 0
    elif t.esquerda is not None and t.direita is not None:
        return 1 + qnt_grau2(t.esquerda) + qnt_grau2(t.direita)
    else:
        return qnt_grau2(t.esquerda) + qnt_grau2(t.direita)

def eh_cheia(t: Arvore) -> bool:
    '''
    Devolve True caso a árvore binária *t* seja cheia e
    False, caso não seja uma árvore cheia.
    Uma árvore binária cheia é aquela em que todos os seus 
    nós tem grau 0 ou 2.

    Exemplos:
    >>> t = None
    >>> eh_cheia(t)
    True
    >>> t = insere(t, 6)
    >>> eh_cheia(t)
    True
    >>> t = insere(t, 21)
    >>> eh_cheia(t)
    False
    >>> t = insere(t, 3)
    >>> eh_cheia(t)
    True
    >>> t = insere(t, 32)
    >>> t = insere(t, 15)
    >>> eh_cheia(t)
    True
    '''
    if t is None:
        return True
    elif (t.esquerda is not None and t.direita is None) or \
        (t.direita is not None and t.esquerda is None):
        return False
    else:
        return True and eh_cheia(t.esquerda) and eh_cheia(t.direita)
