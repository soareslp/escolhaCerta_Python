import pygame


def caixaDialogo(x, y, texto, texto2, texto3, texto4, texto5, texto6, texto7, texto8, texto9, texto10, texto11, texto12,
                 texto13, texto14, texto15, texto16, texto17, texto18, texto19, texto20):
    caixa = pygame.Rect(x, y, 350, 425)
    pygame.draw.rect(tela, PINK, caixa)
    tela.blit(main_font.render(texto, True, BLUE), (x + 5, y + 5))
    tela.blit(main_font.render(texto2, True, BLUE), (x + 5, y + 25))
    tela.blit(main_font.render(texto3, True, BLUE), (x + 5, y + 45))
    tela.blit(main_font.render(texto4, True, BLUE), (x + 5, y + 65))
    tela.blit(main_font.render(texto5, True, BLUE), (x + 5, y + 85))
    tela.blit(main_font.render(texto6, True, BLUE), (x + 5, y + 105))
    tela.blit(main_font.render(texto7, True, BLUE), (x + 5, y + 125))
    tela.blit(main_font.render(texto8, True, BLUE), (x + 5, y + 145))
    tela.blit(main_font.render(texto9, True, BLUE), (x + 5, y + 165))
    tela.blit(main_font.render(texto10, True, BLUE), (x + 5, y + 185))
    tela.blit(main_font.render(texto11, True, BLUE), (x + 5, y + 205))
    tela.blit(main_font.render(texto12, True, BLUE), (x + 5, y + 225))
    tela.blit(main_font.render(texto13, True, BLUE), (x + 5, y + 245))
    tela.blit(main_font.render(texto14, True, BLUE), (x + 5, y + 265))
    tela.blit(main_font.render(texto15, True, BLUE), (x + 5, y + 285))
    tela.blit(main_font.render(texto16, True, BLUE), (x + 5, y + 305))
    tela.blit(main_font.render(texto17, True, BLUE), (x + 5, y + 325))
    tela.blit(main_font.render(texto18, True, BLUE), (x + 5, y + 345))
    tela.blit(main_font.render(texto19, True, BLUE), (x + 5, y + 365))
    tela.blit(main_font.render(texto20, True, BLUE), (x + 5, y + 385))


def caixaSimples(x, y):
    caixa = pygame.Rect(x, y, 350, 400)
    pygame.draw.rect(tela, PINK, caixa)


def calculaAderência(loja, empresa):
    totalAderencia = (empresa.total / loja.total)*100
    return totalAderencia


pygame.init()

#Tela
LARGURA = 1366
ALTURA = 768
tela = pygame.display.set_mode((LARGURA, ALTURA))

#FONTES
titulo_font = pygame.font.Font('fonts\ookman-old-style.ttf', 72)
main_font = pygame.font.Font('fonts\ookman-old-style.ttf', 20)

#CORES
PINK = (252, 228, 236)
BLUE = (61, 90, 254)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (50, 200, 50)
