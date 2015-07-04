#Calcular Metros em Pes
class Converter(object):   
    def _init_(self,altura):
        self.altura = altura

    def Pes(self,altura): 
        self.altura = 3.28 * altura
        print("A altura da pessoa em Pes e = ", self.altura)

v_altura = float(input("Digite a altura da pessoa: "))
c = Converter()
c.Pes(v_altura)


