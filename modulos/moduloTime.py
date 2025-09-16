import time #importa a biblioteca time que serve para trabalhar com tempo
import locale#importa a biblioteca locale que serve para trabalhar com localidade
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')#configura a localidade para português do Brasil

data=time.strftime("%d/%m/%Y")#formata a data para o formato dia/mes/ano
data_pt=time.strftime("%A, %d de %B de %Y") #formata a data para o formato dia/mes/ano e dia da semana, dia de mes de ano em português
dia=time.strftime("%A")
hora=time.strftime("%H:%M:%S")#formata a hora para o formato horas:minutos:segundos
print(data,data_pt, hora)
