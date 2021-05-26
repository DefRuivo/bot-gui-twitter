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
        self.atualizar_tweets()

    @property
    def tweet(self):
        return Mensagens._tweet[int(self._dia_do_tweet)]
    
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
        caminho_imagens = os.path.join(os.getcwd() + '/imagens/')
        lista_imagens = os.listdir(caminho_imagens)
        nome_do_arquivo_da_imagem_de_hoje = lista_imagens[int(dia)]
        self._nome_do_arquivo = nome_do_arquivo_da_imagem_de_hoje
        self._caminho_da_imagem_de_hoje = caminho_imagens + nome_do_arquivo_da_imagem_de_hoje

    def tratar_nome_arquivo(self):
        nome = self._nome_do_arquivo.split(".")[0]
        return nome.replace("  ", "\n")
    
    def atualizar_tweets(self):
        caminho_imagens = os.path.join(os.getcwd() + '/imagens')
        lista_imagens = os.listdir(caminho_imagens)
        tweet_tratado = self.tratar_nome_arquivo()
        for len_imagem in range(len(lista_imagens)):
            Mensagens._tweet[len_imagem] = tweet_tratado