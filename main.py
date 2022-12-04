hora_inicial = int(input('Hora inicial: '))
minuto_inicial = int(input('Minuto inicial: '))
hora_final = int(input('Hora final: '))
minuto_final = int(input('Minuto final: '))

minuto_inicial += hora_inicial*60
minuto_final += hora_final*60

tempo = minuto_final - minuto_inicial

hora = tempo // 60
minuto = tempo % 60

print(f'O jogo durou {hora} horas e {minuto} minutos')
