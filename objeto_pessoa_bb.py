#Realiza a importaçao da classe Pessoa
from objeto_pessoa import Pessoa

#Herdamos da classe Pessoa
class BB(Pessoa):

    def __init__(self, nome, mae):
        print("Método construtor da sub classe")
        super().__init__(nome,mae) #Acessa o metodo construtor da super classe
        self.nome = nome
        self.mae  = mae

    #Especializaçao da classe
    def bicicleta(self):
        print("Agora aprendendo a pedalar...")
