#pacote que carrega o 'infinito'
from time import time
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

    print('Estudo Experimental sobre o tempo de execução da função max')
    inicio = 1_000_000
    for n in range(0, inicio * 20 + 1, inicio):
        inicio = time()
        meu_max(range(n))
        fim = time()
        tempo_de_execucao_em_segundos = fim - inicio
        print('*' * int(tempo_de_execucao_em_segundos * 10), ' - ',  tempo_de_execucao_em_segundos, ' - ', n)
