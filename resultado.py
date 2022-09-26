import sys, intro, botao
from config import *


def run(loja, empresa):
    voltar = botao.Botao((LARGURA - 65), (ALTURA - 75), 'imagens/tutorial/voltar.png')
    background = pygame.image.load('imagens/cackground/fundo.jpg')
    tela.blit(background, (0, 0))

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
                if voltar.rect.collidepoint(event.pos):
                    intro.run()

            tela.blit(titulo_font.render('Resultado da partida:', True, BLUE), (LARGURA / 2 - 375, ALTURA / 2 - 325))
            tela.blit(main_font.render('Empresa escolhida:', True, BLACK), (LARGURA / 2 - 650, ALTURA / 2 - 150))
            caixaDialogo(30, 260, f'Tamanho: {empresa.tamanho}M²',
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


            tela.blit(main_font.render('Ponto de venda escolhido:', True, BLACK), (LARGURA / 2 - 200, ALTURA / 2 - 150))
            caixaDialogo(480, 260, f'Tamanho: {loja.tamanho}M²',
                         f'Acessibilidade: {loja.acessibilidade}',
                         f'Ventilação: {loja.ventilacao}',
                         f'Iluminaçao: {loja.iluminacao}',
                         f'Ar Condicionado: {loja.arCond}',
                         f'Quantidade de banehiros: {loja.qtdBanheiro}',
                         f'Tamanho da Cozinha: {loja.tamCozinha}',
                         f'Número de Assentos: {loja.numAssentos}',
                         f'Câmeras de Segurança: {loja.camSeguranca}',
                         f'Extintor de Incêndio: {loja.extIncendio}',
                         f'Alarmes de Segurança: {loja.almSeguranca}',
                         f'Wi-Fi: {loja.wifi}',
                         f'Conservação da Loja: {loja.consLoja}',
                         f'Estacionamento: {loja.estacionamento}',
                         f'Possibilidade de Expansão: {loja.possExpansao}',
                         f'Vitrine: {loja.vitrine}',
                         f'IPTU: R${loja.iptu:.2f}',
                         f'Concorrentes: {loja.numConco}',
                         f'Custos de Implantação: R${loja.implantacao:.2f}',
                         f'Total: {loja.total}')


            tela.blit(main_font.render('Aderência:', True, BLACK), (LARGURA / 2 + 275, ALTURA / 2 - 150))
            caixaSimples(955, 260)
            tela.blit(main_font.render(f'Realizando a análise dos fatores', True, BLUE),
                      (LARGURA / 2 + 280, ALTURA / 2 - 120))
            tela.blit(main_font.render(f'necessários da empresa com os', True, BLUE),
                      (LARGURA / 2 + 280, ALTURA / 2 - 100))
            tela.blit(main_font.render(f'do ponto de venda escolhido o', True, BLUE),
                      (LARGURA / 2 + 280, ALTURA / 2 - 80))
            tela.blit(main_font.render(f'resultado da tomada de decisão do', True, BLUE),
                      (LARGURA / 2 + 280, ALTURA / 2 - 60))
            tela.blit(main_font.render(f'jogador foi de:', True, BLUE),
                      (LARGURA / 2 + 280, ALTURA / 2 - 40))
            tela.blit(main_font.render(f'Aderência de: {calculaAderência(loja, empresa):.2f}%', True, BLUE),
                      (LARGURA / 2 + 280, ALTURA / 2 + 40))
            if calculaAderência(loja, empresa) == 100:
                tela.blit(main_font.render(f'Exelente! A escolha do ponto foi', True, GREEN),
                          (LARGURA / 2 + 280, ALTURA / 2 + 120))
                tela.blit(main_font.render(f'totalmente aderente à empresa', True, GREEN),
                          (LARGURA / 2 + 280, ALTURA / 2 + 140))
                tela.blit(main_font.render(f'escolhida', True, GREEN),
                          (LARGURA / 2 + 280, ALTURA / 2 + 160))
            elif 75 < calculaAderência(loja, empresa) < 100 or 100 < calculaAderência(loja, empresa) < 125:
                tela.blit(main_font.render(f'Muito bom! A escolha do ponto foi', True, BLUE),
                          (LARGURA / 2 + 280, ALTURA / 2 + 120))
                tela.blit(main_font.render(f'aderente à empresa escolhida.', True, BLUE),
                          (LARGURA / 2 + 280, ALTURA / 2 + 140))

            else:
                tela.blit(main_font.render(f'MÁ ESCOLHA! A escolha do ponto', True, RED),
                          (LARGURA / 2 + 280, ALTURA / 2 + 120))
                tela.blit(main_font.render(f'não foi aderente à empresa', True, RED),
                          (LARGURA / 2 + 280, ALTURA / 2 + 140))
                tela.blit(main_font.render(f'escolhida', True, RED),
                          (LARGURA / 2 + 280, ALTURA / 2 + 160))



        placas = pygame.sprite.Group()
        placas.add(voltar)
        pygame.display.flip()
        pygame.display.update()
