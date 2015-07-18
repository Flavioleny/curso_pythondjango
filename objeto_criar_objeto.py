from objeto_pessoa import Pessoa
from objeto_pessoa_bb import BB
from objeto_pessoa_vovo import Vovo

#Instanciando um objeto do tipo BB
bb1 = BB("João Gabriel","Thaline André")

#Imprime o BB criado...
print("Nome: " + bb1.nome)
print("Mãe: " + bb1.mae)

#Método definido na super classe Pessoa
bb1.andar()

#Método definido na sub-classe BB
bb1.bicicleta()

#Método chorar da super classe
bb1.chorar()
print("-----------------------------------------------------------------")

#Instanciando um objeto do tipo Pessoa
p1 = Pessoa("João Miguel","Emanuela Carvalho")

#Imprime a pessoa criada...
print("Nome: " + p1.nome)
print("Mãe: " + p1.mae)

#Método definido na própria classe
p1.andar()
p1.chorar()
#Isso vai da merda federal!!!:(
#p1.bicicleta() #Este metodo esta definido na sub-classe, por isso nao funciona.
print("-----------------------------------------------------------------")

#Instanciando um nova vovó
vo = Vovo()

#Setando o nome da vovó
vo.nome = "Maria do Amparo"

#Imprime o nome da vovó
print(vo.nome)

#Chamada ao método da sub-classe Vovó
vo.idade(59)

#Acessando método sobrescrito da super classe
vo.andar()
