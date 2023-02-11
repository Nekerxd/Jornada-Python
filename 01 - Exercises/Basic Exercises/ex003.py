# Write a Python program to display the current date and time.

from datetime import datetime

hora = datetime.now()

print(hora.strftime("%H:%M:%S %d-%m-%Y"))