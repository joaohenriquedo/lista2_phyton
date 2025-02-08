#escreva um programa que solicite um determinado numero de dias, em seguida exiba o quanto esses dias equivalem em horas minutos e segundos
dias = int (input("quantos dias voce deseja?"))
horas =(dias / 24)
min = (dias / 1440)
segundos = (dias / 86400)
print(dias, "dias", horas, "horas", min, "minutos", segundos, "segundos")