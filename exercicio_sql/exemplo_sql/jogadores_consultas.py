# esse sqlalchemy é uma biblioteca (conjunto de arquivos .py)
# que está disponível porque você baixou,
# com o comando
# python -m pip install sqlalchemy==1.4.50

from sqlalchemy import create_engine
from sqlalchemy.sql import text

#eu nao estou usando um servidor, como MySQL,
#ou postgres.
#estou usando essa biblioteca sqlite3, 
#que cria meu banco de dados em um arquivo.
#tanto que eu posso mandar esse arquivo para o site
#sqliteonline.com e todos os dados estão lá

engine = create_engine('sqlite:///rpg.db') #abre esse arquivo como se fosse um banco de dados
                                           # o arquivo no caso é rpg.db, da pasta atual

# se fosse para usar outro banco, a URL seria mais complexa
# sqlalchemy.create_engine("mysql://root:123456@localhost:3306/aula")
# bancodedados://usuario:senha@nomedamaquina:porta/nome_do_banco_de_dados

# Isso cria um erro personalizado (uma Exception)
# Como o KeyError de um dicionário
class JogadorNaoExisteException(Exception):
    pass # é só pass mesmo, pode deixar assim

def consultar_jogador(id_j):
    with engine.connect() as con:  #conecta no meu banco de dados
        #vou montar uma query, mas com um "buraco" chamado jogador
        statement = text ("""SELECT * FROM Jogador WHERE id = :jogador""") 
        # :jogador -> buraco que vai ser preenchido depois, parte da query
        # que varia de uma chamada da função pra outra
        # :jogador -> repare no ":", que marca o buraco. 
        # Sem ":" nao tem buraco, a query não vai conseguir usar dados externos
        
        rs = con.execute(statement, jogador=id_j) #preenchi o buraco :jogador
        # com esse comando jogador=id_j
        
        # rs representa o resultado de ter rodado a query
        jogadores = rs.fetchall()                 #pega todos os resultados numa lista
        if jogadores == []:                       #se nao tinha nenhuma linha
            raise JogadorNaoExisteException       #exibe um erro
        

        # se não, converte o primeiro elemento da lista para um dicionário
        # ele era um objeto (tipo de variável) da biblioteca sqlalchemy,
        # mas a gente não quer se preocupar com isso
        d = dict(jogadores[0])                 #converte o jogador para dicionário
        return d
        




def conta_jogadores():
    with engine.connect() as con:    
        statement = text ("""SELECT * FROM Jogador""") #todos os jogadores
        rs = con.execute(statement) 
        jogadores = len(rs.fetchall()) 
        return jogadores


