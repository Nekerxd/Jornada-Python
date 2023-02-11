# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)

from datetime import date

data1 = date(2001, 2, 16)
data2 = date(2022, 12, 14)
periodo = data2 - data1

print(periodo.days)