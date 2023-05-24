from classes import CoinGeckoAPI, TelegramBot
from datetime import datetime
from time import sleep
import locale
import asyncio

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')

# Inserir token de acesso bot Telegram e ID do chat utilizado.
bot = TelegramBot(token='', chat_id=None)

while True:
    if api.ping():
        preco, atualizado_em = api.consulta_preco(id_moeda='ethereum')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None
        
        if preco < 8900:
            mensagem = f'*Cotação do Ethereum*: \n\tR$ {preco}\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor menor que o mínimo.'
        elif preco > 9000:
            mensagem = f'*Cotação do Ethereum*: \n\tR$ {preco}\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor maior que o máximo.'
        
        if mensagem:
            asyncio.run(bot.envia_mensagem(texto_markdown=mensagem))
    
    else:
        print('API Offline, tente novamente mais tarde!')
    
    sleep(300)
