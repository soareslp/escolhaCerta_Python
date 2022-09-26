import sys, botao, intro
from config import *


def run():
    # Imagens
    empresa = pygame.image.load('imagens/tutorial/tuto1.png')
    mapa1 = pygame.image.load('imagens/tutorial/tuto2.png')
    mapa2 = pygame.image.load('imagens/tutorial/tuto3.png')
    mapa3 = pygame.image.load('imagens/tutorial/tuto4.png')
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
            tela.blit(titulo_font.render('Tutorial', True, BLACK), (LARGURA / 2 - 150, ALTURA / 2 - 375))
            tela.blit(main_font.render('1º: Ao inciar o jogo selecione e confirme a empresa para jogar:', True, BLACK), (LARGURA / 2 - 680, ALTURA / 2 - 280))
            tela.blit(empresa, (3, ALTURA / 2 - 250))

            tela.blit(main_font.render('2º: Clique nos pontos para ver as suas características:', True, BLACK),
                      (LARGURA / 2, ALTURA / 2 - 280))
            tela.blit(mapa1, (LARGURA / 2, ALTURA / 2 - 250))

            tela.blit(main_font.render('3º: No info terá as características da empresa escolhida:', True, BLACK),
                      (3, ALTURA / 2 + 60))
            tela.blit(mapa2, (3, ALTURA / 2 + 82))

            tela.blit(main_font.render('4º: Ao escolher o ponto de venda será mostrado o resultado:', True, BLACK),
                      (LARGURA / 2, ALTURA / 2 + 60))
            tela.blit(mapa3, (LARGURA / 2, ALTURA / 2 + 82))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if voltar.rect.collidepoint(event.pos):
                    intro.run()

        placas = pygame.sprite.Group()
        placas.add(voltar)
        placas.draw(tela)
        pygame.display.flip()
        pygame.display.update()
