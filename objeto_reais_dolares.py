#Calcular valores reais em dolares
class Converter(object):

    def dolar(self,real,dolar): 
        valor = real * dolar
        print("O valor de Reais em Dolares = ", valor)

v_real  = float(input("Digite o valor em Real: "))
v_dolar = float(input("Digite o valor em Dolar: "))
v = Converter()
v.dolar(v_real,v_dolar)

