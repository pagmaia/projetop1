import os
import pygame
from classes import Texto
from classes import Botao
from classes import InputBox
from classes import Puzzle
from classes import Timer


ALTURA = 800
LARGURA = 600
NCELULAS = LIMITELETRAS = 8
TAMANHOCELULA = 49
TAMANHOGRID = 401
FPS = 60

pygame.init()
tela = pygame.display.set_mode((ALTURA, LARGURA))
clock = pygame.time.Clock()
pygame.display.set_caption("STAR PUZZLE")

botaojogar = pygame.image.load(os.path.join("Imagens", "Botoes", "jogar.png")).convert_alpha()
botaocomojogar = pygame.image.load(os.path.join("Imagens", "Botoes", "comojogar.png")).convert_alpha()
botaosair = pygame.image.load(os.path.join("Imagens", "Botoes", "sair.png")).convert_alpha()
botaovoltar = pygame.image.load(os.path.join("Imagens", "Botoes", "voltar.png")).convert_alpha()
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

CORESPUZZLE = {
    1: VERMELHO,
    2: VERDE,
    3: LARANJA,
    4: AMARELO,
    5: AZUL,
    6: ROXO,
    7: ROSA,
    8: TURQUESA,
}


gridcells = [[0 for _ in range(NCELULAS)] for _ in range(NCELULAS)]
listavazia = [""]
seedinputbox = InputBox((165, 35), (312, 25), fonteprincipal30, BRANCO, PRETO, LIMITELETRAS, "")
bjogar = Botao((300, 250), botaojogar)
bcomojogar = Botao((300, 350), botaocomojogar)
bsair = Botao((598, 529), botaosair)
bvoltar = Botao((20, 545), botaovoltar)
game = Puzzle(
    grid,
    (197, 80),
    CORESPUZZLE,
    estrela,
    ponto,
    TAMANHOGRID,
    TAMANHOCELULA,
    gridcells,
    listavazia,
)
regrastitulo = Texto(
    (335, 29),
    "Regras:", 
    fonteprincipal30,
    PRETO,
)
regras = Texto(
    (25, 80),
    "Em cada tabuleiro gerado existe apenas uma solução\n" \
    "com uma estrela por linha/coluna/cor, sem que haja duas\n" \
    "estrelas tocando uma a outra, mesmo diagonalmente.",
    fonteprincipal25,
    PRETO,
)
controlestitulo = Texto((314, 195), "Controles:", fonteprincipal30, PRETO)
controles = Texto(
    (25, 242),
    "Para gerar um tabuleiro, clique na caixa de input, digite a\n" \
    "seed desejada e depois aperte ENTER para gerar o tabuleiro.\n" \
    "Para marcar uma célula sem estrela, clique uma vez na célula.\n" \
    "Para marcar uma célula com estrela, clique outra vez na célula.\n" \
    "Para limpar todas as marcações, aperte ENTER sem digitar\nnenhuma seed.\n" \
    "ATENÇÃO: Seeds válidas têm de 2 a 8 caracteres e não \n" \
    "tem espaços.",
    fonteprincipal25,
    PRETO,
)
seedtitulo = Texto(
    (223, 21),
    "Seed:", 
    fonteprincipal30,
    PRETO,
)
vitoriatexto = Texto(
    (180, 73),
      "Parabéns!!\n" \
      "Você resolveu o star puzzle!!", 
      fonteprincipal30,
      PRETO,
)
timer = Timer((301, 498), fonteprincipal30, PRETO, pygame.K_RETURN, "Tempo:")

def criar_menu():
    tela.blit(titulo, (225, 100))
    bjogar.criar_botao(tela)
    bcomojogar.criar_botao(tela)

def criar_botoes_textos_game():
    seedtitulo.criar_texto(tela)
    seedinputbox.criar_inputbox(tela)
    game.desenhar_frame(tela)
    bsair.criar_botao(tela)
    bvoltar.criar_botao(tela)

def criar_jogar_game():
    timer.criar_timer(tela)
    game.desenhar_puzzle(tela)
    game.desenhar_ponto_estrela(tela)
    game.ativar_hold()

def criar_botoes_textos_vitoria():
    seedpuzzle = Texto(
                (180, 237),
                f"Seed: {seedinputbox.input}",
                fonteprincipal30,
                PRETO,
            )
    timerfinal = Texto(
                (180, 287),
                f"Tempo: {timer.tempopassado // 60:02d}:{timer.tempopassado % 60:02d}",
                fonteprincipal30,
                PRETO,
            )
    bsair.criar_botao(tela)
    vitoriatexto.criar_texto(tela)
    seedpuzzle.criar_texto(tela)
    timerfinal.criar_texto(tela)

def criar_botoes_textos_howtoplay():
    bsair.criar_botao(tela)
    regrastitulo.criar_texto(tela)
    regras.criar_texto(tela)
    controlestitulo.criar_texto(tela)
    controles.criar_texto(tela)

def eventos_game_teclado(event):
    if event.key == pygame.K_RETURN and game.seedsgeradas[-1] != seedinputbox.input:
        game.gerar_puzzle(seedinputbox.input)
        game.limpar_ponto_estrela()
        timer.start(event)

    elif event.key == pygame.K_RETURN and game.seedsgeradas[-1] == seedinputbox.input:
        game.gerar_puzzle(seedinputbox.input)
        game.limpar_ponto_estrela()

def botoes_menu(event, exibindo):
    if bjogar.lidar_press(event):
        exibindo = "game"

    if bcomojogar.lidar_press(event):
        exibindo = "howtoplay"

    return exibindo

def botoes_howtoplay(event, exibindo):
    if bsair.lidar_press(event):
        exibindo = "menu"

    return exibindo

def botoes_play_game(event, exibindo, jogoativo):
    if jogoativo:
        game.ativar_click(event)

    if bsair.lidar_press(event):
        exibindo = "menu"
        jogoativo = False
        seedinputbox.reset()
        timer.reset()

    if bvoltar.lidar_press(event):
        game.voltar()

    return exibindo, jogoativo

def botoes_vitoria(event, exibindo):
    if bsair.lidar_press(event):
        exibindo = "menu"
        seedinputbox.reset()
        timer.reset()

    return exibindo

def main():
    rodando = True
    jogoativo = False
    exibindo = "menu"

    while rodando:

        tela.fill(BACKGROUND)

        if exibindo == "menu":
            criar_menu()

        elif exibindo == "game":
            criar_botoes_textos_game()

            if len(seedinputbox.input) > 1:
                criar_jogar_game()
                jogoativo = True

                if game.vitoria():
                    exibindo = "vitoria"

        elif exibindo == "vitoria":
            criar_botoes_textos_vitoria()

        elif exibindo == "howtoplay":
            criar_botoes_textos_howtoplay()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                rodando = False

            if exibindo == "game":
                seedinputbox.lidar_input(event)

            if event.type == pygame.KEYDOWN:
                if exibindo == "game":
                    eventos_game_teclado(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exibindo == "menu":
                    exibindo = botoes_menu(event, exibindo)

                if exibindo == "game":
                    exibindo, jogoativo = botoes_play_game(event, exibindo, jogoativo)

                if exibindo == "vitoria":
                    exibindo = botoes_vitoria(event, exibindo)

                if exibindo == "howtoplay":
                    exibindo = botoes_howtoplay(event, exibindo)
                    
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
