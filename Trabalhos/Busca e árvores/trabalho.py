from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esquerda: Arvore
    valor: int
    direita: Arvore

    def __repr__(self) -> str:
        '''
        Devolve uma representação dos nós usando um percurso pré-ordem. Nós
        vazios não aparecen na saída. A representação de um nó que não é vazio
        é composto por abre parênteses, a representação do nó a esquerda, o
        valor do nó entre espaços, seguido da representação do nó a direita,
        seguido de fecha parênteses.

        Exemplos:
        >>> No(No(None, 6, None), 5, None)
        (( 6 ) 5 )
        >>> No(None, 2, No(None, 6, None))
        ( 2 ( 6 ))
        '''
        if self.esquerda is None:
            esquerda = ''
        else:
            esquerda = repr(self.esquerda)
        if self.direita is None:
            direita = ''
        else:
            direita = repr(self.direita)
        return f'({esquerda} {self.valor} {direita})'

Arvore = No | None


def cria_avl(lista: list[int]) -> Arvore:
    '''
    Cria uma Árvore Binária de Busca Balanceada (AVL) a partir
    de uma *lista* de inteiros.
    Requer que *lista* possua valores distintos em ordem crescente.

    Exemplos:
    >>> r = cria_avl([])
    >>> r
    >>> r = cria_avl([15])
    >>> r
    ( 15 )
    >>> r = cria_avl([1, 2, 3, 4, 5, 6])
    >>> r
    ((( 1 ) 2 ( 3 )) 4 (( 5 ) 6 ))
    '''
    if lista == []:
        return None
    else:
        meio = (len(lista)) // 2
        return No(cria_avl(lista[:meio]), lista[meio], cria_avl(lista[meio + 1:]))

   
def mesmos_elementos(t: Arvore, r: Arvore) -> bool:
    '''
    Retorna True caso as ABBs *t* e *r* possuam os mesmos elementos
    e False caso contrário.

    Exemplos:

    >>> t = cria_avl([])
    >>> r = cria_avl([])
    >>> mesmos_elementos(t, r)
    True

    >>> r = cria_avl([1, 2, 3])
    >>> mesmos_elementos(t, r)
    False

    >>> t = cria_avl([2, 5, 10, 300]) #Balanceada
    >>> r = cria_avl([])
    >>> mesmos_elementos(t, r)
    False

    >>> r = No(None, 2, No(None, 5, No(None, 10, No(None, 300, None)))) #Desbalanceada
    >>> mesmos_elementos(t, r)
    True

    >>> r = No(None, 1, No(None, 2, No(None, 3, No(None, 4, None))))
    >>> mesmos_elementos(t, r)
    False

    >>> r = cria_avl([2, 5, 10, 300, 1000])
    >>> mesmos_elementos(t, r)
    False
    '''
    if qnt_elementos(t) != qnt_elementos(r):
        return False
    else:
        return estao_na_arvore(t, r)


def estao_na_arvore(t: Arvore, r: Arvore) -> bool:
    '''
    Retorna True caso todos os elementos da AAB *t* estão
    na ABB *r*.

    Exemplos:
    >>> t = cria_avl([])
    >>> r = cria_avl([])
    >>> estao_na_arvore(t, r)
    True
    >>> r = cria_avl([0, 1, 2])
    >>> estao_na_arvore(t, r)
    True
    >>> t = cria_avl([0, 1])
    >>> estao_na_arvore(t, r)
    True
    >>> t = cria_avl([0, 1, 2, 3])
    >>> estao_na_arvore(t, r)
    False
    '''
    if t is None:
        return True
    else:
        return estao_na_arvore(t.esquerda, r) \
               and busca_binaria(r, t.valor) \
               and estao_na_arvore(t.direita, r)
    

def qnt_elementos(t: Arvore) -> int:
    '''
    Retorna a quantidade de elementos não nulos de uma árvore.

    Exemplos:
    >>> r = cria_avl([])
    >>> qnt_elementos(r)
    0
    >>> r = cria_avl([3, 5, 6, 10, 43, 54, 100, 432])
    >>> qnt_elementos(r)
    8
    '''
    if t is None:
        return 0
    else:
        return 1 + qnt_elementos(t.esquerda) + qnt_elementos(t.direita)


def busca_binaria(t: Arvore, valor: int) -> bool:
    '''
    Retorna True caso o *valor* esteja na Árvore Binária de Busca *t*
    e False caso não esteja.
    Requer que *t* seja uma Árvore Binária de Busca (ABB)

    Exemplos:
    >>> r = cria_avl([])
    >>> busca_binaria(r, 0)
    False
    >>> r = cria_avl([3, 5, 6, 10, 43, 54, 100, 432])
    >>> busca_binaria(r, 3)
    True
    >>> busca_binaria(r, 6)
    True
    >>> busca_binaria(r, 30)
    False
    >>> busca_binaria(r, 432)
    True
    '''
    if t is None:
        return False
    elif valor == t.valor:
        return True
    elif valor < t.valor:
        return busca_binaria(t.esquerda, valor)
    else: # valor > t.valor
        return busca_binaria(t.direita, valor)
