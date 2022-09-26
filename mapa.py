import loja, sys, resultado, botao
from config import *


def run(empresa):
    mapa = pygame.image.load('imagens/cackground/mapa.png')
    tela.blit(mapa, (0, 0))

    # Loja de 1M²
    ponto = loja.Loja(223, 50, 'imagens\placas\placa1m.png', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1000, 0, 700,
                      32)

    # Loja de 3M²      236, 327
    ponto3 = loja.Loja(297, 140, 'imagens\placas\placa3m.png', 3, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 700, 0, 1500,
                       36)

    # Loja de 4M²
    ponto4 = loja.Loja(753, 510, 'imagens\placas\placa4m.png', 4, 0, 6, 6, 0, 0, 2, 8, 5, 10, 10, 0, 10, 10, 10, 0, 1300, 1,
                       1700, 95)
    # Loja de 5M²
    ponto5 = loja.Loja(581, 427, 'imagens\placas\placa5m.png', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 600, 0, 2000,
                       32)

    # Loja de 7M²
    ponto7 = loja.Loja(40, 561, 'imagens\placas\placa7m.png', 7, 0, 4, 5, 0, 2, 2, 8, 5, 0, 10, 0, 5, 0, 10, 10, 800, 1, 1700,
                       84)

    # Loja de 15M²      410, 123
    ponto15 = loja.Loja(180, 410, 'imagens\placas\placa15m.png', 15, 0, 6, 6, 0, 1, 4, 10, 5, 10, 0, 0, 6, 0, 0, 0, 2000, 2,
                        4000, 58)

    # Loja de 16M²
    ponto16 = loja.Loja(1143, 75, 'imagens\placas\placa16m.png', 16, 0, 5, 4, 0, 0, 3, 5, 5, 0, 0, 0, 6, 0, 0, 0, 1100, 0,
                        2500, 46)

    # Loja de 24M²      915, 350
    ponto24 = loja.Loja(1260, 135, 'imagens\placas\placa24m.png', 24, 0, 6, 6, 0, 2, 5, 15, 5, 10, 10, 0, 7, 0, 10, 0, 2300, 0,
                        4500, 101)

    # Loja de 26M²
    ponto26 = loja.Loja(190, 670, 'imagens\placas\placa26m.png', 26, 0, 8, 9, 0, 2, 2, 25, 10, 10, 10, 0, 7, 0, 10, 0, 2800, 0,
                        2500, 106)

    # Loja de 40M²
    ponto40 = loja.Loja(470, 610, 'imagens\placas\placa40m.png', 40, 0, 7, 8, 0, 2, 6, 20, 10, 10, 10, 10, 7, 10, 0, 0, 2500,
                        0, 5000, 117)

    # Loja de 55M²      1107, 327
    ponto55 = loja.Loja(1150, 327, 'imagens\placas\placa55m.png', 55, 10, 8, 7, 10, 2, 8, 25, 10, 10, 10, 10, 9, 0, 10, 0,
                        3000, 1, 7000, 141)

    # Loja de 67M²
    ponto67 = loja.Loja(970, 480, 'imagens\placas\placa67m.png', 67, 10, 10, 10, 10, 4, 7, 30, 10, 10, 10, 10, 8, 10, 0, 0,
                        3300, 3, 6000, 143)

    info = botao.Botao(20, 690, 'imagens/botoes/info2.png')

    confirmaPonto1 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto3 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto4 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto5 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto7 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto15 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto16 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto24 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto26 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto40 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto55 = pygame.Rect(565, 395, 115, 25)
    confirmaPonto67 = pygame.Rect(565, 395, 115, 25)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ponto.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto.tamanho}M²',
                                 f'Acessibilidade: {ponto.acessibilidade}',
                                 f'Ventilação: {ponto.ventilacao}',
                                 f'Iluminaçao: {ponto.iluminacao}',
                                 f'Ar Condicionado: {ponto.arCond}',
                                 f'Quantidade de banheiros: {ponto.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto.tamCozinha}',
                                 f'Número de Assentos: {ponto.numAssentos}',
                                 f'Câmeras de Segurança: {ponto.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto.extIncendio}',
                                 f'Alarmes de Segurança: {ponto.almSeguranca}',
                                 f'Wi-Fi: {ponto.wifi}',
                                 f'Conservação da Loja: {ponto.consLoja}',
                                 f'Estacionamento: {ponto.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto.possExpansao}',
                                 f'Vitrine: {ponto.vitrine}',
                                 f'IPTU: R${ponto.iptu:.2f}',
                                 f'Concorrentes: {ponto.numConco}',
                                 f'Custos de Implantação: R${ponto.implantacao:.2f}',
                                 f'Total: {ponto.total}')

                    confirmaPonto1.update(565, 395, 115, 25)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto1)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto1.collidepoint(event.pos):
                    resultado.run(ponto, empresa)

                elif ponto3.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto3.tamanho}M²',
                                 f'Acessibilidade: {ponto3.acessibilidade}',
                                 f'Ventilação: {ponto3.ventilacao}',
                                 f'Iluminaçao: {ponto3.iluminacao}',
                                 f'Ar Condicionado: {ponto3.arCond}',
                                 f'Quantidade de banheiros: {ponto3.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto3.tamCozinha}',
                                 f'Número de Assentos: {ponto3.numAssentos}',
                                 f'Câmeras de Segurança: {ponto3.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto3.extIncendio}',
                                 f'Alarmes de Segurança: {ponto3.almSeguranca}',
                                 f'Wi-Fi: {ponto3.wifi}',
                                 f'Conservação da Loja: {ponto3.consLoja}',
                                 f'Estacionamento: {ponto3.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto3.possExpansao}',
                                 f'Vitrine: {ponto3.vitrine}',
                                 f'IPTU: R${ponto3.iptu:.2f}',
                                 f'Concorrentes: {ponto3.numConco}',
                                 f'Custos de Implantação: R${ponto3.implantacao:.2f}',
                                 f'Total: {ponto3.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(565, 395, 115, 25)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto3)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto3.collidepoint(event.pos):
                    resultado.run(ponto3, empresa)

                elif ponto4.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto4.tamanho}M²',
                                 f'Acessibilidade: {ponto4.acessibilidade}',
                                 f'Ventilação: {ponto4.ventilacao}',
                                 f'Iluminaçao: {ponto4.iluminacao}',
                                 f'Ar Condicionado: {ponto4.arCond}',
                                 f'Quantidade de banheiros: {ponto4.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto4.tamCozinha}',
                                 f'Número de Assentos: {ponto4.numAssentos}',
                                 f'Câmeras de Segurança: {ponto4.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto4.extIncendio}',
                                 f'Alarmes de Segurança: {ponto4.almSeguranca}',
                                 f'Wi-Fi: {ponto4.wifi}',
                                 f'Conservação da Loja: {ponto4.consLoja}',
                                 f'Estacionamento: {ponto4.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto4.possExpansao}',
                                 f'Vitrine: {ponto4.vitrine}',
                                 f'IPTU: R${ponto4.iptu:.2f}',
                                 f'Concorrentes: {ponto4.numConco}',
                                 f'Custos de Implantação: R${ponto4.implantacao:.2f}',
                                 f'Total: {ponto4.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(565, 395, 115, 25)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto4)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto4.collidepoint(event.pos):
                    resultado.run(ponto4, empresa)

                elif ponto5.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto5.tamanho}M²',
                                 f'Acessibilidade: {ponto5.acessibilidade}',
                                 f'Ventilação: {ponto5.ventilacao}',
                                 f'Iluminaçao: {ponto5.iluminacao}',
                                 f'Ar Condicionado: {ponto5.arCond}',
                                 f'Quantidade de banheiros: {ponto5.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto5.tamCozinha}',
                                 f'Número de Assentos: {ponto5.numAssentos}',
                                 f'Câmeras de Segurança: {ponto5.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto5.extIncendio}',
                                 f'Alarmes de Segurança: {ponto5.almSeguranca}',
                                 f'Wi-Fi: {ponto5.wifi}',
                                 f'Conservação da Loja: {ponto5.consLoja}',
                                 f'Estacionamento: {ponto5.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto5.possExpansao}',
                                 f'Vitrine: {ponto5.vitrine}',
                                 f'IPTU: R${ponto5.iptu:.2f}',
                                 f'Concorrentes: {ponto5.numConco}',
                                 f'Custos de Implantação: R${ponto5.implantacao:.2f}',
                                 f'Total: {ponto5.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(565, 395, 115, 25)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto5)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto5.collidepoint(event.pos):
                    resultado.run(ponto5, empresa)

                elif ponto7.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto7.tamanho}M²',
                                 f'Acessibilidade: {ponto7.acessibilidade}',
                                 f'Ventilação: {ponto7.ventilacao}',
                                 f'Iluminaçao: {ponto7.iluminacao}',
                                 f'Ar Condicionado: {ponto7.arCond}',
                                 f'Quantidade de banheiros: {ponto7.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto7.tamCozinha}',
                                 f'Número de Assentos: {ponto7.numAssentos}',
                                 f'Câmeras de Segurança: {ponto7.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto7.extIncendio}',
                                 f'Alarmes de Segurança: {ponto7.almSeguranca}',
                                 f'Wi-Fi: {ponto7.wifi}',
                                 f'Conservação da Loja: {ponto7.consLoja}',
                                 f'Estacionamento: {ponto7.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto7.possExpansao}',
                                 f'Vitrine: {ponto7.vitrine}',
                                 f'IPTU: R${ponto7.iptu:.2f}',
                                 f'Concorrentes: {ponto7.numConco}',
                                 f'Custos de Implantação: R${ponto7.implantacao:.2f}',
                                 f'Total: {ponto7.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(565, 395, 115, 25)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto7)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto7.collidepoint(event.pos):
                    resultado.run(ponto7, empresa)

                elif ponto15.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto15.tamanho}M²',
                                 f'Acessibilidade: {ponto15.acessibilidade}',
                                 f'Ventilação: {ponto15.ventilacao}',
                                 f'Iluminaçao: {ponto15.iluminacao}',
                                 f'Ar Condicionado: {ponto15.arCond}',
                                 f'Quantidade de banheiros: {ponto15.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto15.tamCozinha}',
                                 f'Número de Assentos: {ponto15.numAssentos}',
                                 f'Câmeras de Segurança: {ponto15.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto15.extIncendio}',
                                 f'Alarmes de Segurança: {ponto15.almSeguranca}',
                                 f'Wi-Fi: {ponto15.wifi}',
                                 f'Conservação da Loja: {ponto15.consLoja}',
                                 f'Estacionamento: {ponto15.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto15.possExpansao}',
                                 f'Vitrine: {ponto15.vitrine}',
                                 f'IPTU: R${ponto15.iptu:.2f}',
                                 f'Concorrentes: {ponto15.numConco}',
                                 f'Custos de Implantação: R${ponto15.implantacao:.2f}',
                                 f'Total: {ponto15.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(565, 395, 115, 25)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto15)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto15.collidepoint(event.pos):
                    resultado.run(ponto15, empresa)

                elif ponto16.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto16.tamanho}M²',
                                 f'Acessibilidade: {ponto16.acessibilidade}',
                                 f'Ventilação: {ponto16.ventilacao}',
                                 f'Iluminaçao: {ponto16.iluminacao}',
                                 f'Ar Condicionado: {ponto16.arCond}',
                                 f'Quantidade de banheiros: {ponto16.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto16.tamCozinha}',
                                 f'Número de Assentos: {ponto16.numAssentos}',
                                 f'Câmeras de Segurança: {ponto16.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto16.extIncendio}',
                                 f'Alarmes de Segurança: {ponto16.almSeguranca}',
                                 f'Wi-Fi: {ponto16.wifi}',
                                 f'Conservação da Loja: {ponto16.consLoja}',
                                 f'Estacionamento: {ponto16.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto16.possExpansao}',
                                 f'Vitrine: {ponto16.vitrine}',
                                 f'IPTU: R${ponto16.iptu}',
                                 f'Concorrentes: {ponto16.numConco}',
                                 f'Custos de Implantação: R${ponto16.implantacao:.2f}',
                                 f'Total: {ponto16.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(565, 395, 115, 25)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto16)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto16.collidepoint(event.pos):
                    resultado.run(ponto16, empresa)

                elif ponto24.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto24.tamanho}M²',
                                 f'Acessibilidade: {ponto24.acessibilidade}',
                                 f'Ventilação: {ponto24.ventilacao}',
                                 f'Iluminaçao: {ponto24.iluminacao}',
                                 f'Ar Condicionado: {ponto24.arCond}',
                                 f'Quantidade de banheiros: {ponto24.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto24.tamCozinha}',
                                 f'Número de Assentos: {ponto24.numAssentos}',
                                 f'Câmeras de Segurança: {ponto24.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto24.extIncendio}',
                                 f'Alarmes de Segurança: {ponto24.almSeguranca}',
                                 f'Wi-Fi: {ponto24.wifi}',
                                 f'Conservação da Loja: {ponto24.consLoja}',
                                 f'Estacionamento: {ponto24.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto24.possExpansao}',
                                 f'Vitrine: {ponto24.vitrine}',
                                 f'IPTU: R${ponto24.iptu:.2f}',
                                 f'Concorrentes: {ponto24.numConco}',
                                 f'Custos de Implantação: R${ponto24.implantacao:.2f}',
                                 f'Total: {ponto24.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(565, 395, 115, 25)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto24)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto24.collidepoint(event.pos):
                    resultado.run(ponto24, empresa)

                elif ponto26.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto26.tamanho}M²',
                                 f'Acessibilidade: {ponto26.acessibilidade}',
                                 f'Ventilação: {ponto26.ventilacao}',
                                 f'Iluminaçao: {ponto26.iluminacao}',
                                 f'Ar Condicionado: {ponto26.arCond}',
                                 f'Quantidade de banheiros: {ponto26.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto26.tamCozinha}',
                                 f'Número de Assentos: {ponto26.numAssentos}',
                                 f'Câmeras de Segurança: {ponto26.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto26.extIncendio}',
                                 f'Alarmes de Segurança: {ponto26.almSeguranca}',
                                 f'Wi-Fi: {ponto26.wifi}',
                                 f'Conservação da Loja: {ponto26.consLoja}',
                                 f'Estacionamento: {ponto26.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto26.possExpansao}',
                                 f'Vitrine: {ponto26.vitrine}',
                                 f'IPTU: R${ponto26.iptu:.2f}',
                                 f'Concorrentes: {ponto26.numConco}',
                                 f'Custos de Implantação: R${ponto26.implantacao:.2f}',
                                 f'Total: {ponto26.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(565, 395, 115, 25)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto26)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto26.collidepoint(event.pos):
                    resultado.run(ponto26, empresa)

                elif ponto40.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto40.tamanho}M²',
                                 f'Acessibilidade: {ponto40.acessibilidade}',
                                 f'Ventilação: {ponto40.ventilacao}',
                                 f'Iluminaçao: {ponto40.iluminacao}',
                                 f'Ar Condicionado: {ponto40.arCond}',
                                 f'Quantidade de banheiros: {ponto40.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto40.tamCozinha}',
                                 f'Número de Assentos: {ponto40.numAssentos}',
                                 f'Câmeras de Segurança: {ponto40.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto40.extIncendio}',
                                 f'Alarmes de Segurança: {ponto40.almSeguranca}',
                                 f'Wi-Fi: {ponto40.wifi}',
                                 f'Conservação da Loja: {ponto40.consLoja}',
                                 f'Estacionamento: {ponto40.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto40.possExpansao}',
                                 f'Vitrine: {ponto40.vitrine}',
                                 f'IPTU: R${ponto40.iptu:.2f}',
                                 f'Concorrentes: {ponto40.numConco}',
                                 f'Custos de Implantação: R${ponto40.implantacao:.2f}',
                                 f'Total: {ponto40.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(565, 395, 115, 25)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto40)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto40.collidepoint(event.pos):
                    resultado.run(ponto40, empresa)

                elif ponto55.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto55.tamanho}M²',
                                 f'Acessibilidade: {ponto55.acessibilidade}',
                                 f'Ventilação: {ponto55.ventilacao}',
                                 f'Iluminaçao: {ponto55.iluminacao}',
                                 f'Ar Condicionado: {ponto55.arCond}',
                                 f'Quantidade de banheiros: {ponto55.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto55.tamCozinha}',
                                 f'Número de Assentos: {ponto55.numAssentos}',
                                 f'Câmeras de Segurança: {ponto55.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto55.extIncendio}',
                                 f'Alarmes de Segurança: {ponto55.almSeguranca}',
                                 f'Wi-Fi: {ponto55.wifi}',
                                 f'Conservação da Loja: {ponto55.consLoja}',
                                 f'Estacionamento: {ponto55.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto55.possExpansao}',
                                 f'Vitrine: {ponto55.vitrine}',
                                 f'IPTU: R${ponto55.iptu:.2f}',
                                 f'Concorrentes: {ponto55.numConco}',
                                 f'Custos de Implantação: R${ponto55.implantacao:.2f}',
                                 f'Total: {ponto55.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(565, 395, 115, 25)
                    confirmaPonto67.update(2000, 2000, 1, 1)
                    pygame.draw.rect(tela, BLACK, confirmaPonto55)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto55.collidepoint(event.pos):
                    resultado.run(ponto55, empresa)

                elif ponto67.rect.collidepoint(event.pos):
                    caixaDialogo(345, 0,
                                 f'Tamanho: {ponto67.tamanho}M²',
                                 f'Acessibilidade: {ponto67.acessibilidade}',
                                 f'Ventilação: {ponto67.ventilacao}',
                                 f'Iluminaçao: {ponto67.iluminacao}',
                                 f'Ar Condicionado: {ponto67.arCond}',
                                 f'Quantidade de banheiros: {ponto67.qtdBanheiro}',
                                 f'Tamanho da Cozinha: {ponto67.tamCozinha}',
                                 f'Número de Assentos: {ponto67.numAssentos}',
                                 f'Câmeras de Segurança: {ponto67.camSeguranca}',
                                 f'Extintor de Incêndio: {ponto67.extIncendio}',
                                 f'Alarmes de Segurança: {ponto67.almSeguranca}',
                                 f'Wi-Fi: {ponto67.wifi}',
                                 f'Conservação da Loja: {ponto67.consLoja}',
                                 f'Estacionamento: {ponto67.estacionamento}',
                                 f'Possibilidade de Expansão: {ponto67.possExpansao}',
                                 f'Vitrine: {ponto67.vitrine}',
                                 f'IPTU: R${ponto67.iptu:.2f}',
                                 f'Concorrentes: {ponto67.numConco}',
                                 f'Custos de Implantação: R${ponto67.implantacao:.2f}',
                                 f'Total: {ponto67.total}')

                    confirmaPonto1.update(2000, 2000, 1, 1)
                    confirmaPonto3.update(2000, 2000, 1, 1)
                    confirmaPonto4.update(2000, 2000, 1, 1)
                    confirmaPonto5.update(2000, 2000, 1, 1)
                    confirmaPonto7.update(2000, 2000, 1, 1)
                    confirmaPonto15.update(2000, 2000, 1, 1)
                    confirmaPonto16.update(2000, 2000, 1, 1)
                    confirmaPonto24.update(2000, 2000, 1, 1)
                    confirmaPonto26.update(2000, 2000, 1, 1)
                    confirmaPonto40.update(2000, 2000, 1, 1)
                    confirmaPonto55.update(2000, 2000, 1, 1)
                    confirmaPonto67.update(565, 395, 115, 25)
                    pygame.draw.rect(tela, BLACK, confirmaPonto67)
                    tela.blit(main_font.render('CONFIRMA', True, WHITE), (566, 395))
                if confirmaPonto67.collidepoint(event.pos):
                    resultado.run(ponto67, empresa)

                elif info.rect.collidepoint(event.pos):
                    caixaDialogo(700, 0, f'Tamanho: {empresa.tamanho}M²',
                     f'Acessibilidade: {empresa.acessibilidade}',
                     f'Ventilação: {empresa.ventilacao}',
                     f'Iluminaçao: {empresa.iluminacao}',
                     f'Ar Condicionado: {empresa.arCond}',
                     f'Quantidade de banehiros: {empresa.qtdBanheiro}',
                     f'Tamanho da Cozinha: {empresa.tamCozinha}',
                     f'Número de Assentos: {empresa.numAssentos}',
                     f'Câmeras de Segurança: {empresa.camSeguranca}',
                     f'Extintor de Incêndio: {empresa.extIncendio}',
                     f'Alarmes de Segurança: {empresa.almSeguranca}',
                     f'Wi-Fi: {empresa.wifi}',
                     f'Conservação da Loja: {empresa.consLoja}',
                     f'Estacionamento: {empresa.estacionamento}',
                     f'Possibilidade de Expansão: {empresa.possExpansao}',
                     f'Vitrine: {empresa.vitrine}',
                     f'IPTU: R${empresa.iptu:.2f}',
                     f'Concorrentes: {empresa.numConco}',
                     f'Custos de Implantação: R${empresa.implantacao:.2f}',
                     f'Total: {empresa.total}')

        # Desenhando na tela
        placas = pygame.sprite.Group()
        placas.add(ponto, ponto3, ponto4, ponto5, ponto7, ponto15, ponto16, ponto24, ponto26, ponto40, ponto55, ponto67,
                   info)
        placas.draw(tela)
        pygame.display.flip()
        pygame.display.update()
