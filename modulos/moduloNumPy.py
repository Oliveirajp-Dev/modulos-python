import matplotlib.pyplot as plt # biblioteca matplotlib para criar graficos
import numpy as np # biblioteca numpy para manipulação de arrays    

vendas=np.random.randint(1000,3000,50) #gerar 50 numeros aleatorios entre 1000 e 3000
meses=np.arange(1,51) #gerar um array com os numeros de 1 a 50
plt.figure(1, figsize=(17,3)) #criar uma figura com tamanho 17x3
plt.subplot(1, 3, 1) #criar uma figura com 1 linha e 3 colunas
plt.plot(meses,vendas) #plotar o grafico
plt.xlabel('Meses') #legenda eixo x
plt.ylabel('Vendas') #legenda eixo y
plt.axis([0,50,0,max(vendas)+500]) #definir os limites dos eixos x e y, eixo X de 0 a 50 e eixo Y de 0 ao maximo de vendas + 500 apenas para melhor visualização e espaço em cima


plt.subplot(1, 3, 2) #criar uma figura com 1 linha e 3 colunas
plt.bar(meses,vendas) #plotar o grafico de barras
plt.xlabel('Meses') #legenda eixo x
plt.ylabel('Vendas') #legenda eixo y    
plt.axis([0,50,0,max(vendas)+500]) #definir os limites dos eixos x e y


plt.subplot(1, 3, 3) #criar uma figura com 1 linha e 3 colunas
plt.scatter(meses,vendas) #plotar o grafico de dispersão
plt.xlabel('Meses') #legenda eixo x
plt.ylabel('Vendas') #legenda eixo y
plt.axis([0,50,0,max(vendas)+500]) #definir os limites dos eixos x e y
plt.show() #exibir o grafico

# qualquer duvida sobre numpy e matplotlib, veja a documentacao oficial:
# numpy: https://numpy.org/doc/stable/
# matplotlib: https://matplotlib.org/stable/contents.html