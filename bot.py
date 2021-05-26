import tweepy
import schedule
import time
from mensagens import Mensagens

KEY = "xH64CoAf3R787YzV7M0ymePOh"
S_KEY = "JpiZGn3KHp0B0x8Sdl66FxBf976f1AUhL5zL8pwJPK2QtOifIB"
TOKEN = "1395165522484998146-WTM2HoBrqGTZJimpY7LENn0hI329Ok"
TOKEN_S = "KFVReTFlGs9BV1TTej9eyFSonyFduRCyJAkiDiY9IvleL"

class Bot(Mensagens):   
    def __init__(self, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def publicar(self, mensagem):
        try:
            self.api.update_with_media(filename=mensagens.caminho_meme, )
        except:
            self.api.update_status(mensagem)

    def atualizar(self):
        mensagens = Mensagens()
        return mensagens

    def agendar(self):
        schedule.every().day.do(self.atualizar)
        schedule.every().day.at("18:00").do(self.publicar, mensagens.mensagem))
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    bot = Bot(KEY, S_KEY, TOKEN, TOKEN_S)
    bot.agendar()