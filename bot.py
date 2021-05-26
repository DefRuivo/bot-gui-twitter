import tweepy
import schedule
import time
import os
from mensagens import Mensagens
from dotenv import load_dotenv, find_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ.get("KEY")
S_KEY = os.environ.get("S_KEY")
TOKEN = os.environ.get("TOKEN")
TOKEN_S = os.environ.get("TOKEN_S")

class Bot(Mensagens):   
    def __init__(self, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
    
    def publicar(self, mensagem, nome_do_arquivo):
        try:
            self.api.update_with_media(filename=nome_do_arquivo, status=mensagem )
        except:
            self.api.update_status(mensagem)


    def agendar(self):
        schedule.every().day.at("18:00").do(job_func=self.publicar, mensagem=Mensagens().tweet, nome_do_arquivo=Mensagens().caminho_da_imagem_de_hoje)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    bot = Bot(KEY, S_KEY, TOKEN, TOKEN_S)
    bot.agendar()