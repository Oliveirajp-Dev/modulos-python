import matplotlib.pyplot as plt # biblioteca matplotlib para criar graficos 

vendas_meses=[1500,1727,1350,999,1999,2380,1433]
meses=['jan', 'fev', 'mar', 'abr', 'mai','jun', ' jul']

#plotar o grafico 
plt.plot(meses,vendas_meses) #plotar o grafico
plt.xlabel('Meses') #legenda eixo x
plt.ylabel('Vendas') #legenda eixo y
plt.axis([0,6,0,max(vendas_meses)+500]) #definir os limites dos eixos x e y
plt.title('Vendas por Meses') #titulo do grafico
plt.show() #exibir o grafico
