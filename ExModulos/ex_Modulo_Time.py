import time

#Exercicio 1 - Contagem regreciva começando em 10

for i in range(10,0,-1):
    print(i, end=" \r") #o \r faz o cursor voltar para o início da linha sem pular linha na contagem regressiva
    time.sleep(1)



#Exercicio 2 - Formatação de tempo

import locale #importa a biblioteca locale que serve para trabalhar com localidade
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8') #configura a localidade para português do Brasil
data_hora=time.strftime('%A: %d de %B de %Y hora: %H:%M:%S')#formata a data e hora para o formato dia da semana, dia do mes, ano atual, e hora:minutos:segundos

print(data_hora)

#Exercicio 3 - Tempo ate o proximo ano

tempo_atual=time.localtime() #pega o tempo atual
tempo_ano_novo=(tempo_atual.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, -1) #define o tempo do próximo ano
segundos_ate_ano_novo=time.mktime(tempo_ano_novo) - time.mktime(tempo_atual) #calcula a diferença em segundos entre o tempo atual e o próximo ano
segundos_ate_ano_novo=int(segundos_ate_ano_novo) #converte o resultado para inteiro

print(f'Faltam {segundos_ate_ano_novo} segundos para o próximo ano.')
segundos_por_minuto=60
segundos_por_hora=60*60
segundos_por_dia=24*3600

dias ,resto_segundos=divmod(segundos_ate_ano_novo,segundos_por_dia)
horas,resto_segundos=divmod(resto_segundos,segundos_por_hora)
minutos,segundos=divmod(resto_segundos,segundos_por_minuto)

print(f"Na conversão, são {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para 2026.")