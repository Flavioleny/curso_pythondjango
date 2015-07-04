#New-Style
class Pessoa(object):
    nome = ""
    idade= 0

    def _init_(self,nome):
        self.nome = nome
        
    def andar(self):
        print("A pessoa esta andando...")
    
#Instanciamos o objeto
p = Pessoa()

#Definimos o valor do atributo nome
p.nome = "Flavio Santos"

#Definimos o valor do atributo idade
p.idade= 40

#Faz a impressao dos valores dos atributos
print("Nome: ",p.nome, "Idade: ",p.idade)
p.andar()

