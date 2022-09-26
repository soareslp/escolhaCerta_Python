import sys, botao, empresas, tutorial
from config import *

def run():
    background = pygame.image.load('imagens/cackground/fundoIntro.jpg')
    logo = botao.Botao(LARGURA / 2 - 256, ALTURA / 2 - 300, 'imagens/botoes/logo3.png')
    novoJogo = botao.Botao(LARGURA / 2 - 48, ALTURA / 2, 'imagens/botoes/novoJogo.png')
    tutorialButton = botao.Botao(LARGURA / 2 - 48, ALTURA / 2 + 100, 'imagens/botoes/tutorial.png')
    sair = botao.Botao(LARGURA / 2 - 48, ALTURA / 2 + 200, 'imagens/botoes/sair.png')
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
                if novoJogo.rect.collidepoint(event.pos):
                    empresas.run()

                if tutorialButton.rect.collidepoint(event.pos):
                    tutorial.run()

                if sair.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        placas = pygame.sprite.Group()
        placas.add(novoJogo, tutorialButton, sair, logo)
        placas.draw(tela)
        pygame.display.flip()
        pygame.display.update()