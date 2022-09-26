import unittest
from lojaFake import LojaFake, calculaAderência

class TestAderencia(unittest.TestCase):
    def setUp(self):
        self.ponto1 = LojaFake(32)
        self.ponto3 = LojaFake(36)
        self.ponto4 = LojaFake(95)
        self.ponto5 = LojaFake(32)
        self.ponto7 = LojaFake(84)
        self.ponto15 = LojaFake(58)
        self.ponto16 = LojaFake(46)
        self.ponto24 = LojaFake(101)
        self.ponto26 = LojaFake(106)
        self.ponto40 = LojaFake(117)
        self.ponto55 = LojaFake(141)
        self.ponto67 = LojaFake(143)

        self.acaiteria = LojaFake(60)
        self.carrinhoPipoca = LojaFake(32)
        self.carroChurros = LojaFake(48)
        self.empada = LojaFake(70)
        self.foodTruck = LojaFake(82)
        self.hamburgueria = LojaFake(114)
        self.lanchonete = LojaFake(47)
        self.lojaCachorroQuente = LojaFake(96)
        self.pastelaria = LojaFake(130)
        self.pizzaria = LojaFake(131)
        self.salgaderia = LojaFake(42)
        self.sorveteria = LojaFake(96)

    #AÇAITERIA
    def test_aderênciaTeste_Acaiteria_Ponto1(self):
        self.assertEquals(187.50, round(calculaAderência(self.acaiteria, self.ponto1), 2))

    def test_aderênciaTeste_Acaiteria_Ponto3(self):
        self.assertEquals(166.67, round(calculaAderência(self.acaiteria, self.ponto3), 2))

    def test_aderênciaTeste_Acaiteria_Ponto4(self):
        self.assertEquals(63.16, round(calculaAderência(self.acaiteria, self.ponto4), 2))

    def test_aderênciaTeste_Acaiteria_Ponto5(self):
        self.assertEquals(187.50, round(calculaAderência(self.acaiteria, self.ponto5), 2))

    def test_aderênciaTeste_Acaiteria_Ponto7(self):
        self.assertEquals(71.43, round(calculaAderência(self.acaiteria, self.ponto7), 2))

    def test_aderênciaTeste_Acaiteria_Ponto15(self):
        self.assertEquals(103.45, round(calculaAderência(self.acaiteria, self.ponto15), 2))

    def test_aderênciaTeste_Acaiteria_Ponto16(self):
        self.assertEquals(130.43, round(calculaAderência(self.acaiteria, self.ponto16), 2))

    def test_aderênciaTeste_Acaiteria_Ponto24(self):
        self.assertEquals(59.41, round(calculaAderência(self.acaiteria, self.ponto24), 2))

    def test_aderênciaTeste_Acaiteria_Ponto26(self):
        self.assertEquals(56.60, round(calculaAderência(self.acaiteria, self.ponto26), 2))

    def test_aderênciaTeste_Acaiteria_Ponto40(self):
        self.assertEquals(51.28, round(calculaAderência(self.acaiteria, self.ponto40), 2))

    def test_aderênciaTeste_Acaiteria_Ponto55(self):
        self.assertEquals(42.55, round(calculaAderência(self.acaiteria, self.ponto55), 2))

    def test_aderênciaTeste_Acaiteria_Ponto67(self):
        self.assertEquals(41.96, round(calculaAderência(self.acaiteria, self.ponto67), 2))


    #CARRINHO DA PIPOCA
    def test_aderênciaTeste_CarrinhoPipoca_Ponto1(self):
        self.assertEquals(100.00, round(calculaAderência(self.carrinhoPipoca, self.ponto1), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto3(self):
        self.assertEquals(88.89, round(calculaAderência(self.carrinhoPipoca, self.ponto3), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto4(self):
        self.assertEquals(33.68, round(calculaAderência(self.carrinhoPipoca, self.ponto4), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto5(self):
        self.assertEquals(100.00, round(calculaAderência(self.carrinhoPipoca, self.ponto5), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto7(self):
        self.assertEquals(38.10, round(calculaAderência(self.carrinhoPipoca, self.ponto7), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto15(self):
        self.assertEquals(55.17, round(calculaAderência(self.carrinhoPipoca, self.ponto15), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto16(self):
        self.assertEquals(69.57, round(calculaAderência(self.carrinhoPipoca, self.ponto16), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto24(self):
        self.assertEquals(31.68, round(calculaAderência(self.carrinhoPipoca, self.ponto24), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto26(self):
        self.assertEquals(30.19, round(calculaAderência(self.carrinhoPipoca, self.ponto26), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto40(self):
        self.assertEquals(27.35, round(calculaAderência(self.carrinhoPipoca, self.ponto40), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto55(self):
        self.assertEquals(22.70, round(calculaAderência(self.carrinhoPipoca, self.ponto55), 2))

    def test_aderênciaTeste_CarrinhoPipoca_Ponto67(self):
        self.assertEquals(22.38, round(calculaAderência(self.carrinhoPipoca, self.ponto67), 2))



    #CARRINHO DA PIPOCA
    def test_aderênciaTeste_CarroChurros_Ponto1(self):
        self.assertEquals(150.00, round(calculaAderência(self.carroChurros, self.ponto1), 2))

    def test_aderênciaTeste_CarroChurros_Ponto3(self):
        self.assertEquals(133.33, round(calculaAderência(self.carroChurros, self.ponto3), 2))

    def test_aderênciaTeste_CarroChurros_Ponto4(self):
        self.assertEquals(50.53, round(calculaAderência(self.carroChurros, self.ponto4), 2))

    def test_aderênciaTeste_CarroChurros_Ponto5(self):
        self.assertEquals(150.00, round(calculaAderência(self.carroChurros, self.ponto5), 2))

    def test_aderênciaTeste_CarroChurros_Ponto7(self):
        self.assertEquals(57.14, round(calculaAderência(self.carroChurros, self.ponto7), 2))

    def test_aderênciaTeste_CarroChurros_Ponto15(self):
        self.assertEquals(82.76, round(calculaAderência(self.carroChurros, self.ponto15), 2))

    def test_aderênciaTeste_CarroChurros_Ponto16(self):
        self.assertEquals(104.35, round(calculaAderência(self.carroChurros, self.ponto16), 2))

    def test_aderênciaTeste_CarroChurros_Ponto24(self):
        self.assertEquals(47.52, round(calculaAderência(self.carroChurros, self.ponto24), 2))

    def test_aderênciaTeste_CarroChurros_Ponto26(self):
        self.assertEquals(45.28, round(calculaAderência(self.carroChurros, self.ponto26), 2))

    def test_aderênciaTeste_CarroChurros_Ponto40(self):
        self.assertEquals(41.03, round(calculaAderência(self.carroChurros, self.ponto40), 2))

    def test_aderênciaTeste_CarroChurros_Ponto55(self):
        self.assertEquals(34.04, round(calculaAderência(self.carroChurros, self.ponto55), 2))

    def test_aderênciaTeste_CarroChurros_Ponto67(self):
        self.assertEquals(33.57, round(calculaAderência(self.carroChurros, self.ponto67), 2))



    #LOJA DE EMPADA
    def test_aderênciaTeste_Empada_Ponto1(self):
        self.assertEquals(218.75, round(calculaAderência(self.empada, self.ponto1), 2))

    def test_aderênciaTeste_Empada_Ponto3(self):
        self.assertEquals(194.44, round(calculaAderência(self.empada, self.ponto3), 2))

    def test_aderênciaTeste_Empada_Ponto4(self):
        self.assertEquals(73.68, round(calculaAderência(self.empada, self.ponto4), 2))

    def test_aderênciaTeste_Empada_Ponto5(self):
        self.assertEquals(218.75, round(calculaAderência(self.empada, self.ponto5), 2))

    def test_aderênciaTeste_Empada_Ponto7(self):
        self.assertEquals(83.33, round(calculaAderência(self.empada, self.ponto7), 2))

    def test_aderênciaTeste_Empada_Ponto15(self):
        self.assertEquals(120.69, round(calculaAderência(self.empada, self.ponto15), 2))

    def test_aderênciaTeste_Empada_Ponto16(self):
        self.assertEquals(152.17, round(calculaAderência(self.empada, self.ponto16), 2))

    def test_aderênciaTeste_Empada_Ponto24(self):
        self.assertEquals(69.31, round(calculaAderência(self.empada, self.ponto24), 2))

    def test_aderênciaTeste_Empada_Ponto26(self):
        self.assertEquals(66.04, round(calculaAderência(self.empada, self.ponto26), 2))

    def test_aderênciaTeste_Empada_Ponto40(self):
        self.assertEquals(59.83, round(calculaAderência(self.empada, self.ponto40), 2))

    def test_aderênciaTeste_Empada_Ponto55(self):
        self.assertEquals(49.65, round(calculaAderência(self.empada, self.ponto55), 2))

    def test_aderênciaTeste_Empada_Ponto67(self):
        self.assertEquals(48.95, round(calculaAderência(self.empada, self.ponto67), 2))



    #FOODTRUCK
    def test_aderênciaTeste_Foodtruck_Ponto1(self):
        self.assertEquals(256.25, round(calculaAderência(self.foodTruck, self.ponto1), 2))

    def test_aderênciaTeste_Foodtruck_Ponto3(self):
        self.assertEquals(227.78, round(calculaAderência(self.foodTruck, self.ponto3), 2))

    def test_aderênciaTeste_Foodtruck_Ponto4(self):
        self.assertEquals(86.32, round(calculaAderência(self.foodTruck, self.ponto4), 2))

    def test_aderênciaTeste_Foodtruck_Ponto5(self):
        self.assertEquals(256.25, round(calculaAderência(self.foodTruck, self.ponto5), 2))

    def test_aderênciaTeste_Foodtruck_Ponto7(self):
        self.assertEquals(97.62, round(calculaAderência(self.foodTruck, self.ponto7), 2))

    def test_aderênciaTeste_Foodtruck_Ponto15(self):
        self.assertEquals(141.38, round(calculaAderência(self.foodTruck, self.ponto15), 2))

    def test_aderênciaTeste_Foodtruck_Ponto16(self):
        self.assertEquals(178.26, round(calculaAderência(self.foodTruck, self.ponto16), 2))

    def test_aderênciaTeste_Foodtruck_Ponto24(self):
        self.assertEquals(81.19, round(calculaAderência(self.foodTruck, self.ponto24), 2))

    def test_aderênciaTeste_Foodtruck_Ponto26(self):
        self.assertEquals(77.36, round(calculaAderência(self.foodTruck, self.ponto26), 2))

    def test_aderênciaTeste_Foodtruck_Ponto40(self):
        self.assertEquals(70.09, round(calculaAderência(self.foodTruck, self.ponto40), 2))

    def test_aderênciaTeste_Foodtruck_Ponto55(self):
        self.assertEquals(58.16, round(calculaAderência(self.foodTruck, self.ponto55), 2))

    def test_aderênciaTeste_Foodtruck_Ponto67(self):
        self.assertEquals(57.34, round(calculaAderência(self.foodTruck, self.ponto67), 2))



    #HAMBURGUERIA
    def test_aderênciaTeste_Hamburgueria_Ponto1(self):
        self.assertEquals(356.25, round(calculaAderência(self.hamburgueria, self.ponto1), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto3(self):
        self.assertEquals(316.67, round(calculaAderência(self.hamburgueria, self.ponto3), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto4(self):
        self.assertEquals(120.00, round(calculaAderência(self.hamburgueria, self.ponto4), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto5(self):
        self.assertEquals(356.25, round(calculaAderência(self.hamburgueria, self.ponto5), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto7(self):
        self.assertEquals(135.71, round(calculaAderência(self.hamburgueria, self.ponto7), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto15(self):
        self.assertEquals(196.55, round(calculaAderência(self.hamburgueria, self.ponto15), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto16(self):
        self.assertEquals(247.83, round(calculaAderência(self.hamburgueria, self.ponto16), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto24(self):
        self.assertEquals(112.87, round(calculaAderência(self.hamburgueria, self.ponto24), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto26(self):
        self.assertEquals(107.55, round(calculaAderência(self.hamburgueria, self.ponto26), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto40(self):
        self.assertEquals(97.44, round(calculaAderência(self.hamburgueria, self.ponto40), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto55(self):
        self.assertEquals(80.85, round(calculaAderência(self.hamburgueria, self.ponto55), 2))

    def test_aderênciaTeste_Hamburgueria_Ponto67(self):
        self.assertEquals(79.72, round(calculaAderência(self.hamburgueria, self.ponto67), 2))



    #LANCHONETE
    def test_aderênciaTeste_Lanchonete_Ponto1(self):
        self.assertEquals(146.88, round(calculaAderência(self.lanchonete, self.ponto1), 2))

    def test_aderênciaTeste_Lanchonete_Ponto3(self):
        self.assertEquals(130.56, round(calculaAderência(self.lanchonete, self.ponto3), 2))

    def test_aderênciaTeste_Lanchonete_Ponto4(self):
        self.assertEquals(49.47, round(calculaAderência(self.lanchonete, self.ponto4), 2))

    def test_aderênciaTeste_Lanchonete_Ponto5(self):
        self.assertEquals(146.88, round(calculaAderência(self.lanchonete, self.ponto5), 2))

    def test_aderênciaTeste_Lanchonete_Ponto7(self):
        self.assertEquals(55.95, round(calculaAderência(self.lanchonete, self.ponto7), 2))

    def test_aderênciaTeste_Lanchonete_Ponto15(self):
        self.assertEquals(81.03, round(calculaAderência(self.lanchonete, self.ponto15), 2))

    def test_aderênciaTeste_Lanchonete_Ponto16(self):
        self.assertEquals(102.17, round(calculaAderência(self.lanchonete, self.ponto16), 2))

    def test_aderênciaTeste_Lanchonete_Ponto24(self):
        self.assertEquals(46.53, round(calculaAderência(self.lanchonete, self.ponto24), 2))

    def test_aderênciaTeste_Lanchonete_Ponto26(self):
        self.assertEquals(44.34, round(calculaAderência(self.lanchonete, self.ponto26), 2))

    def test_aderênciaTeste_Lanchonete_Ponto40(self):
        self.assertEquals(40.17, round(calculaAderência(self.lanchonete, self.ponto40), 2))

    def test_aderênciaTeste_Lanchonete_Ponto55(self):
        self.assertEquals(33.33, round(calculaAderência(self.lanchonete, self.ponto55), 2))

    def test_aderênciaTeste_Lanchonete_Ponto67(self):
        self.assertEquals(32.87, round(calculaAderência(self.lanchonete, self.ponto67), 2))



    #LOJA CACHORRO-QUENTE
    def test_aderênciaTeste_CachorroQuente_Ponto1(self):
        self.assertEquals(300.00, round(calculaAderência(self.lojaCachorroQuente, self.ponto1), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto3(self):
        self.assertEquals(266.67, round(calculaAderência(self.lojaCachorroQuente, self.ponto3), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto4(self):
        self.assertEquals(101.05, round(calculaAderência(self.lojaCachorroQuente, self.ponto4), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto5(self):
        self.assertEquals(300, round(calculaAderência(self.lojaCachorroQuente, self.ponto5), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto7(self):
        self.assertEquals(114.29, round(calculaAderência(self.lojaCachorroQuente, self.ponto7), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto15(self):
        self.assertEquals(165.52, round(calculaAderência(self.lojaCachorroQuente, self.ponto15), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto16(self):
        self.assertEquals(208.70, round(calculaAderência(self.lojaCachorroQuente, self.ponto16), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto24(self):
        self.assertEquals(95.05, round(calculaAderência(self.lojaCachorroQuente, self.ponto24), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto26(self):
        self.assertEquals(90.57, round(calculaAderência(self.lojaCachorroQuente, self.ponto26), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto40(self):
        self.assertEquals(82.05, round(calculaAderência(self.lojaCachorroQuente, self.ponto40), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto55(self):
        self.assertEquals(68.09, round(calculaAderência(self.lojaCachorroQuente, self.ponto55), 2))

    def test_aderênciaTeste_CachorroQuente_Ponto67(self):
        self.assertEquals(67.13, round(calculaAderência(self.lojaCachorroQuente, self.ponto67), 2))



    #PASTELARIA
    def test_aderênciaTeste_Pastelaria_Ponto1(self):
        self.assertEquals(406.25, round(calculaAderência(self.pastelaria, self.ponto1), 2))

    def test_aderênciaTeste_Pastelaria_Ponto3(self):
        self.assertEquals(361.11, round(calculaAderência(self.pastelaria, self.ponto3), 2))

    def test_aderênciaTeste_Pastelaria_Ponto4(self):
        self.assertEquals(136.84, round(calculaAderência(self.pastelaria, self.ponto4), 2))

    def test_aderênciaTeste_Pastelaria_Ponto5(self):
        self.assertEquals(406.25, round(calculaAderência(self.pastelaria, self.ponto5), 2))

    def test_aderênciaTeste_Pastelaria_Ponto7(self):
        self.assertEquals(154.76, round(calculaAderência(self.pastelaria, self.ponto7), 2))

    def test_aderênciaTeste_Pastelaria_Ponto15(self):
        self.assertEquals(224.14, round(calculaAderência(self.pastelaria, self.ponto15), 2))

    def test_aderênciaTeste_Pastelaria_Ponto16(self):
        self.assertEquals(282.61, round(calculaAderência(self.pastelaria, self.ponto16), 2))

    def test_aderênciaTeste_Pastelaria_Ponto24(self):
        self.assertEquals(128.71, round(calculaAderência(self.pastelaria, self.ponto24), 2))

    def test_aderênciaTeste_Pastelaria_Ponto26(self):
        self.assertEquals(122.64, round(calculaAderência(self.pastelaria, self.ponto26), 2))

    def test_aderênciaTeste_Pastelaria_Ponto40(self):
        self.assertEquals(111.11, round(calculaAderência(self.pastelaria, self.ponto40), 2))

    def test_aderênciaTeste_Pastelaria_Ponto55(self):
        self.assertEquals(92.20, round(calculaAderência(self.pastelaria, self.ponto55), 2))

    def test_aderênciaTeste_Pastelaria_Ponto67(self):
        self.assertEquals(90.91, round(calculaAderência(self.pastelaria, self.ponto67), 2))



    #PASTELARIA
    def test_aderênciaTeste_Pizzaria_Ponto1(self):
        self.assertEquals(409.38, round(calculaAderência(self.pizzaria, self.ponto1), 2))

    def test_aderênciaTeste_Pizzaria_Ponto3(self):
        self.assertEquals(363.89, round(calculaAderência(self.pizzaria, self.ponto3), 2))

    def test_aderênciaTeste_Pizzaria_Ponto4(self):
        self.assertEquals(137.89, round(calculaAderência(self.pizzaria, self.ponto4), 2))

    def test_aderênciaTeste_Pizzaria_Ponto5(self):
        self.assertEquals(409.38, round(calculaAderência(self.pizzaria, self.ponto5), 2))

    def test_aderênciaTeste_Pizzaria_Ponto7(self):
        self.assertEquals(155.95, round(calculaAderência(self.pizzaria, self.ponto7), 2))

    def test_aderênciaTeste_Pizzaria_Ponto15(self):
        self.assertEquals(225.86, round(calculaAderência(self.pizzaria, self.ponto15), 2))

    def test_aderênciaTeste_Pizzaria_Ponto16(self):
        self.assertEquals(284.78, round(calculaAderência(self.pizzaria, self.ponto16), 2))

    def test_aderênciaTeste_Pizzaria_Ponto24(self):
        self.assertEquals(129.70, round(calculaAderência(self.pizzaria, self.ponto24), 2))

    def test_aderênciaTeste_Pizzaria_Ponto26(self):
        self.assertEquals(123.58, round(calculaAderência(self.pizzaria, self.ponto26), 2))

    def test_aderênciaTeste_Pizzaria_Ponto40(self):
        self.assertEquals(111.97, round(calculaAderência(self.pizzaria, self.ponto40), 2))

    def test_aderênciaTeste_Pizzaria_Ponto55(self):
        self.assertEquals(92.91, round(calculaAderência(self.pizzaria, self.ponto55), 2))

    def test_aderênciaTeste_Pizzaria_Ponto67(self):
        self.assertEquals(91.61, round(calculaAderência(self.pizzaria, self.ponto67), 2))



    #PASTELARIA
    def test_aderênciaTeste_Salgaderia_Ponto1(self):
        self.assertEquals(131.25, round(calculaAderência(self.salgaderia, self.ponto1), 2))

    def test_aderênciaTeste_Salgaderia_Ponto3(self):
        self.assertEquals(116.67, round(calculaAderência(self.salgaderia, self.ponto3), 2))

    def test_aderênciaTeste_Salgaderia_Ponto4(self):
        self.assertEquals(44.21, round(calculaAderência(self.salgaderia, self.ponto4), 2))

    def test_aderênciaTeste_Salgaderia_Ponto5(self):
        self.assertEquals(131.25, round(calculaAderência(self.salgaderia, self.ponto5), 2))

    def test_aderênciaTeste_Salgaderia_Ponto7(self):
        self.assertEquals(50.00, round(calculaAderência(self.salgaderia, self.ponto7), 2))

    def test_aderênciaTeste_Salgaderia_Ponto15(self):
        self.assertEquals(72.41, round(calculaAderência(self.salgaderia, self.ponto15), 2))

    def test_aderênciaTeste_Salgaderia_Ponto16(self):
        self.assertEquals(91.30, round(calculaAderência(self.salgaderia, self.ponto16), 2))

    def test_aderênciaTeste_Salgaderia_Ponto24(self):
        self.assertEquals(41.58, round(calculaAderência(self.salgaderia, self.ponto24), 2))

    def test_aderênciaTeste_Salgaderia_Ponto26(self):
        self.assertEquals(39.62, round(calculaAderência(self.salgaderia, self.ponto26), 2))

    def test_aderênciaTeste_Salgaderia_Ponto40(self):
        self.assertEquals(35.90, round(calculaAderência(self.salgaderia, self.ponto40), 2))

    def test_aderênciaTeste_Salgaderia_Ponto55(self):
        self.assertEquals(29.79, round(calculaAderência(self.salgaderia, self.ponto55), 2))

    def test_aderênciaTeste_Salgaderia_Ponto67(self):
        self.assertEquals(29.37, round(calculaAderência(self.salgaderia, self.ponto67), 2))



    #PASTELARIA
    def test_aderênciaTeste_Sorveteria_Ponto1(self):
        self.assertEquals(300.00, round(calculaAderência(self.sorveteria, self.ponto1), 2))

    def test_aderênciaTeste_Sorveteria_Ponto3(self):
        self.assertEquals(266.67, round(calculaAderência(self.sorveteria, self.ponto3), 2))

    def test_aderênciaTeste_Sorveteria_Ponto4(self):
        self.assertEquals(101.05, round(calculaAderência(self.sorveteria, self.ponto4), 2))

    def test_aderênciaTeste_Sorveteria_Ponto5(self):
        self.assertEquals(300, round(calculaAderência(self.sorveteria, self.ponto5), 2))

    def test_aderênciaTeste_Sorveteria_Ponto7(self):
        self.assertEquals(114.29, round(calculaAderência(self.sorveteria, self.ponto7), 2))

    def test_aderênciaTeste_Sorveteria_Ponto15(self):
        self.assertEquals(165.52, round(calculaAderência(self.sorveteria, self.ponto15), 2))

    def test_aderênciaTeste_Sorveteria_Ponto16(self):
        self.assertEquals(208.70, round(calculaAderência(self.sorveteria, self.ponto16), 2))

    def test_aderênciaTeste_Sorveteria_Ponto24(self):
        self.assertEquals(95.05, round(calculaAderência(self.sorveteria, self.ponto24), 2))

    def test_aderênciaTeste_Sorveteria_Ponto26(self):
        self.assertEquals(90.57, round(calculaAderência(self.sorveteria, self.ponto26), 2))

    def test_aderênciaTeste_Sorveteria_Ponto40(self):
        self.assertEquals(82.05, round(calculaAderência(self.sorveteria, self.ponto40), 2))

    def test_aderênciaTeste_Sorveteria_Ponto55(self):
        self.assertEquals(68.09, round(calculaAderência(self.sorveteria, self.ponto55), 2))

    def test_aderênciaTeste_Sorveteria_Ponto67(self):
        self.assertEquals(67.13, round(calculaAderência(self.sorveteria, self.ponto67), 2))