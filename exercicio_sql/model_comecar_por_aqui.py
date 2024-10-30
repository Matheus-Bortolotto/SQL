

'''

1) Examine o banco de dados no site https://sqliteonline.com/.
O arquivo é rpg.db, e você pode subir ele ao site
usando file > opendb. Note que há 4 tabelas diferentes
(veja no canto superior direito).

Depois de subir, pode fazer varias consultas para se familiarizar 
com as tabelas: select * from jogador;
select * from Heroi; select * from Item; select * from ItemDoHeroi

2) rode "python -m pip install sqlalchemy==1.4.50" no cmd 
para poder usar os arquivos fornecidos. Isso vai instalar a biblioteca sqlalchemy

3) Examine as funcoes do arquivo exemplo_sql/jogador_consultas.py, 
que ilustra como 
podemos usar o sql no python com sqlite. Pode deixar os demais arquivos
do diretório exemplo_sql/ para depois

4) Sobre o sqlite:
    Voce deve manipular e consultar apenas o arquivo rpg.db
    Jamais manipule o arquivo rpg.original.db no seu programa,
    pois ele serve para termos um ponto de partida confiavel
    para os testes

    Voce nao deve enviar os arquivos sqlite se for 
    submeter esse trabalho para avaliação

5) Seu ponto de partida é esse arquivo model. Ele pedirá que você crie funções,
tanto nele quanto nos outros arquivos, e será com ele que voce rodará os testes
'''



'''
já temos um arquivo herois, que foi importado
abaixo
'''
from herois import HeroiNaoExisteException
import herois

'''
Parte 1: Consultas

Se familiarize com as tabelas "Heroi" e "Item", pois 
vamos fazer diversas consultas com elas. 
(veja o item 1 da introdução para saber como)

Então, comece os exercícios abaixo
'''

'''
Ex1

O arquivo herois deve conter uma função heroi_existe
Ela recebe uma id de herói e consulta no banco para ver
se o herói em questão existe. Ela retorna True
se ele existe, False caso contrário

Rode o arquivo runtests_rpg.py pra ver se está tudo certo
'''
'''
Ex2

O arquivo herois deve conter uma funcao 
consultar_heroi.
ela recebe uma id de heroi e retorna 
um dicionario com todos os dados do heroi
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma HeroiNaoExisteException 

Rode o arquivo runtests_rpg.py pra ver se está tudo certo
(isso vai ser verdade pra todos os exercicios, vou parar de falar)
'''

'''
Já existe um arquivo itens.py,
que está importado abaixo

'''
from itens import ItemNaoExisteException
import itens

'''
Ex3
O arquivo itens.py
deve conter uma funcao consultar_item.
ela recebe uma id de item e retorna 
um dicionario com todos os dados do item
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma ItemNaoExisteException (que voce deverá
criar)

(já fizemos coisa parecida no heroi!)
'''

'''
Ex4a 
No arquivo heroi, crie uma funcao consultar_heroi_por_nome 
que recebe um nome de heroi
e retorna um dicionario com os dados desse heroi.
'''

'''
Ex 4b (na real não vamos fazer nada nele, ele já está pronto
abaixo)

No arquivo model, crie uma funcao heroi_pronto_por_nome 
que recebe um nome de heroi
e retorna um dicionario com os dados desse heroi.

'''
def heroi_pronto_por_nome(nomeHeroi):
    heroi = herois.consultar_heroi_por_nome(nomeHeroi)
    return heroi
'''
Ex5
Melhore sua funcao heroi_pronto_por_nome. Agora, o dicionario também
incluirá o a chave vida. O valor da vida de um heroi é inicializado
com seu fisico multiplicado por 10
'''

'''
Ex06 (ainda no model.py)
Chegou a hora de fazer um ataque!

A função atacar_com_fisico recebe dois dicionarios, de dois herois. 
(esses dicionarios sao os gerados pela funcao heroi_pronto_por_nome
mas, você não precisa chamar a função. Eu mesmo chamo lá no teste
e já te passo os dicionários)

O primeiro heroi é o atacante e o segundo é o defensor

O defensor perde vida. A perda é igual ao atributo fisico do atacante.

O retorno não importa, o que importa é alterar o dicionario do defensor

Repare que a funcao recebe dicionários, e nem fala com o SQL
'''

def atacar_com_fisico(atacante, defensor):
   pass




'''
Opcional - não testado

Se você quiser, pode usar a funcao mensagem_de_ataque_fisico para
dar uns prints simpaticos avisando quanto de dano o defensor tomou.

A função mensagem_de_ataque_fisico já está definida, mais abaixo, 
mas você pode trocar as
mensagens de ataque por coisas mais interessantes, se quiser.

Esses prints nao serão corrigidos, é só pela diversão mesmo
'''


'''
Ex07 (ainda no arquivo model)
A função atacar_com_magia faz o mesmo, mas agora o dano que o defensor sofre é igual 
ao atributo magia do atacante.

Repare que a vida nunca pode ficar negativa. O mínimo é 0. 
Se o defensor tinha 15 de vida e toma 30 de dano, ele fica com a vida 0,
não com a vida -15.

(fazer a funcao abaixo) - ela recebe dicionarios e nem fala com o sql
'''


def atacar_com_magia(atacante, defensor):
    pass

    


'''
Ok, que papo é esse dos arquivos?
Porque temos um arquivo model e os arquivos herois e itens?
Porque usamos o banco de dados no arquivo herois, no arquivo itens,
mas não no arquivo model?

https://pt.wikipedia.org/wiki/Objeto_de_acesso_a_dados

Estamos separando claramente a lógica (por exemplo, da briga)
e os dados que são salvos no banco de dados.

A idéia é ter arquivos que *só falam* com o banco de dados, e não
implementam mais nada, e arquivos que *não falam* com banco de dados,
mas implementam outras funções lógicas (validação de dados, criação
de dados que não são salvos no banco,)
'''


'''
Parte 2: Consultas mais complexas

Temos um terceiro arquivo de acesso ao banco, 
chamado itens_do_heroi. Ele está importado
abaixo

Ele representa um relacionamento "many to many", de muitos para muitos.
Diz quais herois tem quais itens, permitindo a um heroi ter vários items
e a um item ser possuído por vários herois

Verifique e se familiarize com a tabela ItemDoHeroi do banco de dados
'''
import itens_do_heroi

'''
Ex100
No arquivo itens_do_heroi, crie uma funçao heroi_tem_item.

Ela recebe uma id de heroi, e retorna True se o heroi
possui algum item, false caso contrário

Um heroi 10 tem o item 15 se na tabela itemDoHeroi
temos uma linha com idItem 15 e idHeroi 10
'''

'''
Ex101
No arquivo itens_do_heroi,
crie uma função heroi_quantos_itens, que recebe uma
id de heroi e diz quantos itens ele possui
'''

'''
Ex102a e Ex102b

No arquivo itens_do_heroi,
crie uma funcao itens_do_heroi

Ela recebe a id do heroi e devolve uma lista com dicionarios, um para cada item dele.

Cada dicionário descreve um item 

Por exemplo, se o heroi 3 tem uma varinha com 2 de magia:

Chamar itens_do_heroi.itens_do_heroi(3) vai devolver a lista de dicionarios. Um desses dicionarios vai representar a varinha: ter chaves "tipo" com valor "varinha" e chave "magia" com valor 2


Dica: é possivel fazer com duas consultas, usando
o python para fazer o meio de campo, mas é mais
interessante e rápido usar um join
'''


'''
Ex103
Agora, criemos uma nova função, que lista apenas os itens em uso. Essa função será criada no arquivo model, 
onde você está agora

Um item está em uso quando o valor da coluna emUso é 1.
Se for 0, o heroi tem o item mas não está usando.

A assinatura da função será:
def lista_itens_em_uso_do_heroi(idHeroi):

Voce já pegou todos os dados necessários 
do banco. Usando as funcoes que já definiu, nao precisará
fazer acessos a mais
'''
def lista_itens_em_uso_do_heroi(idHeroi):
    pass


'''
Ex104a e 104b
Funcao itens_em_uso_por_nome_do_heroi
Crie essa função no arquivo itens_do_heroi

Ela recebe uma string (o nome do heroi) e devolve uma lista (com os itens em uso do heroi)

Cada item é um dicionário descrevendo o item

Recomendo usar um join para fazer a consulta.
'''


'''
Ex105a e Ex105b
Melhore sua função heroi_pronto_por_nome: agora, os o dicionario que representa o heroi é alterado pelos itens em uso. 

Se o heroi está usando um item que aumenta
suas habilidades, as habilidades que aparecem no dicionario serão
as do heroi, aumentadas de acordo com o item

Por exemplo, considere um heroi com agilidade 2 e usando 
um item de agilidade 3. Para ele, o dicionario devera 
reportar agilidade 5 

repare, porem, que o item tem que ser do heroi e estar
em uso para fazer efeito

(fazer a funcao nesse arquivo - na verdade, melhorar a função
que já existe)

Se for o caso, altere a vida do heroi adequadamente! (isso é o Ex105b)
'''
'''
Ex106
Façamos um upgrade nas duas funções de ataque. Agora, se o atacante
for muito mais rápido que o defensor, poderá atacar mais vezes

Para isso, divida agilidade do atacante pela agilidade do defensor,
arredondando para baixo.

Se der algum número maior que 1, esse é o número de ataques
que o atacante vai conseguir fazer.

Se der 1 ou menos, o atacante conseguirá fazer exatamente 1 ataque.

Fazer um ataque 2 vezes significa dar duas vezes o dano:
Se harry tem 7 de magia e vai atacar 2 vezes, dará 14 de dano
'''

'''
Parte 3: Editar os valores do banco de dados

Agora você já conhece todos os arquivos, é hora de criar herois e heroinas

Para aprender a criar registros no banco de dados, devemos consultar o 
arquivo jogadores_editar.py na pasta exemplo_sql
'''

'''
Ex200 (sim, pulamos alguns numeros)

Nesse arquivo, faça uma funcao criar heroi, que recebe
o nome e os atributos:

def criar_heroi(nome,agilidade,fisico,magia):

Ela deve criar um heroi no banco de dados, com os atributos
dados.

Para isso, ela deve chamar uma funcao no arquivo heroi.py. Essa funcao no heroi.py fará o acesso ao banco de dados
'''

def criar_heroi(nome,agilidade,fisico,magia):
    pass

'''
Ex201
Façamos um upgrade em criar_heroi. Se o heroi for poderoso
demais (a soma dos 3 atributos for maior que 20) nossa funcao
criar_heroi devera lançar uma OverpowerException

(fazer a funcao nesse arquivo. Na verdade, se trata de um upgrade de criar_heroi)

(Você também deve criar a excessao nesse arquivo)
'''

'''
Ex202
No arquivo itens.py crie uma funcao nome_para_id_item, que recebe
um nome de item e devolve a id numerica correspondente

(esse arquivo ja foi importado acima)
'''

'''
Ex203
no arquivo itens.py, crie uma funcao criar_item, que recebe os atributos
do item e cria um item novo no banco de dados.

Ou seja, uma funcao com a seguinte assinatura:
criar_item(tipo, nome,fisico,agilidade,magia)
'''


'''
Ex204 -- repare que voce precisa de duas funcoes para passar esse teste!

Crie uma funcao dar_item_para_heroi, que faz com que o heroi se
torne o dono (ou dona) do item. Ela recebe dois dicionarios:
um do heroi e um do item.

Para dar o item ao heroi, sua função deve 
chamar uma funcao no arquivo itens_do_heroi,
que você também deverá criar. No itens_do_heroi, você
adicionará uma linha nova, marcando que o item pertence
ao heroi. 

Lembre-se de manter o codigo sql apenas no arquivo itens_do_heroi

Alem dessa funcao, para passar o teste relevante, voce precisara
tambem do proximo exercicio (colocar_item_em_uso)
'''
def dar_item_para_heroi(heroi,item):
    pass



'''
Ex204 -- essa é a segunda função necessária para passar o ex 204
Crie uma funcao colocar_item_em_uso, que recebe o dicionario do
heroi e o dicionario do item, e faz com que o item fique emUso

Para isso, voce deve criar uma funcao no arquivo itens para a manipulacao
do SQL
'''
class HeroiJaUsaEsseTipoDeItemException(Exception):
    pass

def colocar_item_em_uso(heroi,item):
    pass




'''
Ex205
Façamos um upgrade em colocar_item_em_uso: um item só pode ficar em 
uso se o heroi nao está usando outro item do mesmo tipo

Se tentarmos colocar_item_em_uso em um chapeu quando o heroi já
tem um chapeu em uso, a funcao deve lancar 
o erro HeroiJaUsaEsseTipoDeItemException
'''

'''
Voce terminou a atividade!

Agora, pode fazer tres coisas:
    * primeiro, experimentar os prints abaixo
    * depois, verificar nos exemplos o uso do fetchOne em vez do fetchall, e tentar adaptar algumas
 funcoes para usar o fetchOne. Isso dá um trabalhinho a mais,
    mas deixa seu código mais robusto (explicacao no jogadores_consultas)
    * crie um teste você mesmo
    * crie um teste você mesmo, em que o usuário adicione o mesmo item para dois herois diferentes. 
Qual caracteristica do banco de dados nos permite fazer isso?
    * terceiro: criar uma nova tabela,de ataques personalizados
    por exemplo "merlin sufoca harry com a sua barba" e
    "hulk esmaga conan". um heroi poderá ter um ou mais
    ataques personalizados, e deverá usar eles em vez/misturados
    com os genericos (como você preferir, porque isso nao
    será testado)
'''

'''
O uso das funcoes a seguir é opcional
'''

fazer_prints = False

import random
def mensagem_de_ataque_fisico(dano,nome_atacante,nome_defensor):
    msgs = [f'{nome_atacante} dá um soco em {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} dá um chute em {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} ataca {nome_defensor} covardemente, causando {dano} de dano']
    msg = msgs[random.randrange(0,len(msgs)-1)]
    if fazer_prints:
        print(msg)

def mensagem_de_ataque_magico(dano,nome_atacante,nome_defensor):
    msgs = [f'{nome_atacante} solta raios contra {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} congela {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} transforma {nome_defensor} em um flamingo, causando {dano} de dano']
    msg = msgs[random.randrange(0,len(msgs)-1)]
    if fazer_prints:
        print(msg)

def luta(atacante,defensor):
    while (atacante['vida'] != 0 and defensor['vida'] != 0):
        if atacante['magia'] > atacante['fisico']:
            atacar_com_magia(atacante,defensor)
        else:
            atacar_com_fisico(atacante,defensor)
        print(f'Agora, {defensor["nome"]} tem {defensor["vida"]} de vida')
        atacante,defensor = defensor,atacante #inverte

def merlin_versus_harry():
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        luta(merlin,harry)

assert 'create_engine' not in locals() #não devemos usar o sql no arquivo model!
assert 'sqlalchemy' not in locals() #não devemos usar o sql no arquivo model!
