from herois import HeroiNaoExisteException
import herois

from itens import ItemNaoExisteException
import itens
import itens_do_heroi

#from model_comecar_por_aqui import *
import model_comecar_por_aqui as model

'''
Fim das funcoes de uso opcional

Inicio dos testes
'''

import unittest
class TestStringMethods(unittest.TestCase):

    def test_ex01_heroi_existe(self):
        self.assertTrue(herois.heroi_existe(1))
        #    ----------  xxxxx oooooooooooo a
        #  no arquivo herois (xxxxx), tem que existir uma funcao
        # heroi existe (oooooooo), quando eu passar o argumento 1
        # para ela (a), a funcao tem que retornar verdadeiro
        # (---------)
        self.assertTrue(herois.heroi_existe(2))
        self.assertTrue(herois.heroi_existe(3))
        self.assertFalse(herois.heroi_existe(30))

    def test_ex02a_consultar_heroi(self):
        d = herois.consultar_heroi(1)
        self.assertTrue(type(d),dict) # herois.consultar_heroi tem que retornar dicionario


    def test_ex02b_consultar_heroi(self):
        self.assertEqual(herois.consultar_heroi(1)['nome'],'conan')
        self.assertEqual(herois.consultar_heroi(2)['nome'],'merlin')
        #    ooooooooooo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa xxxxxxxx
        #estou usando o assertEqual (ooooooo) para dizer que o lado
        # esquerdo (aaaaaaaaaa) tem que ser igual ao direito (xxxxxxx)
        self.assertEqual(herois.consultar_heroi(3)['nome'],'harry')
   
    def test_ex02c_consultar_heroi_invalido(self):
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,50329)
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,50)
        #                 xxxxxxxxxxxxxxxxxxxxxxx oooooooooooooooooooooo aa
        #diz que tem que ocorrer uma excessão (xxxxxx), quando eu chamar aa funcao (ooooooooooo) com a id 50 (aa)
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,450)

    def test_ex03a_consultar_item(self):
        d = itens.consultar_item(1)
        self.assertTrue(type(d),dict) # itens.consultar_item tem que retornar dicionario


    def test_ex03b_consultar_item(self):
        self.assertEqual(itens.consultar_item(1)['nome'],'forca do gigante')
        self.assertEqual(itens.consultar_item(1)['tipo'],'cinto')
        self.assertEqual(itens.consultar_item(2)['nome'],'de alladin')
        self.assertEqual(itens.consultar_item(2)['tipo'],'lampada')
        self.assertRaises(ItemNaoExisteException,itens.consultar_item,329)
    
    def test_ex04a_consultar_heroi_por_nome(self):
        self.assertEqual(herois.consultar_heroi_por_nome('conan')['fisico'],3)
        self.assertEqual(herois.consultar_heroi_por_nome('conan')['magia'],2)
        self.assertEqual(herois.consultar_heroi_por_nome('conan')['agilidade'],5)
        self.assertEqual(herois.consultar_heroi_por_nome('merlin')['fisico'],3)
        self.assertEqual(herois.consultar_heroi_por_nome('merlin')['agilidade'],1)
        self.assertEqual(herois.consultar_heroi_por_nome('merlin')['magia'],8)
        self.assertEqual(type(herois.consultar_heroi_por_nome('merlin')),dict,"herois.consultar_heroi_por_nome_tem_que_retornar um dicionario")
    
    def test_ex04b_heroi_pronto_por_nome(self):
        self.assertNotIn('vida',herois.consultar_heroi_por_nome('merlin'),"não é o a funcao herois.consultar_heroi_por_nome que acrescenta a vida, é a função model.heroi_pronto_por_nome")
        self.assertEqual(model.heroi_pronto_por_nome('conan')['fisico'],3)
        self.assertEqual(model.heroi_pronto_por_nome('conan')['magia'],2)
        self.assertEqual(model.heroi_pronto_por_nome('conan')['agilidade'],5)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['fisico'],3)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['agilidade'],1)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['magia'],8)
    
    def test_ex05_vida_do_heroi(self):
        self.assertEqual(model.heroi_pronto_por_nome('conan')['vida'],30)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['vida'],30)
    
    def test_ex06_ataque_fisico(self):
        conan = model.heroi_pronto_por_nome('conan')
        harry = model.heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'],20)
        model.atacar_com_fisico(atacante=conan,defensor=harry)
        #conan tem 3 de fisico, harry perdeu 3 de vida
        self.assertEqual(harry['vida'],17)
        model.atacar_com_fisico(atacante=conan,defensor=harry)
        self.assertEqual(harry['vida'],14)
        model.atacar_com_fisico(defensor=conan,atacante=harry)
        self.assertEqual(conan['vida'],28)

    def test_ex07_ataque_magico(self):
        merlin = model.heroi_pronto_por_nome('merlin')
        harry = model.heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'],20)
        model.atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],12)
        model.atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],4)
        model.atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],0)

    def test_ex100_heroi_tem_item(self):
        self.assertEqual(itens_do_heroi.heroi_tem_item(1),True)
        self.assertEqual(itens_do_heroi.heroi_tem_item(3),True)
        self.assertEqual(itens_do_heroi.heroi_tem_item(2),False)
    
    def test_ex101_heroi_quantos_itens(self):
        self.assertEqual(itens_do_heroi.heroi_quantos_itens(1),2)
        self.assertEqual(itens_do_heroi.heroi_quantos_itens(3),1)
        self.assertEqual(itens_do_heroi.heroi_quantos_itens(2),0)
    
    def test_ex102a_itens_do_heroi_acerta_quantidades(self):
        self.assertEqual(len(itens_do_heroi.itens_do_heroi(1)),2)
        self.assertEqual(len(itens_do_heroi.itens_do_heroi(3)),1)
        self.assertEqual(len(itens_do_heroi.itens_do_heroi(2)),0)

    
    def test_ex102b_itens_do_heroi(self):
        itens = itens_do_heroi.itens_do_heroi(1)
        lista_tipos = [itens[0]['tipo'],itens[1]['tipo']]
        self.assertIn('cinto',lista_tipos)
        self.assertIn('lampada',lista_tipos)

    


    def test_ex103_itens_que_heroi_esta_usando(self):
        self.assertEqual(len(model.lista_itens_em_uso_do_heroi(1)),0)
        self.assertEqual(len(model.lista_itens_em_uso_do_heroi(3)),1)
        self.assertEqual(len(model.lista_itens_em_uso_do_heroi(2)),0)
        item=model.lista_itens_em_uso_do_heroi(3)
        item_do_3 = item[0]
        self.assertEqual(item_do_3['tipo'],'varinha')

    def test_ex104a_itens_em_uso_por_nome_do_heroi(self):
        itens = itens_do_heroi.itens_em_uso_por_nome_do_heroi("conan")
        self.assertEqual(itens,[])
        itens = itens_do_heroi.itens_em_uso_por_nome_do_heroi("harry")
        self.assertEqual(len(itens),1)
        #varinha de duelo do harry é do tipo "varinha"
        self.assertEqual(itens[0]['tipo'],"varinha")
    
    def test_ex104b_itens_em_uso_por_nome_do_heroi_verifica_atributos(self):
        itens = itens_do_heroi.itens_em_uso_por_nome_do_heroi("harry")
        #varinha de duelo do harry tem 2 de magia. Cuidado! dependendo
        #de como você fez seu select, você poderá ver a magia do harry
        #no lugar da magia da varinha.
        #Seu select, em vez de usar SELECT * FROM, deve especificar
        #as colunas, para poder especificar a coluna Item.magia,
        #e evitar esse problema
        self.assertEqual(itens[0]['magia'],2,"há uma dica, leia o teste 104b")
        # e faça o mesmo para agilidade e fisico. Mostrar os atributos do
        # item, nao do personagem!
        self.assertEqual(itens[0]['agilidade'],1)
        self.assertEqual(itens[0]['fisico'],0)
    

    def test_ex105a_status_alterado_por_itens(self):
        self.assertEqual(model.heroi_pronto_por_nome('conan')['fisico'],3)
        self.assertEqual(model.heroi_pronto_por_nome('conan')['magia'],2)
        self.assertEqual(model.heroi_pronto_por_nome('conan')['agilidade'],5)
        self.assertEqual(model.heroi_pronto_por_nome('harry')['fisico'],2)
        self.assertEqual(model.heroi_pronto_por_nome('harry')['agilidade'],4)
        self.assertEqual(model.heroi_pronto_por_nome('harry')['magia'],7)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['fisico'],3)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['agilidade'],1)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['magia'],8)

    
    def test_ex105b_vida_do_heroi_alterado_por_itens(self):
        self.assertEqual(model.heroi_pronto_por_nome('conan')['vida'],30)
        self.assertEqual(model.heroi_pronto_por_nome('merlin')['vida'],30)
        self.assertEqual(model.heroi_pronto_por_nome('harry')['vida'],20)
    

    def test_ex106_ataque_repetido_gracas_a_agilidade(self):
        merlin = model.heroi_pronto_por_nome('merlin')
        harry = model.heroi_pronto_por_nome('harry')
        self.assertEqual(merlin['vida'],30)
        model.atacar_com_magia(atacante=harry,defensor=merlin)
        self.assertEqual(merlin['vida'],2)
        model.atacar_com_magia(atacante=harry,defensor=merlin)
        self.assertEqual(merlin['vida'],0)

    def test_ex200_criar_heroi(self):
        model.criar_heroi('chun-li',agilidade=5,fisico=7,magia=0)
        chun = model.heroi_pronto_por_nome('chun-li')
        self.assertEqual(chun['agilidade'],5)
        self.assertEqual(chun['fisico'],7)
        harry = model.heroi_pronto_por_nome('harry')
        model.atacar_com_magia(atacante=harry,defensor=chun)
        self.assertEqual(chun['vida'],63)


    def test_ex201_criar_overpower(self):
        self.assertRaises(model.OverpowerException,model.criar_heroi,'freeza',10,10,10)
        self.assertRaises(model.OverpowerException,model.criar_heroi,'legolas',20,2,2)


    def test_ex202_nome_para_id_item(self):
        idDuelo = itens.nome_para_id_item('de duelo')
        duelo = itens.consultar_item(idDuelo)
        self.assertEqual(duelo['nome'],'de duelo')
        idConfortavel = itens.nome_para_id_item('confortavel')
        confortavel = itens.consultar_item(idConfortavel)
        self.assertEqual(confortavel['nome'],'confortavel')


    def test_ex203_criar_item(self):
        itens.criar_item(tipo='varinha', nome='mestra',fisico=0,agilidade=0,magia=8)
        idMestra = itens.nome_para_id_item('mestra')
        mestra = itens.consultar_item(idMestra)
        self.assertEqual(mestra['nome'],'mestra')
        self.assertEqual(mestra['id'],idMestra)
        self.assertEqual(mestra['magia'],8)

    def test_ex204_dar_item_para_heroi_e_colocar_item_em_uso(self):
        itens.criar_item(tipo='espada', nome='celestial',
                          fisico=3,agilidade=3,magia=3)
        chun = model.heroi_pronto_por_nome('chun-li')
        idCelestial = itens.nome_para_id_item('celestial')
        celestial = itens.consultar_item(idCelestial)
        model.dar_item_para_heroi(heroi=chun,item=celestial)
        chun = model.heroi_pronto_por_nome('chun-li')
        self.assertEqual(chun['agilidade'],5) #agilidade ainda nao mudou
        model.colocar_item_em_uso(chun,celestial)
        self.assertEqual(chun['agilidade'],5) #agilidade ainda nao mudou,
        #pois ainda nao fizemos uma nova consulta
        chun = model.heroi_pronto_por_nome('chun-li')
        self.assertEqual(chun['agilidade'],8) #agilidade mudou
        #chun está usando o item e tb fizemos a nova consulta

    def test_ex205_heroi_nao_pode_usar_dois_itens_do_mesmo_tipo(self):
        itens.criar_item(tipo='espada', nome='vorpal',
                          fisico=10,agilidade=2,magia=0)
        chun = model.heroi_pronto_por_nome('chun-li')
        idVorpal = itens.nome_para_id_item('vorpal')
        vorpal = itens.consultar_item(idVorpal)
        model.dar_item_para_heroi(heroi=chun,item=vorpal) #roda sem problemas
        #o que nao pode eh ela usar o item, porque ela ja tem outra varinha
        self.assertRaises(model.HeroiJaUsaEsseTipoDeItemException,model.colocar_item_em_uso,chun,vorpal)



import shutil
def runTests():
        try:
            shutil.copyfile('rpg.original.db','rpg.db')
        except FileNotFoundError:
            print ('''Não achei o arquivo rpg.original.db.
Você precisa abrir a pasta certinha no VSCode/pycharm, pro python poder localizar os arquivos
Não pode ser a pasta "disciplina" tem que ser a pasta "exercicio_sql" mesmo''')
            return
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()

