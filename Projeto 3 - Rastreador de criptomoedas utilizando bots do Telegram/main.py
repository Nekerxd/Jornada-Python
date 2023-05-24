from datetime import datetime
from time import sleep
import telegram
import requests
import asyncio
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

async def main():
    bot = telegram.Bot(token='')
    async with bot:
        await bot.send_message(text=mensagem, chat_id=1609972757, parse_mode=telegram.constants.ParseMode.MARKDOWN)

URL_BASE = 'https://api.coingecko.com/api/v3'
ENDPOINT_PING = f'{URL_BASE}/ping'
ENDPOINT_PRECOS = f'{URL_BASE}/simple/price'

while True:
    resposta = requests.get(ENDPOINT_PING)

    if resposta.status_code == 200:
        url = f'{ENDPOINT_PRECOS}?ids=ethereum&vs_currencies=BRL&include_last_updated_at=true'
        
        resposta = requests.get(url).json()
        
        dados_moeda = resposta.get('ethereum', None)
        preco = dados_moeda.get('brl', None)
        atualizado_em = dados_moeda.get('last_updated_at', None)
        
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        
        mensagem = None
        
        if preco < 8900:
            mensagem = f'*Cotação do Ethereum*: \n\tR$ {preco}\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor menor que o mínimo.'
        elif preco > 9000:
            mensagem = f'*Cotação do Ethereum*: \n\tR$ {preco}\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor maior que o máximo.'
        
        if mensagem:
            asyncio.run(main())
    
    else:
        print('API Offline, tente novamente mais tarde!')
    
    sleep(300)

