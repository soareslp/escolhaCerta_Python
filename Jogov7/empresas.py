import sys, loja, botao, intro, mapa
from config import *


def run():
    background = pygame.image.load('imagens/cackground/fundo.jpg')
    tela.blit(background, (0, 0))

    acaiteria = loja.Loja(20, 115, 'imagens\empresas\caiteria.png', 12, 10, 6, 6, 0, 0, 1, 6, 0, 0, 10, 0, 6, 0, 0, 0,
                          1600, 0, 1200, 60)
    carrinhoPipoca = loja.Loja(250, 115, 'imagens\empresas\carrinhoPipoca.png', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
                               0, 0, 0, 900, 0, 500, 32)
    carroChurros = loja.Loja(480, 115, 'imagens\empresas\carroChurros.png', 4, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 6, 0, 0,
                             0, 400, 0, 1000, 48)
    empada = loja.Loja(710, 115, 'imagens\empresas\empada.png', 35, 0, 6, 10, 0, 0, 0, 0, 0, 10, 0, 0, 6, 0, 0, 0, 400, 0,
                       1000, 70)


    foodTruck = loja.Loja(20, 305, 'imagens\empresas\goodtruck.png', 6, 0, 4, 4, 0, 0, 1, 8, 0, 10, 10, 0, 10, 2, 10, 0,
                          1000, 0, 1500, 82)
    hamburgueria = loja.Loja(250, 305, 'imagens\empresas\hamburgueria.png', 50, 10, 10, 7, 10, 2, 4, 20, 10, 10, 10, 0,
                             10, 0, 0, 0, 3500, 2, 5000, 114)
    lanchonete = loja.Loja(480, 305, 'imagens\empresas\lanchonete.png', 15, 0, 4, 8, 0, 0, 1, 5, 0, 0, 0, 0, 3, 0, 0, 0,
                           1500, 0, 1000, 47)
    lojaCachorroQuente = loja.Loja(710, 305, 'imagens\empresas\lojacachorroquente.png', 20, 10, 7, 6, 0, 2, 3, 10, 10, 0, 0,
                                   0, 7, 0, 10, 10, 2300, 0, 5000, 96)


    pastelaria = loja.Loja(20, 495, 'imagens\empresas\pastelaria.png', 40, 10, 9, 8, 10, 2, 6, 30, 10, 10, 10, 10, 8, 0, 0, 0,
                           3300, 0, 4000, 130)
    pizzaria = loja.Loja(250, 495, 'imagens\empresas\pizzaria.png', 80, 10, 8, 10, 10, 4, 8, 40, 5, 10, 10, 10, 10, 8, 0, 0,
                         5000, 0, 6000, 131)
    salgaderia = loja.Loja(480, 495, 'imagens\empresas\salgaderia.png', 10, 0, 3, 4, 0, 0, 1, 4, 5, 0, 0, 0, 5, 0, 0, 0,
                           1200, 0, 2500, 42)
    sorveteria = loja.Loja(710, 495, 'imagens\empresas\sorveteria.png', 25, 0, 10, 10, 0, 2, 2, 25, 10, 10, 10, 0, 9, 0, 0, 0,
                           2400, 0, 3000, 96)

    voltar = botao.Botao((LARGURA - 65), (ALTURA - 75), 'imagens/tutorial/voltar.png')

    confirmaAcai = pygame.Rect(1150, 595, 115, 25)
    confirmaPipoca = pygame.Rect(1150, 595, 115, 25)
    confirmaChurr = pygame.Rect(1150, 595, 115, 25)
    confirmaEmpa = pygame.Rect(1150, 595, 115, 25)
    confirmaFood = pygame.Rect(1150, 595, 115, 25)
    confirmaHamb = pygame.Rect(1150, 595, 115, 25)
    confirmaLanche = pygame.Rect(1150, 595, 115, 25)
    confirmaCacho = pygame.Rect(1150, 595, 115, 25)
    confirmaPas = pygame.Rect(1150, 595, 115, 25)
    confirmaPizz = pygame.Rect(1150, 595, 115, 25)
    confirmaSal = pygame.Rect(1150, 595, 115, 25)
    confirmaSorv = pygame.Rect(1150, 595, 115, 25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            tela.blit(titulo_font.render('Selecione o tipo de empresa:', True, BLUE),
                      (LARGURA / 2 - 500, ALTURA / 2 - 380))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if voltar.rect.collidepoint(event.pos):
                    intro.run()
                elif acaiteria.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {acaiteria.tamanho}M²',
                                 f'Acessibilidade: {acaiteria.acessibilidade}',
                                 f'Ventilação: {acaiteria.ventilacao}',
                                 f'Iluminaçao: {acaiteria.iluminacao}',
                                 f'Ar Condicionado: {acaiteria.arCond}',
                                 f'Quantidade de banheiros: {acaiteria.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {acaiteria.tamCozinha}',
                                 f'Número de Assentos: {acaiteria.numAssentos}',
                                 f'Câmeras de Segurança: {acaiteria.camSeguranca}',
                                 f'Extintor de Incêndio: {acaiteria.extIncendio}',
                                 f'Alarmes de Segurança: {acaiteria.almSeguranca}',
                                 f'Wi-Fi: {acaiteria.wifi}',
                                 f'Conservação da Loja: {acaiteria.consLoja}',
                                 f'Estacionamento: {acaiteria.estacionamento}',
                                 f'Possibilidade de Expansão: {acaiteria.possExpansao}',
                                 f'Vitrine: {acaiteria.vitrine}',
                                 f'IPTU: R${acaiteria.iptu:.2f}',
                                 f'Concorrentes: {acaiteria.numConco}',
                                 f'Custos de Implantação: R${acaiteria.implantacao:.2f}',
                                 f'Total: {acaiteria.total}')

                    confirmaAcai.update(1150, 595, 115, 25)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaAcai)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaAcai.collidepoint(event.pos):
                    mapa.run(acaiteria)

                elif carrinhoPipoca.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {carrinhoPipoca.tamanho}M²',
                                 f'Acessibilidade: {carrinhoPipoca.acessibilidade}',
                                 f'Ventilação: {carrinhoPipoca.ventilacao}',
                                 f'Iluminaçao: {carrinhoPipoca.iluminacao}',
                                 f'Ar Condicionado: {carrinhoPipoca.arCond}',
                                 f'Quantidade de banheiros: {carrinhoPipoca.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {carrinhoPipoca.tamCozinha}',
                                 f'Número de Assentos: {carrinhoPipoca.numAssentos}',
                                 f'Câmeras de Segurança: {carrinhoPipoca.camSeguranca}',
                                 f'Extintor de Incêndio: {carrinhoPipoca.extIncendio}',
                                 f'Alarmes de Segurança: {carrinhoPipoca.almSeguranca}',
                                 f'Wi-Fi: {carrinhoPipoca.wifi}',
                                 f'Conservação da Loja: {carrinhoPipoca.consLoja}',
                                 f'Estacionamento: {carrinhoPipoca.estacionamento}',
                                 f'Possibilidade de Expansão: {carrinhoPipoca.possExpansao}',
                                 f'Vitrine: {carrinhoPipoca.vitrine}',
                                 f'IPTU: R${carrinhoPipoca.iptu:.2f}',
                                 f'Concorrentes: {carrinhoPipoca.numConco}',
                                 f'Custos de Implantação: R${carrinhoPipoca.implantacao:.2f}',
                                 f'Total: {carrinhoPipoca.total}')
                    confirmaAcai.update(2000,2000,1,1)
                    confirmaPipoca.update(1150, 595, 115, 25)
                    confirmaChurr.update(2000,2000,1,1)
                    confirmaEmpa.update(2000,2000,1,1)
                    confirmaFood.update(2000,2000,1,1)
                    confirmaHamb.update(2000,2000,1,1)
                    confirmaLanche.update(2000,2000,1,1)
                    confirmaCacho.update(2000,2000,1,1)
                    confirmaPas.update(2000,2000,1,1)
                    confirmaPizz.update(2000,2000,1,1)
                    confirmaSal.update(2000,2000,1,1)
                    confirmaSorv.update(2000,2000,1,1)
                    pygame.draw.rect(tela, BLACK, confirmaPipoca)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaPipoca.collidepoint(event.pos):
                    mapa.run(carrinhoPipoca)

                elif carroChurros.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {carroChurros.tamanho}M²',
                                 f'Acessibilidade: {carroChurros.acessibilidade}',
                                 f'Ventilação: {carroChurros.ventilacao}',
                                 f'Iluminaçao: {carroChurros.iluminacao}',
                                 f'Ar Condicionado: {carroChurros.arCond}',
                                 f'Quantidade de banheiros: {carroChurros.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {carroChurros.tamCozinha}',
                                 f'Número de Assentos: {carroChurros.numAssentos}',
                                 f'Câmeras de Segurança: {carroChurros.camSeguranca}',
                                 f'Extintor de Incêndio: {carroChurros.extIncendio}',
                                 f'Alarmes de Segurança: {carroChurros.almSeguranca}',
                                 f'Wi-Fi: {carroChurros.wifi}',
                                 f'Conservação da Loja: {carroChurros.consLoja}',
                                 f'Estacionamento: {carroChurros.estacionamento}',
                                 f'Possibilidade de Expansão: {carroChurros.possExpansao}',
                                 f'Vitrine: {carroChurros.vitrine}',
                                 f'IPTU: R${carroChurros.iptu:.2f}',
                                 f'Concorrentes: {carroChurros.numConco}',
                                 f'Custos de Implantação: R${carroChurros.implantacao:.2f}',
                                 f'Total: {carroChurros.total}')
                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(1150, 595, 115, 25)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaChurr)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaChurr.collidepoint(event.pos):
                    mapa.run(carroChurros)

                elif empada.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {empada.tamanho}M²',
                                 f'Acessibilidade: {empada.acessibilidade}',
                                 f'Ventilação: {empada.ventilacao}',
                                 f'Iluminaçao: {empada.iluminacao}',
                                 f'Ar Condicionado: {empada.arCond}',
                                 f'Quantidade de banheiros: {empada.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {empada.tamCozinha}',
                                 f'Número de Assentos: {empada.numAssentos}',
                                 f'Câmeras de Segurança: {empada.camSeguranca}',
                                 f'Extintor de Incêndio: {empada.extIncendio}',
                                 f'Alarmes de Segurança: {empada.almSeguranca}',
                                 f'Wi-Fi: {empada.wifi}',
                                 f'Conservação da Loja: {empada.consLoja}',
                                 f'Estacionamento: {empada.estacionamento}',
                                 f'Possibilidade de Expansão: {empada.possExpansao}',
                                 f'Vitrine: {empada.vitrine}',
                                 f'IPTU: R${empada.iptu:.2f}',
                                 f'Concorrentes: {empada.numConco}',
                                 f'Custos de Implantação: R${empada.implantacao:.2f}',
                                 f'Total: {empada.total}')
                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(1150, 595, 115, 25)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaEmpa)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaEmpa.collidepoint(event.pos):
                    mapa.run(empada)

                elif foodTruck.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {foodTruck.tamanho}M²',
                                 f'Acessibilidade: {foodTruck.acessibilidade}',
                                 f'Ventilação: {foodTruck.ventilacao}',
                                 f'Iluminaçao: {foodTruck.iluminacao}',
                                 f'Ar Condicionado: {foodTruck.arCond}',
                                 f'Quantidade de banheiros: {foodTruck.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {foodTruck.tamCozinha}',
                                 f'Número de Assentos: {foodTruck.numAssentos}',
                                 f'Câmeras de Segurança: {foodTruck.camSeguranca}',
                                 f'Extintor de Incêndio: {foodTruck.extIncendio}',
                                 f'Alarmes de Segurança: {foodTruck.almSeguranca}',
                                 f'Wi-Fi: {foodTruck.wifi}',
                                 f'Conservação da Loja: {foodTruck.consLoja}',
                                 f'Estacionamento: {foodTruck.estacionamento}',
                                 f'Possibilidade de Expansão: {foodTruck.possExpansao}',
                                 f'Vitrine: {foodTruck.vitrine}',
                                 f'IPTU: R${foodTruck.iptu:.2f}',
                                 f'Concorrentes: {foodTruck.numConco}',
                                 f'Custos de Implantação: R${foodTruck.implantacao:.2f}',
                                 f'Total: {foodTruck.total}')
                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(1150, 595, 115, 25)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaFood)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaFood.collidepoint(event.pos):
                    mapa.run(foodTruck)

                elif hamburgueria.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {hamburgueria.tamanho}M²',
                                 f'Acessibilidade: {hamburgueria.acessibilidade}',
                                 f'Ventilação: {hamburgueria.ventilacao}',
                                 f'Iluminaçao: {hamburgueria.iluminacao}',
                                 f'Ar Condicionado: {hamburgueria.arCond}',
                                 f'Quantidade de banheiros: {hamburgueria.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {hamburgueria.tamCozinha}',
                                 f'Número de Assentos: {hamburgueria.numAssentos}',
                                 f'Câmeras de Segurança: {hamburgueria.camSeguranca}',
                                 f'Extintor de Incêndio: {hamburgueria.extIncendio}',
                                 f'Alarmes de Segurança: {hamburgueria.almSeguranca}',
                                 f'Wi-Fi: {hamburgueria.wifi}',
                                 f'Conservação da Loja: {hamburgueria.consLoja}',
                                 f'Estacionamento: {hamburgueria.estacionamento}',
                                 f'Possibilidade de Expansão: {hamburgueria.possExpansao}',
                                 f'Vitrine: {hamburgueria.vitrine}',
                                 f'IPTU: R${hamburgueria.iptu:.2f}',
                                 f'Concorrentes: {hamburgueria.numConco}',
                                 f'Custos de Implantação: R${hamburgueria.implantacao:.2f}',
                                 f'Total: {hamburgueria.total}')

                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(1150, 595, 115, 25)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaHamb)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaHamb.collidepoint(event.pos):
                    mapa.run(hamburgueria)

                elif lanchonete.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {lanchonete.tamanho}M²',
                                 f'Acessibilidade: {lanchonete.acessibilidade}',
                                 f'Ventilação: {lanchonete.ventilacao}',
                                 f'Iluminaçao: {lanchonete.iluminacao}',
                                 f'Ar Condicionado: {lanchonete.arCond}',
                                 f'Quantidade de banheiros: {lanchonete.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {lanchonete.tamCozinha}',
                                 f'Número de Assentos: {lanchonete.numAssentos}',
                                 f'Câmeras de Segurança: {lanchonete.camSeguranca}',
                                 f'Extintor de Incêndio: {lanchonete.extIncendio}',
                                 f'Alarmes de Segurança: {lanchonete.almSeguranca}',
                                 f'Wi-Fi: {lanchonete.wifi}',
                                 f'Conservação da Loja: {lanchonete.consLoja}',
                                 f'Estacionamento: {lanchonete.estacionamento}',
                                 f'Possibilidade de Expansão: {lanchonete.possExpansao}',
                                 f'Vitrine: {lanchonete.vitrine}',
                                 f'IPTU: R${lanchonete.iptu}',
                                 f'Concorrentes: {lanchonete.numConco}',
                                 f'Custos de Implantação: R${lanchonete.implantacao:.2f}',
                                 f'Total: {lanchonete.total}')

                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(1150, 595, 115, 25)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaLanche)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaLanche.collidepoint(event.pos):
                    mapa.run(lanchonete)

                elif lojaCachorroQuente.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {lojaCachorroQuente.tamanho}M²',
                                 f'Acessibilidade: {lojaCachorroQuente.acessibilidade}',
                                 f'Ventilação: {lojaCachorroQuente.ventilacao}',
                                 f'Iluminaçao: {lojaCachorroQuente.iluminacao}',
                                 f'Ar Condicionado: {lojaCachorroQuente.arCond}',
                                 f'Quantidade de banheiros: {lojaCachorroQuente.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {lojaCachorroQuente.tamCozinha}',
                                 f'Número de Assentos: {lojaCachorroQuente.numAssentos}',
                                 f'Câmeras de Segurança: {lojaCachorroQuente.camSeguranca}',
                                 f'Extintor de Incêndio: {lojaCachorroQuente.extIncendio}',
                                 f'Alarmes de Segurança: {lojaCachorroQuente.almSeguranca}',
                                 f'Wi-Fi: {lojaCachorroQuente.wifi}',
                                 f'Conservação da Loja: {lojaCachorroQuente.consLoja}',
                                 f'Estacionamento: {lojaCachorroQuente.estacionamento}',
                                 f'Possibilidade de Expansão: {lojaCachorroQuente.possExpansao}',
                                 f'Vitrine: {lojaCachorroQuente.vitrine}',
                                 f'IPTU: R${lojaCachorroQuente.iptu:.2f}',
                                 f'Concorrentes: {lojaCachorroQuente.numConco}',
                                 f'Custos de Implantação: R${lojaCachorroQuente.implantacao:.2f}',
                                 f'Total: {lojaCachorroQuente.total}')

                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(1150, 595, 115, 25)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaCacho)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaCacho.collidepoint(event.pos):
                    mapa.run(lojaCachorroQuente)

                elif pastelaria.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {pastelaria.tamanho}M²',
                                 f'Acessibilidade: {pastelaria.acessibilidade}',
                                 f'Ventilação: {pastelaria.ventilacao}',
                                 f'Iluminaçao: {pastelaria.iluminacao}',
                                 f'Ar Condicionado: {pastelaria.arCond}',
                                 f'Quantidade de banheiros: {pastelaria.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {pastelaria.tamCozinha}',
                                 f'Número de Assentos: {pastelaria.numAssentos}',
                                 f'Câmeras de Segurança: {pastelaria.camSeguranca}',
                                 f'Extintor de Incêndio: {pastelaria.extIncendio}',
                                 f'Alarmes de Segurança: {pastelaria.almSeguranca}',
                                 f'Wi-Fi: {pastelaria.wifi}',
                                 f'Conservação da Loja: {pastelaria.consLoja}',
                                 f'Estacionamento: {pastelaria.estacionamento}',
                                 f'Possibilidade de Expansão: {pastelaria.possExpansao}',
                                 f'Vitrine: {pastelaria.vitrine}',
                                 f'IPTU: R${pastelaria.iptu:.2f}',
                                 f'Concorrentes: {pastelaria.numConco}',
                                 f'Custos de Implantação: R${pastelaria.implantacao:.2f}',
                                 f'Total: {pastelaria.total}')
                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(1150, 595, 115, 25)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPas)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaPas.collidepoint(event.pos):
                    mapa.run(pastelaria)

                elif pizzaria.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {pizzaria.tamanho}M²',
                                 f'Acessibilidade: {pizzaria.acessibilidade}',
                                 f'Ventilação: {pizzaria.ventilacao}',
                                 f'Iluminaçao: {pizzaria.iluminacao}',
                                 f'Ar Condicionado: {pizzaria.arCond}',
                                 f'Quantidade de banheiros: {pizzaria.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {pizzaria.tamCozinha}',
                                 f'Número de Assentos: {pizzaria.numAssentos}',
                                 f'Câmeras de Segurança: {pizzaria.camSeguranca}',
                                 f'Extintor de Incêndio: {pizzaria.extIncendio}',
                                 f'Alarmes de Segurança: {pizzaria.almSeguranca}',
                                 f'Wi-Fi: {pizzaria.wifi}',
                                 f'Conservação da Loja: {pizzaria.consLoja}',
                                 f'Estacionamento: {pizzaria.estacionamento}',
                                 f'Possibilidade de Expansão: {pizzaria.possExpansao}',
                                 f'Vitrine: {pizzaria.vitrine}',
                                 f'IPTU: R${pizzaria.iptu:.2f}',
                                 f'Concorrentes: {pizzaria.numConco}',
                                 f'Custos de Implantação: R${pizzaria.implantacao:.2f}',
                                 f'Total: {pizzaria.total}')

                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPizz.update(1150, 595, 115, 25)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPizz)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaPizz.collidepoint(event.pos):
                    mapa.run(pizzaria)

                elif salgaderia.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200,
                                 f'Tamanho: {salgaderia.tamanho}M²',
                                 f'Acessibilidade: {salgaderia.acessibilidade}',
                                 f'Ventilação: {salgaderia.ventilacao}',
                                 f'Iluminaçao: {salgaderia.iluminacao}',
                                 f'Ar Condicionado: {salgaderia.arCond}',
                                 f'Quantidade de banheiros: {salgaderia.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {salgaderia.tamCozinha}',
                                 f'Número de Assentos: {salgaderia.numAssentos}',
                                 f'Câmeras de Segurança: {salgaderia.camSeguranca}',
                                 f'Extintor de Incêndio: {salgaderia.extIncendio}',
                                 f'Alarmes de Segurança: {salgaderia.almSeguranca}',
                                 f'Wi-Fi: {salgaderia.wifi}',
                                 f'Conservação da Loja: {salgaderia.consLoja}',
                                 f'Estacionamento: {salgaderia.estacionamento}',
                                 f'Possibilidade de Expansão: {salgaderia.possExpansao}',
                                 f'Vitrine: {salgaderia.vitrine}',
                                 f'IPTU: R${salgaderia.iptu:.2f}',
                                 f'Concorrentes: {salgaderia.numConco}',
                                 f'Custos de Implantação: R${salgaderia.implantacao:.2f}',
                                 f'Total: {salgaderia.total}')

                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(1150, 595, 115, 25)
                    confirmaSorv.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaSal)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaSal.collidepoint(event.pos):
                    mapa.run(salgaderia)

                elif sorveteria.rect.collidepoint(event.pos):
                    caixaDialogo(930, 200, f'Tamanho: {sorveteria.tamanho}M²',
                                 f'Acessibilidade: {sorveteria.acessibilidade}',
                                 f'Ventilação: {sorveteria.ventilacao}',
                                 f'Iluminaçao: {sorveteria.iluminacao}',
                                 f'Ar Condicionado: {sorveteria.arCond}',
                                 f'Quantidade de banheiros: {sorveteria.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {sorveteria.tamCozinha}',
                                 f'Número de Assentos: {sorveteria.numAssentos}',
                                 f'Câmeras de Segurança: {sorveteria.camSeguranca}',
                                 f'Extintor de Incêndio: {sorveteria.extIncendio}',
                                 f'Alarmes de Segurança: {sorveteria.almSeguranca}',
                                 f'Wi-Fi: {sorveteria.wifi}',
                                 f'Conservação da Loja: {sorveteria.consLoja}',
                                 f'Estacionamento: {sorveteria.estacionamento}',
                                 f'Possibilidade de Expansão: {sorveteria.possExpansao}',
                                 f'Vitrine: {sorveteria.vitrine}',
                                 f'IPTU: R${sorveteria.iptu:.2f}',
                                 f'Concorrentes: {sorveteria.numConco}',
                                 f'Custos de Implantação: R${sorveteria.implantacao:.2f}',
                                 f'Total: {sorveteria.total}')
                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSorv.update(1150, 595, 115, 25)
                    pygame.draw.rect(tela, BLACK, confirmaSorv)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaSal.collidepoint(event.pos):
                    mapa.run(sorveteria)

                    confirmaAcai.update(2000, 2000, 1, 1)
                    confirmaChurr.update(2000, 2000, 1, 1)
                    confirmaEmpa.update(2000, 2000, 1, 1)
                    confirmaFood.update(2000, 2000, 1, 1)
                    confirmaHamb.update(2000, 2000, 1, 1)
                    confirmaLanche.update(2000, 2000, 1, 1)
                    confirmaCacho.update(2000, 2000, 1, 1)
                    confirmaPas.update(2000, 2000, 1, 1)
                    confirmaPipoca.update(2000, 2000, 1, 1)
                    confirmaPizz.update(2000, 2000, 1, 1)
                    confirmaSal.update(2000, 2000, 1, 1)
                    confirmaSal.update(1150, 595, 115, 25)
                pygame.draw.rect(tela, BLACK, confirmaSorv)
                tela.blit(main_font.render('CONFIRMA', True, WHITE), (1151, 595))
                if confirmaSorv.collidepoint(event.pos):
                    mapa.run(sorveteria)


            tela.blit(main_font.render('Açaiteria', True, BLACK), (37, 250))
            tela.blit(main_font.render('Carro da Pipoca', True, BLACK), (235, 250))
            tela.blit(main_font.render('Carro do Churros', True, BLACK), (455, 250))
            tela.blit(main_font.render('Loja de Empada', True, BLACK), (693, 250))

            tela.blit(main_font.render('Foodtruck', True, BLACK), (33, 440))
            tela.blit(main_font.render('Hamburgueria', True, BLACK), (242, 440))
            tela.blit(main_font.render('Lanchonete', True, BLACK), (487, 440))
            tela.blit(main_font.render('Cachorro-Quente', True, BLACK), (690, 440))

            tela.blit(main_font.render('Pastelaria', True, BLACK), (33, 630))
            tela.blit(main_font.render('Pizzaria', True, BLACK), (277, 630))
            tela.blit(main_font.render('Salgaderia', True, BLACK), (494, 630))
            tela.blit(main_font.render('Sorveteria', True, BLACK), (727, 630))

        placas = pygame.sprite.Group()
        placas.add(acaiteria, carrinhoPipoca, carroChurros, empada, foodTruck, hamburgueria,
                   lanchonete, lojaCachorroQuente, pastelaria, pizzaria, salgaderia, sorveteria, voltar)
        placas.draw(tela)
        pygame.display.flip()
        pygame.display.update()
