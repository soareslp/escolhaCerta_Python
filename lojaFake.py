class LojaFake:
    def __init__(self, total):
        self.total = total


def calculaAderência(empresa, loja):
    totalAderencia = (empresa.total / loja.total) * 100
    return totalAderencia


ponto = LojaFake(32)
ponto3 = LojaFake(36)
ponto4 = LojaFake(95)
ponto5 = LojaFake(32)
ponto7 = LojaFake(84)
ponto15 = LojaFake(58)
ponto16 = LojaFake(46)
ponto24 = LojaFake(101)
ponto26 = LojaFake(106)
ponto40 = LojaFake(117)
ponto55 = LojaFake(141)
ponto67 = LojaFake(143)

acaiteria = LojaFake(60)
carrinhoPipoca = LojaFake(32)
carroChurros = LojaFake(48)
empada = LojaFake(70)
foodTruck = LojaFake(82)
hamburgueria = LojaFake(114)
lanchonete = LojaFake(47)
lojaCachorroQuente = LojaFake(96)
pastelaria = LojaFake(130)
pizzaria = LojaFake(131)
salgaderia = LojaFake(42)
sorveteria = LojaFake(96)

print(round(calculaAderência(acaiteria, ponto15),2))
