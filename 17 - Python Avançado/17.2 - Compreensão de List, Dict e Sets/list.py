emails = [
    ',henRy@gmail.com',
    ' ,juLIa@hotmail.com',
    'ivaN@gmail.com ',
    'mar,coS@yahoo.com.br',
    '   SandovAL@hotmail.com',
    'IVANA@gmail.com',
    'ItamaR@edu.gov.br'
]

emails_tratados = [email.strip().replace(",", "").lower() for email in emails]
emails_tratados_gmail = [email.strip().replace(",", "").lower() for email in emails if "@gmail" in email]

print(f'Emails tratados: {emails_tratados}')
print(f'Emails tratados com gmail: {emails_tratados_gmail}')

# Múltiplos comuns de 4 e 5 de 0 até 500

resultado = [numero for numero in range(0, 501) if numero % 4 == 0 if numero % 5 == 0]

print(resultado)