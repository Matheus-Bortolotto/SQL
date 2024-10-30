# OPCIONAL - só precisa ler daqui pra baixo depois de passar *todos* os testes
# do RPG

# fetchall é perigoso. 
# Monta uma lista com todas as linhas que vieram da query. 
# Pode encher a sua RAM (se o banco for grande)

# Alternativa ? fetchone: pega o "próximo" jogador, e retorna None
# se não tem mais nenhum

def conta_jogadores2(): #IGNORE ESSA FUNCAO ATE TER TERMINADO O EXERCICIO
    # ELA DESCREVE ALGO OPCIONAL, PRA VOCE ESTUDAR DEPOIS DE PASSAR 
    # TODOS OS TESTES
    with engine.connect() as con:    
        statement = text ("""SELECT * FROM Jogador""") #todos os jogadores
        rs = con.execute(statement) 
        jogadores = 0
        while (rs.fetchone() != None): # Pego um jogador. Uma linha do resultado. 
                                       # Se acabaram os jogadores, vou receber um None
            jogadores += 1
        return jogadores

#fetch one
#pega  um

#fetch all
#pega todos

#fetch many
#pega muitos

def consultar_jogador2(id_j): #IGNORE ESSA FUNCAO ATE TER TERMINADO O EXERCICIO
    # ELA DESCREVE ALGO OPCIONAL, PRA VOCE ESTUDAR DEPOIS DE PASSAR 
    # TODOS OS TESTES
    with engine.connect() as con:  #conecta no meu banco de dados
        #query com "buraco" com o nome jogador    
        statement = text ("""SELECT * FROM Jogador WHERE id = :jogador""") 
        # :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
        # :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        
        rs = con.execute(statement, jogador=id_j) #e usei esse buraco
        jogador = rs.fetchone()                   #pega a primeira linha do resultado
        if jogador == None:                       #se nao tinha nenhuma linha, 
                                                  #jogador vale None
                                                  # (None tb aparece quando a gente
                                                  # já leu várias linhas e acabou 
                                                  # a consulta)
            raise JogadorNaoExisteException
        return dict(jogador)                      #converte o jogador para dicionário

def jogador_por_email(email): #IGNORE ESSA FUNCAO ATE TER TERMINADO O EXERCICIO
    # ELA DESCREVE ALGO OPCIONAL, PRA VOCE ESTUDAR DEPOIS DE PASSAR 
    # TODOS OS TESTES
    with engine.connect() as con:   #conecta e depois desconecta automaticamente :) 
        statement = text ("""SELECT * FROM Jogador WHERE email = :email""")
        rs = con.execute(statement, email=email) 
        jogador = rs.fetchone() 
        if jogador == None: 
            raise JogadorNaoExisteException
        return dict(jogador) 