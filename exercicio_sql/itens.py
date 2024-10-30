#Não se esqueca de dar os imports! Eu não fiz pra vc!
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db') 

#isso daqui a gente vai usar pra dar raise quando um item nao existir
class ItemNaoExisteException(Exception):
    pass #pode deixar só pass mesmo. Criamos uma classe nova, igualzinha a Exception
#mas com outro nome.


def consultar_item(id_i):
     with engine.connect() as con:
        statement = text ("""SELECT * FROM Item WHERE id = :item""")
       
        rs = con.execute(statement, item=id_i)
       
        itens = rs.fetchall()  
        if itens == []:      
            raise ItemNaoExisteException
        return dict(itens[0])
