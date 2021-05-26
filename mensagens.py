import os
import datetime


class Mensagens:
    _tweet = {}
    def __init__(self):
        _caminho_da_imagem_de_hoje = None
        _dia_do_tweet = 0
        _nome_do_arquivo = None
        
        self.hoje()
        self.caminho_meme(_dia_do_tweet)
        self.mensagem(_nome_do_arquivo)

    @property
    def tweet(self):
        return Mensagens._tweet[int(self._dia_do_tweet)]
    
    @tweet.setter
    def tweet(self, novo_tweet):
        Mensagens._tweet = dict(novo_tweet)
    
    @property
    def caminho_da_imagem_de_hoje(self):
        return self._caminho_da_imagem_de_hoje
    
    @property
    def dia_do_tweet(self):
        return self._dia_do_tweet
    
    @property
    def nome_do_arquivo(self):
        return self._nome_do_arquivo
    
    def hoje(self):
        dia_hoje = datetime.datetime.now()
        dia_de_hoje = dia_hoje.strftime("%d")
        self._dia_do_tweet = dia_de_hoje
    
    def caminho_meme(self, dia):
        caminho_imagens = os.path.join(os.getcwd() + '/imagens')
        lista_imagens = os.listdir(caminho_imagens)
        nome_do_arquivo_da_imagem_de_hoje = lista_imagens[int(dia)]
        self._nome_do_arquivo = nome_do_arquivo_da_imagem_de_hoje
        self._caminho_da_imagem_de_hoje = caminho_imagens + nome_do_arquivo_da_imagem_de_hoje
  
    def mensagem(self, caminho):
        return self.tweet({int(self._dia_do_tweet): str(caminho.split(".")[0])})

mensagens = Mensagens()


print(mensagens.get_dia_do_tweet)