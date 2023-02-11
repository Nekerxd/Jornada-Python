# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar


ano = int(input("Digite o ano desejado: "))
mes = int(input("Digite o número do mês desejado: "))

print(calendar.month(ano, mes))