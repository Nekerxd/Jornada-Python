import requests
import telegram

class CoinGeckoAPI:
    def __init__(self, url_base: str):
        self.url_base = url_base
        
    def ping(self) -> bool:
        url = f'{self.url_base}/ping'
        return requests.get(url).status_code == 200
    
    def consulta_preco(self, id_moeda: str) -> tuple:
        url = f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=BRL&include_last_updated_at=true'
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados_moeda = resposta.json().get(id_moeda, None)
            preco = dados_moeda.get('brl', None)
            atualizado_em = dados_moeda.get('last_updated_at', None)
            return preco, atualizado_em
            
        else:
            raise ValueError("Código de resposta diferente de HTTP 200 OK")



class TelegramBot:
    def __init__(self, token: str, chat_id: int):
        self.token = token
        self.chat_id = chat_id     
            
    async def envia_mensagem(self, texto_markdown: str):
        self.bot = telegram.Bot(self.token)
        async with self.bot:
            await self.bot.send_message(text=texto_markdown, chat_id=self.chat_id, parse_mode=telegram.constants.ParseMode.MARKDOWN)
