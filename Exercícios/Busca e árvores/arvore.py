from dataclasses import dataclass

@dataclass
class No:
    esquerda = Arvore
    valor = int
    direita = Arvore 

Arvore = No | None
