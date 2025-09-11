# %%
from typing import Any
from sys import exit
from classes import Botao
from classes import InputBox
from classes import Puzzle
import pygame

pygame.init()
altura = 800
largura = 600
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption("STAR PUZZLE")

botaojogar = pygame.image.load("Imagens\\Botoes\\jogar.png").convert_alpha()
botaocomojogar = pygame.image.load("Imagens\\Botoes\\comojogar.png").convert_alpha()
botaosair = pygame.image.load("Imagens\\Botoes\\sair.png").convert_alpha()
titulo = pygame.image.load("Imagens\\Titulo.png").convert_alpha()
boxvazia = pygame.image.load("Imagens\\boxvazia.png").convert_alpha()
grid = pygame.image.load("Imagens\\Puzzle\\grid.png").convert_alpha()
estrela = pygame.image.load("Imagens\\Puzzle\\estrela.png").convert_alpha()
ponto = pygame.image.load("Imagens\\Puzzle\\ponto.png").convert_alpha()

fonteprincipal = pygame.font.Font("Fontes\\Kodchasan\\Kodchasan-Regular.ttf", 30)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
BACKGROUND = (33, 110, 116)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
BACKGROUND = (33, 110, 116)
VERMELHO = (245, 101, 101)
VERDE = (90, 172, 136)
LARANJA = (202, 137, 16)
AMARELO = (248, 233, 188)
AZUL = (23, 55, 115)
ROXO = (182, 89, 213)
ROSA = (210, 144, 188)
TURQUESA = (163, 217, 229)

CORESPUZZLE = {1: VERMELHO, 2: VERDE, 3: LARANJA, 4: AMARELO, 5: AZUL, 6: ROXO, 7: ROSA, 8: TURQUESA}
            
rodando = True
jogoativo = False

exibindo = "menu"
gridcells = [[0 for _ in range(8)] for _ in range(8)]
seed = InputBox((165, 35), (312, 25), fonteprincipal, BRANCO, PRETO, 8, "Seed:")
game = Puzzle(grid, (197, 80), CORESPUZZLE, estrela, ponto, 401, 49, gridcells)

while rodando:
    bjogar = Botao((300, 250), botaojogar)
    bcomojogar = Botao((300, 350), botaocomojogar)
    bsairgame = Botao((400, 500), botaosair)
    bsairhowtoplay = Botao((300, 400), botaosair)
    tela.fill(BACKGROUND)

    if exibindo == "menu":
        tela.blit(titulo, (225, 100))
        bjogar.criar(tela)
        bcomojogar.criar(tela)

    elif exibindo == "game":
        seed.criar(tela)
        pygame.draw.rect(tela, BRANCO, pygame.Rect(197, 80, 401, 401))
        
        if seed.input != "" or seed.input is None:
            game.desenharpuzzle(tela)
            game.desenhar_ponto_estrela(tela)
            jogoativo = True

            if game.vitoria():
                print("x")
            
        bsairgame.criar(tela)

    elif exibindo == "howtoplay":
        bsairhowtoplay.criar(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            exit()
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if exibindo == "game":
                if event.key == pygame.K_RETURN:
                    game.gerarpuzzle(seed.input)
                    game.limpar_ponto_estrela()
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exibindo == "menu":
                if bjogar.lidar_press(event):
                    exibindo = "game"

                if bcomojogar.lidar_press(event):
                    exibindo = "howtoplay"

            if exibindo == "game":
                if bsairgame.lidar_press(event):
                    exibindo = "menu"
                    jogoativo = False
                    seed = InputBox((165, 35), (312, 25), fonteprincipal, BRANCO, PRETO, 8, "Seed:")
                    gridcells = [[0 for _ in range(8)] for _ in range(8)]
            
            if exibindo == "howtoplay":
                if bsairhowtoplay.lidar_press(event):
                    exibindo = "menu"

        seed.lidar_input(event)
        if jogoativo:
            game.controles(event)

    pygame.display.update()




        



# %%