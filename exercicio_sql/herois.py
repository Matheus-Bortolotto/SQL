from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db') 

# Essa classe só representa uma exception com
# novo nome. Não mexa dentro dela.
# Escreva suas funcoes depois dela
class HeroiNaoExisteException(Exception):
    pass #pode deixar só pass mesmo


def heroi_existe(id_h):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""")
       
        rs = con.execute(statement, heroi=id_h)
       
        herois = rs.fetchall()  
        if herois == []:      
            return False
        return True


def consultar_heroi(id_h):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""")
       
        rs = con.execute(statement, heroi=id_h)
       
        herois = rs.fetchall()  
        if herois == []:      
            raise HeroiNaoExisteException 
        return dict(herois[0])


def consultar_heroi_por_nome(nome_h):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM Heroi WHERE nome = :heroi""")
       
        rs = con.execute(statement, heroi=nome_h)
       
        herois = rs.fetchall()  
        if herois == []:      
            raise HeroiNaoExisteException 
        return dict(herois[0])

#pode ignorar a partir daqui
import sqlalchemy
assert (sqlalchemy.__version__ == '1.4.50') #se houver erro nesse assert, reveja as instrucoes de instalacao
