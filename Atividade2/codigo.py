#link do colab: https://colab.research.google.com/drive/1CCEQ7L8bJVJxRtd9tQ0yCiq1p4BwNFx8?usp=sharing

import random
import sys

sys.setrecursionlimit(10000)

#BUBBLE SORT
def bubble_sort(v):
    comparacoes = 0
    trocas = 0

    n = len(v)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocas += 1

    return comparacoes, trocas

#INSERTION SORT
def insertion_sort(v):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if v[j] > chave:
                v[j + 1] = v[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        v[j + 1] = chave
        movimentacoes += 1

    return comparacoes, movimentacoes

#SELECTION SORT
def selection_sort(v):
    comparacoes = 0
    trocas = 0

    n = len(v)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            trocas += 1
    return comparacoes, trocas

#QUICK SORT
def quick_sort(v):

    comparacoes = 0
    movimentacoes = 0

    def ordenar(esquerda, direita):

        nonlocal comparacoes
        nonlocal movimentacoes

        i = esquerda
        j = direita

        pivo = v[(esquerda + direita) // 2]
        while i <= j:
            while True:
                comparacoes += 1
                if v[i] < pivo:
                    i += 1
                else:
                    break
            while True:

                comparacoes += 1

                if v[j] > pivo:
                    j -= 1
                else:
                    break
            if i <= j:
                if i != j:
                    v[i], v[j] = v[j], v[i]
                    movimentacoes += 1

                i += 1
                j -= 1

        if esquerda < j:
            ordenar(esquerda, j)
        if i < direita:
            ordenar(i, direita)
    if len(v) > 0:
        ordenar(0, len(v) - 1)

    return comparacoes, movimentacoes

def roda_todos(original):
    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    return {
        'bubble': bubble_sort(vetor_bubble),
        'insertion': insertion_sort(vetor_insertion),
        'selection': selection_sort(vetor_selection),
        'quick': quick_sort(vetor_quick),
    }

#EXPERIMENTO
random.seed(10)

tamanhos = [10, 20, 1000]
resultados_principais = {}

for tamanho in tamanhos:
    original = []
    for i in range(tamanho):
        original.append(random.randint(1, 10000))

    resultados_principais[tamanho] = roda_todos(original)

    r = resultados_principais[tamanho]
    print('-'*35)
    print('TAMANHO:', tamanho)
    print('Bubble Sort')
    print('Comparacoes:', r['bubble'][0])
    print('Trocas:', r['bubble'][1])
    print('\nInsertion Sort')
    print('Comparacoes:', r['insertion'][0])
    print('Movimentacoes:', r['insertion'][1])
    print('\nSelection Sort')
    print('Comparacoes:', r['selection'][0])
    print('Trocas:', r['selection'][1])
    print('\nQuick Sort')
    print('Comparacoes:', r['quick'][0])
    print('Movimentacoes:', r['quick'][1])


#DESAFIO ADICIONAL
print('')
print('DESAFIO ADICIONAL (tamanho = 1000)')

tamanho_desafio = 1000
aleatorio = [random.randint(1, 10000) for _ in range(tamanho_desafio)]
ordenado = sorted(aleatorio)
invertido = sorted(aleatorio, reverse=True)

casos = {
    'Aleatorio': aleatorio,
    'Ordenado': ordenado,
    'Ordem inversa': invertido,
}

for nome, vetor in casos.items():
    r = roda_todos(vetor)

    print('-'*35)
    print('CASO:', nome)
    print('-'*35)
    print('Bubble Sort')
    print('Comparacoes:', r['bubble'][0])
    print('Trocas:', r['bubble'][1])
    print('\nInsertion Sort')
    print('Comparacoes:', r['insertion'][0])
    print('Movimentacoes:', r['insertion'][1])
    print('\nSelection Sort')
    print('Comparacoes:', r['selection'][0])
    print('Trocas:', r['selection'][1])
    print('\nQuick Sort')
    print('Comparacoes:', r['quick'][0])
    print('Movimentacoes:', r['quick'][1])
