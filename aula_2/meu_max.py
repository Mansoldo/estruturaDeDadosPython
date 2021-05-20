#pacote que carrega o 'infinito'
from math import inf

#função do máximo
def meu_max(iteravel):
    numero_maximo = -inf
    for numero in iteravel:
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo

if __name__ == '__main__':
    print(meu_max([1]))
    print(meu_max([1, 100]))