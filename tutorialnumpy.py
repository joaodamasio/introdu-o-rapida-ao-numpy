import numpy as np

#a função np.array permite a criação de arrays de n dimensões de acordo com o numero de colchetes

array_de_uma_dimensao = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(array_de_uma_dimensao) #funçao que permite a criação de um array com uma dimensao

array_de_duas_dimensoes = np.array([[6, 3], [5, 2],[4, 1]])
print(array_de_duas_dimensoes)#funçao que permite a criação de um array com duas dimensões



#a função np.arange permite você preencher arrays com sequência de números pré definidos

inteiros_sequenciais = np.arange(5, 12)
print(inteiros_sequenciais) #exibe um array de uma dimensão com os valores de 5 até 11, ja que o 12 é excludente




#a função np.random permite você preencher arrays com números aletórios

numeros_inteiros_aleatorios_entre_50_e_100 = np.random.randint(low=50, high=101, size=(6))
print(numeros_inteiros_aleatorios_entre_50_e_100) #gera um array de uma dimensão de tamanho 6 que  contem valores aleatórios entre 50 e 100

numeros_flutuantes_aletorios_entre_0_e_1 = np.random.random([6])
print(numeros_flutuantes_aletorios_entre_0_e_1) #imprime uma lista com seis valores futuantes entre 0 e 1



#operações matemáticas

numeros_flutuantes_aletorios_entre_2_e_3 = numeros_flutuantes_aletorios_entre_0_e_1 + 2.0
print(numeros_flutuantes_aletorios_entre_2_e_3) #soma

numeros_inteiros_aleatorios_entre_150_e_300 = numeros_inteiros_aleatorios_entre_50_e_100 * 3
print(numeros_inteiros_aleatorios_entre_150_e_300) #multiplicação

numeros_aleatorios_entre_150_e_300_dividos_por_2= numeros_inteiros_aleatorios_entre_150_e_300/2
print(numeros_aleatorios_entre_150_e_300_dividos_por_2) #divisão