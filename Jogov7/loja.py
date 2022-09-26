import pygame

class Loja(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0, placa=0, tamanho=0, acessibilidade=0, ventilacao=0, iluminacao=0, arCond=0, qtdBanheiro=0,
                 tamCozinha=0, numAssentos=0, camSeguranca=0, extIncendio=0, almSeguranca=0, wifi=0, consLoja=0, estacionamento=0,
                 possExpansao=0, vitrine=0, iptu=0, numConco=0, implantacao=0, total=0):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(f'{placa}'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.tamanho = tamanho
        self.acessibilidade = acessibilidade
        self.ventilacao = ventilacao
        self.iluminacao = iluminacao
        self.arCond = arCond
        self.qtdBanheiro = qtdBanheiro
        self.tamCozinha = tamCozinha
        self.numAssentos = numAssentos
        self.camSeguranca = camSeguranca
        self.extIncendio = extIncendio
        self.almSeguranca = almSeguranca
        self.wifi = wifi
        self.consLoja = consLoja
        self.estacionamento = estacionamento
        self.possExpansao = possExpansao
        self.vitrine = vitrine
        self.iptu = iptu
        self.numConco = numConco
        self.implantacao = implantacao
        self.total = total

    def aderencia(self):
        self.total / self.total