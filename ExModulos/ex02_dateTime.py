from datetime import datetime, timedelta
import locale
import time

locale.setlocale(locale.LC_ALL, 'pt_br.utf-8')

    #EX 1 - Oferecendo desconto para cliente com base na ultima compra


ultima_compra = datetime(2025,8,10) # Exemplo de data da última compra

data_hora_atual= datetime.now() # Data e hora atual
diferenca = data_hora_atual - ultima_compra # Calcula a diferença entre as datas

if diferenca > timedelta(days=30): # Verifica se a diferença é maior que 30 dias
    print("Cliente elegível para desconto")
else:
    print("Cliente não elegível para desconto")
    
    
    # EX 2 - data e hora em diferentes fusos horários

from datetime import datetime
import zoneinfo
data_hora_agora= datetime.now() 

fuso_sp = zoneinfo.ZoneInfo("America/Sao_Paulo") #definir o fuso horário de São Paulo e as outras cidades
fuso_ny= zoneinfo.ZoneInfo("America/New_York")
fuso_japao= zoneinfo.ZoneInfo("Asia/Tokyo")

data_hora_sp = data_hora_agora.astimezone(fuso_sp) #converter a data e hora atual para o fuso horário de São Paulo
data_hr_ny= data_hora_agora.astimezone(fuso_ny)
data_hr_japao= data_hora_agora.astimezone(fuso_japao)

def verificar_horario(data_hora): #função para verificar se o escritório está aberto ou fechado com base no horário local
    if data_hora.hour > 9 and data_hora.hour<17: # verifica se a hora está entre 9 e 17
        return 'aberto' #considerando o horário comercial das 9 as 17 horas
    else:
        return 'fechado' 
        
print(f'escritorio de sp astá: {verificar_horario(data_hora_sp)}')
print(f'escritorio de ny astá: {verificar_horario(data_hr_ny)}')
print(f'escritorio do japão astá: {verificar_horario(data_hr_japao)}')


    #EX 3 - Calculando idade com base na data de nascimento

data_nascimmento= input('Digite sua data de nascimento:')
data_nascimmento=datetime.strptime(data_nascimmento, '%d/%m/%Y') #converte a string para um objeto datetime usando o formato dia/mes/ano e os codigos speciais do strptime %d/%m/%Y
data_atual= datetime.now()

idade= data_atual.year - data_nascimmento.year #calcula a idade com base no ano atual e o ano de nascimento usando a propriedade year
mes_atual= data_atual.month
dia_atual= data_atual.day
mes_nascimento= data_nascimmento.month #pega o mês de nascimento
dia_nascimento=data_nascimmento.day #pega o dia do mês de nascimento

if mes_nascimento>mes_atual: #se o mês de nascimento for maior que o mês atual, subtrai 1 da idade
    idade-=1
elif mes_nascimento == mes_atual: #se o mês de nascimento for igual ao mês atual, verifica o dia
    if dia_nascimento > dia_atual: #se o dia de nascimento for maior que o dia atual, subtrai 1 da idade
        idade-=1  
    

print(idade)
        