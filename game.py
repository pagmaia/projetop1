# %%
from classes import Texto
from classes import Botao
from classes import InputBox
from classes import Puzzle
from classes import Timer
import pygame
import os

pygame.init()
altura = 800
largura = 600
tela = pygame.display.set_mode((altura, largura))
clock = pygame.time.Clock()
pygame.display.set_caption("STAR PUZZLE")

botaojogar = pygame.image.load(os.path.join("Imagens", "Botoes", "jogar.png")).convert_alpha()
botaocomojogar = pygame.image.load(os.path.join("Imagens", "Botoes", "comojogar.png")).convert_alpha()
botaosair = pygame.image.load(os.path.join("Imagens", "Botoes", "sair.png")).convert_alpha()
titulo = pygame.image.load(os.path.join("Imagens", "Titulo.png")).convert_alpha()
boxvazia = pygame.image.load(os.path.join("Imagens", "boxvazia.png")).convert_alpha()
grid = pygame.image.load(os.path.join("Imagens", "Puzzle", "grid.png")).convert_alpha()
estrela = pygame.image.load(os.path.join("Imagens", "Puzzle", "estrela.png")).convert_alpha()
ponto = pygame.image.load(os.path.join("Imagens", "Puzzle", "ponto.png")).convert_alpha()

fonteprincipal30 = pygame.font.Font(os.path.join("Fontes", "Kodchasan", "Kodchasan-Regular.ttf"), 30)
fonteprincipal25 = pygame.font.Font(os.path.join("Fontes", "Kodchasan", "Kodchasan-Regular.ttf"), 25)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
BACKGROUND = (0, 97, 167)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
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
seed = InputBox((165, 35), (312, 25), fonteprincipal30, BRANCO, PRETO, 8, "")
game = Puzzle(grid, (197, 80), CORESPUZZLE, estrela, ponto, 401, 49, gridcells)
bjogar = Botao((300, 250), botaojogar)
bcomojogar = Botao((300, 350), botaocomojogar)
bsairgame = Botao((598, 529), botaosair)
bsairhowtoplay = Botao((297, 500), botaosair)
bsairvitoria = Botao((305, 425), botaosair)
regrastitulo = Texto((335, 29), "Regras:", fonteprincipal30, PRETO)
regras = Texto((25, 80), "Em cada tabuleiro gerado existe apenas uma solução\ncom uma estrela por linha/coluna/cor, sem que haja duas\nestrelas tocando uma a outra, mesmo diagonalmente.", fonteprincipal25, PRETO)
controlestitulo = Texto((314, 195), "Controles:", fonteprincipal30, PRETO)
controles = Texto((25, 242), "Para gerar um tabuleiro, clique na caixa de input, digite a\nseed desejada e depois aperte ENTER para gerar o tabuleiro.\nPara marcar uma célula sem estrela, clique uma vez na célula.\nPara marcar uma célula com estrela, clique outra vez na célula.\nPara limpar todas as marcações, aperte ENTER sem digitar\nnenhuma seed.\nATENÇÃO: Seeds válidas têm de 2 a 8 caracteres.", fonteprincipal25, PRETO)
seedtitulo = Texto((223, 21), "Seed:", fonteprincipal30, PRETO)
vitoriatexto = Texto((180, 73), "Parabéns!!\nVocê resolveu o star puzzle!!", fonteprincipal30, PRETO)
timer = Timer((301,498), fonteprincipal30, PRETO, pygame.K_RETURN, "Tempo:")

while rodando:
    
    tela.fill(BACKGROUND)

    if exibindo == "menu":
        tela.blit(titulo, (225, 100))
        bjogar.criar(tela)
        bcomojogar.criar(tela)

    elif exibindo == "game":
        seedtitulo.criartexto(tela)
        seed.criar(tela)
        game.desenharframe(tela)
        timer.criartimer(tela)
        
        if len(seed.input) > 1:
            seedtitulo3 = Texto((356, 478), f"{seed.input}", fonteprincipal30, PRETO)
            game.desenharpuzzle(tela)
            game.desenhar_ponto_estrela(tela)
            jogoativo = True

            if game.vitoria():
                exibindo = "vitoria"
            
        bsairgame.criar(tela)

    elif exibindo == "vitoria":
        seedtitulo2 = Texto((180, 237), f"Seed: {seed.input}", fonteprincipal30, PRETO)
        timerfinal = Texto((180, 287), f"Tempo:{timer.tempopassado // 60:2d}:{timer.tempopassado % 60}", fonteprincipal30, PRETO)
        bsairvitoria.criar(tela)
        vitoriatexto.criartexto(tela)
        seedtitulo2.criartexto(tela)
        timerfinal.criartexto(tela)

    elif exibindo == "howtoplay":
        bsairhowtoplay.criar(tela)
        regrastitulo.criartexto(tela)
        regras.criartexto(tela)
        controlestitulo.criartexto(tela)
        controles.criartexto(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if exibindo == "game":
            seed.lidar_input(event)
        if jogoativo:
            game.controles(event)

        if event.type == pygame.KEYDOWN:
            if exibindo == "game":
                if event.key == pygame.K_RETURN:
                    game.gerarpuzzle(seed.input)
                    game.limpar_ponto_estrela()
                    timer.start(event)
                    
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
                    seed.reset()
                    timer.reset()

            if exibindo == "vitoria":
                if bsairvitoria.lidar_press(event):
                    exibindo = "menu"
                    seed.reset()
                    timer.reset()
                    
            if exibindo == "howtoplay":
                if bsairhowtoplay.lidar_press(event):
                    exibindo = "menu"

    clock.tick(60)
    pygame.display.update()

pygame.quit()




        



# %%