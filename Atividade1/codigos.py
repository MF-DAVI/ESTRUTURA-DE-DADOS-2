#link do google colab: https://colab.research.google.com/drive/1FKexA8epIiCIln8ckeCMv2isY9IUuDFB?usp=sharing

#Bubble sort
def bubble_sort(vetor):
  n = len(vetor)
  comparacoes = 0
  trocas = 0

  for i in range(n - 1): #troca 30 por 20. for i faz a passada varias vezes
    trocou = False
    for j in range(n - 1): # troca 30 por 10. for j faz uma passada completa
      comparacoes +=1 # += e a mesma coisa que variavel = variavel + 1
      if vetor[j] > vetor[j+1]:
        vetor[j], vetor[j+1] = vetor[j + 1], vetor[j]
        trocas +=1
        trocou = True
    if  not trocou:
        break
  return comparacoes, trocas

numeros = [30,10,40,20]
compara,troca = bubble_sort(numeros)

print('Bubble sort')
print(numeros)
print('comparaçoes: ',compara)
print('trocas: ',troca)
print()

#=================================================================================

#Quick Sort
print('Quick sort')
def particiona(vetor, inicio, fim, stats):
  pivo = vetor[fim]
  i = inicio - 1

  for j in range(inicio,fim):
    stats['comparacoes'] += 1
    if vetor[j] <= pivo:
      i = i + 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
      stats['movimentacoes'] += 1

  vetor[i + 1], vetor[fim] = vetor[fim], vetor[i+1]
  stats['movimentacoes'] += 1
  return i + 1

def quick_sort(vetor, inicio, fim, stats):
  if inicio < fim:
    pos_pivo = particiona(vetor, inicio, fim, stats) #partiona e desobre onde o pivo ta
    quick_sort(vetor, inicio, pos_pivo - 1, stats) #ordena pivo do lado esquerdo
    quick_sort(vetor, pos_pivo + 1, fim, stats) # ordena a direita

lista = [5,2,8,1,9,3]
print('lista original',lista)

stats = {'comparacoes': 0, 'movimentacoes': 0}

quick_sort(lista, 0, len(lista) - 1, stats)

print('lista ordenada',lista)
print('comparaçoes: ',stats['comparacoes'])
print('movimentaçoes: ',stats['movimentacoes'])
print()

#============================================================================

#gera lista
print('numeros aleatorios')
import random
def gera_lista(tamanho):
  lista =[]
  for i in range(tamanho): # pode usar _ no lugar do i ou j quando esse valor nao tem importancia
    numero_sorteado = random.randint(1, 10000)
    lista.append(numero_sorteado)
  return lista

teste = gera_lista(10)
print(teste)
print()

#============================================================================================================
#PARTE 2 - EXPERIMENTO DE ORDENAÇAO
print('PARTE 2 - EXPERIMENTO DE ORDENAÇAO: ')
tamanhos = [10, 20, 1000]

for tamanho in tamanhos:
    original = gera_lista(tamanho)

    # Bubble Sort
    lista_bubble = original.copy()
    comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

    # Quick Sort
    lista_quick = original.copy()
    stats_quick = {'comparacoes': 0, 'movimentacoes': 0}
    quick_sort(lista_quick, 0, len(lista_quick) - 1, stats_quick)

    # Resultados
    print(f"Tamanho: {tamanho}")
    print(f"Bubble Sort -> comparações: {comparacoes_bubble}, trocas: {trocas_bubble}")
    print(f"Quick Sort  -> comparações: {stats_quick['comparacoes']}, movimentações: {stats_quick['movimentacoes']}")
    print("-" * 50)

  #====================================================================================================================

  #PARTE 3 – INVESTIGAÇÃO DE BUSCA EM MATRIZES: https://colab.research.google.com/drive/1SCim1CmsAeS0S5kS4jzfalVTG3tUOFXE?usp=sharing
  
def busca_sequencial(matriz, valor_procurado):
  comparacoes = 0
  encontrado = False
  linha_encontrada = -1
  coluna_encontrada = -1

  linhas = len(matriz)
  colunas = len(matriz[0])

  for i in range(linhas): #i = linha
    for j in range(colunas): #j = coluna
      comparacoes = comparacoes + 1
      if matriz[i][j] == valor_procurado:
        encontrado = True
        linha_encontrada = i
        coluna_encontrada = j
        break #para o for j
    if encontrado:
      break #para o for i
  return encontrado, linha_encontrada, coluna_encontrada, comparacoes

def gerar_matriz(linhas, colunas):
  matriz = []
  contador = 1
  for i in range(linhas):
    linha_atual = []
    for j in range(colunas):
        linha_atual.append(contador)
        contador = contador + 1
    matriz.append(linha_atual)
  return matriz

matriz_2x2 = gerar_matriz(2, 2)
print('Matriz 2x2:', matriz_2x2)
print('-'*35)

total_elementos = len(matriz_2x2) * len(matriz_2x2[0])
print(f'total de elementos: {total_elementos}')

resultado_inicio = busca_sequencial(matriz_2x2, 1)
print(f'busca no inicio: {resultado_inicio[3]} comparaçao')

resultado_final = busca_sequencial(matriz_2x2,4)
print(f'busca final: {resultado_final[3]} comparaçoes')

resultado_inexistente = busca_sequencial(matriz_2x2, -1)
print(f'busca inexistente: {resultado_inexistente[3]} comparaçoes')
print('-'*35)

#------------------------------------------------------------------------

matriz_10x10 = gerar_matriz(10, 10)
print('matriz 10x10: ')

total_elementos = len(matriz_10x10) * len(matriz_10x10[0])
print(f'total de elementos: {total_elementos}')

resultado_inicio = busca_sequencial(matriz_10x10, 1)
print(f'busca no inicio: {resultado_inicio[3]} comparaçao')

resultado_final = busca_sequencial(matriz_10x10, 100)
print(f'busca final: {resultado_final[3]} comparaçoes')

resultado_inexistente = busca_sequencial(matriz_10x10, -1)
print(f'busca inexistente: {resultado_inexistente[3]} comparaçoes')
print('-'*35)

#------------------------------------------------------------------------
matriz_100x100 = gerar_matriz(100, 100)
print('matriz 100x100: ')

total_elementos = len(matriz_100x100) * len(matriz_100x100[0])
print(f'total de elementos: {total_elementos}')

resultado_inicio = busca_sequencial(matriz_100x100, 1)
print(f'busca no inicio: {resultado_inicio[3]} comparaçao')

resultado_final = busca_sequencial(matriz_100x100, 10000)
print(f'busca final: {resultado_final[3]} comparaçoes')

resultado_inexistente = busca_sequencial(matriz_100x100, -1)
print(f'busca inexistente: {resultado_inexistente[3]} comparaçoes')
print('-'*35)

#==================================================================================================================

# parte 4 Hands On 1 — Array de temperaturas: https://colab.research.google.com/drive/1gUpCGqy66L_brZHbwEk5B4-H7Lq9ztY_?usp=sharing

print("RESULTADOS — ARRAY DE TEMPERATURAS")
print('-'*40)

temperatura = [23.6, 21.4, 23.7, 18.1, 27.2, 27.4, 24.8, 17.4, 22.8, 19.9]
print(temperatura)
soma=0
for i in range(10):
  soma = soma + temperatura[i]
media=soma/10

#print(f'a soma e: {round(soma,2)}')
print(f'a media e: {round(media,2)}') #round serve pra arredondar os numeros

#maior
maior = temperatura[0]
indice_maior = 0

for i in range(10):
  if temperatura[i] > maior:
    maior = temperatura[i]
    indice_maior = i

print('maior valor: ',maior)
print('maior indice: ',indice_maior)

#menor
menor = temperatura[0]
indice_menor = 0

for i in range(10):
  if temperatura[i] < menor:
    menor = temperatura[i]
    indice_menor = i

print('menor valor: ',menor)
print('menor indice: ',indice_menor)

#media
acima_media = 0
for i in range(10):
  if temperatura[i] > media:
   acima_media = acima_media + 1
print('acima da media:',acima_media)

print('complexidade: O(n)')
print('foram realizadas 30 operações de percurso')
print('-'*40)
#===========================================================================================================================

  #Parte 5 — Hands On 2: Monitoramento de Sensores: https://colab.research.google.com/drive/1G1YfaEnEDUJ_Gs-F6YZMZPGMK_W52xDq?usp=sharing

import random

def gerar_sensores():
  sensores = []
  for i in range(5): #5 sensores linha
    linha_sensor =[]
    for j in range(24): #24 horas colunas
      temperatura = round(random.uniform(18, 30),1)
      linha_sensor.append(temperatura)
    sensores.append(linha_sensor)
  return sensores

matriz_sensores = gerar_sensores()

for i in range(5):
    print(f"Sensor {i}: {matriz_sensores[i]}")

#media
print('media sensor: ')
print('-'*35)

medias_sensores = []

for i in range(5):
  soma_sensor = 0
  for j in range(24):
    soma_sensor = soma_sensor + matriz_sensores[i][j]
  media_sensor = soma_sensor /24
  medias_sensores.append(media_sensor)

for i in range(5): #vai repetir esse print 5 vezes para cada media
  print(f'media do sensor {i}: {round(medias_sensores[i],1)}')


print('-'*35)
print('Outros resultados:')

#maior - SENSOR E HORARIO e media

maior_temperatura = matriz_sensores[0][0]
sensor_maior = 0
horario_maior = 0
soma_geral = 0
acima_limite = 0

limite = float(input("Digite o limite de temperatura: ")) #limite


for i in range(5):
  for j in range(24):
    soma_geral = soma_geral + matriz_sensores[i][j] #
    if matriz_sensores[i][j] > maior_temperatura:
        maior_temperatura = matriz_sensores[i][j]
        sensor_maior = i
        horario_maior = j

    if matriz_sensores[i][j] > limite:
      acima_limite = acima_limite + 1

media_geral = soma_geral / 120

print(f'maior temperatura: {maior_temperatura} C')
print(f'sensor responsavel: sensor {sensor_maior}')
print(f'horario da ocorrencia: {horario_maior}h')
print(f'media geral:{round(media_geral,2)} C')
print(f'temperaturas acima do limite {limite} sao {acima_limite} ')
print('Complexidade dos percursos completos: O(m × n)')
