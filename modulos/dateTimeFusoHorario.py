import zoneinfo
from datetime import datetime

fuso_horario_sp=zoneinfo.ZoneInfo('America/sao_paulo') #define o fuso horário do Acre
data_hora_sp=datetime.now(fuso_horario_sp) #pega a data e hora atual do Acre
print(f'Data e hora no rj: {data_hora_sp.strftime("%d/%m/%Y %H:%M:%S")}') #formata a data e hora do Acre
