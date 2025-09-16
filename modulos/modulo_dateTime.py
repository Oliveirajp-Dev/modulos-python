from datetime import datetime  #importa a classe datetime do módulo datetime
from datetime import date #importa a classe date do módulo datetime
from datetime import timedelta #diferença entre datas
import zoneinfo #fuso horário
import locale #importa o módulo locale para definir a localidade


locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8') #define a localidade para português do Brasil com LC_ALL para todas as categorias
agora=datetime.now()#pega a data e hora atual
print(agora)
data=agora.date()#pega só a data
print(data)
hoje=date.today()
print(hoje)
dia=hoje.day
print(dia)

data_futura=hoje+timedelta(days=365) #adiciona 365 dias a data atual
print(data_futura)
data_passada=hoje-timedelta(days=365) #subtrai 365 dias da data atual
print(data_passada)

data=[
    datetime(2023,12,25),
    datetime(2024,1,1), 
    datetime(2024,7,4),
    datetime(2024,11,28),
    datetime(2025,8,25)
]

for datas in data:
    print(datas.strftime('%d/%m/%Y')) #formata a data no formato dia/mes/ano
    print(datas.strftime('%A')) #dia da semana por extenso
    print(datas.date()) #pega só a data
    
fuso_horario_acre=zoneinfo.ZoneInfo('America/Rio_Branco') #define o fuso horário do Acre
data_hora_acre=datetime.now(fuso_horario_acre) #pega a data e hora atual do Acre
print(f'Data e hora no Acre: {data_hora_acre.strftime("%d/%m/%Y %H:%M:%S")}') #formata a data e hora do Acre