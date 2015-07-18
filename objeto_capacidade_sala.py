#Calcular capacidade maxima de pessoas dentro de uma sala
#Ad –área disponível da sala (m2)
#Ep –espaço requerido por pessoas na sala(m2/ocupante)

class Capacidade(object):
    capacidade = 0   
    
    def __init__(self, area, espaco):
        self.area  = area
        self.espaco= espaco
    
    def calculo(self):
        self.capacidade = self.area / self.espaco
        print("Capacidade maxima de pessoas na sala e = " + str(self.capacidade))

v_ad = float(input("Digite a Area disponivel da sala(m2): "))
v_ep = float(input("Digite o espaço requerido por pessoas na sala(m2): "))

c = Capacidade(v_ad,v_ep)
c.calculo()
