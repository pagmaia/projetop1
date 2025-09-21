from classes import Texto
from classes import Botao
from classes import InputBox
from classes import Puzzle
from classes import Timer
import pygame
import os

#inicio
pygame.init()
altura = 800
largura = 600
tela = pygame.display.set_mode((altura, largura))
clock = pygame.time.Clock()
pygame.display.set_caption("STAR PUZZLE")

#Imagens
botaojogar = pygame.image.load(os.path.join("Imagens", "Botoes", "jogar.png")).convert_alpha()
botaocomojogar = pygame.image.load(os.path.join("Imagens", "Botoes", "comojogar.png")).convert_alpha()
botaosair = pygame.image.load(os.path.join("Imagens", "Botoes", "sair.png")).convert_alpha()
botaovoltar = pygame.image.load(os.path.join("Imagens", "Botoes", "voltar.png")).convert_alpha()
titulo = pygame.image.load(os.path.join("Imagens", "Titulo.png")).convert_alpha()
boxvazia = pygame.image.load(os.path.join("Imagens", "boxvazia.png")).convert_alpha()
grid = pygame.image.load(os.path.join("Imagens", "Puzzle", "grid.png")).convert_alpha()
estrela = pygame.image.load(os.path.join("Imagens", "Puzzle", "estrela.png")).convert_alpha()
ponto = pygame.image.load(os.path.join("Imagens", "Puzzle", "ponto.png")).convert_alpha()
#Fontes
fonteprincipal30 = pygame.font.Font(os.path.join("Fontes", "Kodchasan", "Kodchasan-Regular.ttf"), 30)
fonteprincipal25 = pygame.font.Font(os.path.join("Fontes", "Kodchasan", "Kodchasan-Regular.ttf"), 25)

#Cores
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
            
#Objetos
gridcells = [[0 for _ in range(8)] for _ in range(8)]
seedinputbox = InputBox((165, 35), (312, 25), fonteprincipal30, BRANCO, PRETO, 8, "")
game = Puzzle(grid, (197, 80), CORESPUZZLE, estrela, ponto, 401, 49, gridcells, [""])
bjogar = Botao((300, 250), botaojogar)
bcomojogar = Botao((300, 350), botaocomojogar)
bsair = Botao((598, 529), botaosair)
bvoltar = Botao((20, 545), botaovoltar)
regrastitulo = Texto((335, 29), "Regras:", fonteprincipal30, PRETO)
regras = Texto((25, 80), "Em cada tabuleiro gerado existe apenas uma solução\ncom uma estrela por linha/coluna/cor, sem que haja duas\nestrelas tocando uma a outra, mesmo diagonalmente.", fonteprincipal25, PRETO)
controlestitulo = Texto((314, 195), "Controles:", fonteprincipal30, PRETO)
controles = Texto((25, 242), "Para gerar um tabuleiro, clique na caixa de input, digite a\nseed desejada e depois aperte ENTER para gerar o tabuleiro.\nPara marcar uma célula sem estrela, clique uma vez na célula.\nPara marcar uma célula com estrela, clique outra vez na célula.\nPara limpar todas as marcações, aperte ENTER sem digitar\nnenhuma seed.\nATENÇÃO: Seeds válidas têm de 2 a 8 caracteres e não \ntem espaços.", fonteprincipal25, PRETO)
seedtitulo = Texto((223, 21), "Seed:", fonteprincipal30, PRETO)
vitoriatexto = Texto((180, 73), "Parabéns!!\nVocê resolveu o star puzzle!!", fonteprincipal30, PRETO)
timer = Timer((301,498), fonteprincipal30, PRETO, pygame.K_RETURN, "Tempo:")

#Game Loop

def main():
    rodando = True
    jogoativo = False
    exibindo = "menu"

    while rodando:
        
        tela.fill(BACKGROUND)

        if exibindo == "menu":
            tela.blit(titulo, (225, 100))
            bjogar.criar_botao(tela)
            bcomojogar.criar_botao(tela)

        elif exibindo == "game":
            seedtitulo.criar_texto(tela)
            seedinputbox.criar_inputbox(tela)
            game.desenhar_frame(tela)
            
            if len(seedinputbox.input) > 1:
                timer.criar_timer(tela)
                game.desenhar_puzzle(tela)
                game.desenhar_ponto_estrela(tela)
                game.ativar_hold()
                jogoativo = True

                if game.vitoria():
                    exibindo = "vitoria"
                
            bsair.criar_botao(tela)
            bvoltar.criar_botao(tela)

        elif exibindo == "vitoria":
            seedpuzzle = Texto((180, 237), f"Seed: {seedinputbox.input}", fonteprincipal30, PRETO)
            timerfinal = Texto((180, 287), f"Tempo: {timer.tempopassado // 60:02d}:{timer.tempopassado % 60:02d}", fonteprincipal30, PRETO)
            bsair.criar_botao(tela)
            vitoriatexto.criar_texto(tela)
            seedpuzzle.criar_texto(tela)
            timerfinal.criar_texto(tela)

        elif exibindo == "howtoplay":
            bsair.criar_botao(tela)
            regrastitulo.criar_texto(tela)
            regras.criar_texto(tela)
            controlestitulo.criar_texto(tela)
            controles.criar_texto(tela)
    #Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            if exibindo == "game":
                seedinputbox.lidar_input(event)
            
            if event.type == pygame.KEYDOWN:
                if exibindo == "game":
                    if event.key == pygame.K_RETURN and game.seedsgeradas[-1] != seedinputbox.input:
                        game.gerar_puzzle(seedinputbox.input)
                        game.limpar_ponto_estrela()
                        timer.start(event)

                    elif event.key == pygame.K_RETURN and game.seedsgeradas[-1] == seedinputbox.input:
                        game.gerar_puzzle(seedinputbox.input)
                        game.limpar_ponto_estrela()
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exibindo == "menu":
                    if bjogar.lidar_press(event):        
                        exibindo = "game"   

                    if bcomojogar.lidar_press(event):
                        exibindo = "howtoplay"

                if exibindo == "game":
                    if jogoativo:
                        game.ativar_click(event)

                    if bsair.lidar_press(event):
                        exibindo = "menu"
                        jogoativo = False
                        seedinputbox.reset()
                        timer.reset()
                    
                    if bvoltar.lidar_press(event):
                        if game.voltar():
                            continue

                if exibindo == "vitoria":
                    if bsair.lidar_press(event):
                        exibindo = "menu"
                        seedinputbox.reset()
                        timer.reset()
                        
                if exibindo == "howtoplay":
                    if bsair.lidar_press(event):
                        exibindo = "menu"

        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
