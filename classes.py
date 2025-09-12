import pygame
from starpuzzle import generatepuzzle

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

class Botao():

    def __init__(self, posicao, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (posicao[0], posicao[1])

    def criar(self, tela):

        tela.blit(self.imagem, (self.rect.x, self.rect.y))

    def lidar_press(self, evento):
        self.clicked = False
        action = False
        if self.rect.collidepoint(evento.pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action

class InputBox():

    def __init__(self, tamanho, posicao, fonte, fundo, cortexto, limite, textoexibido=""):
        self.fonte = fonte
        self.tamanhox = tamanho[0]
        self.tamanhoy = tamanho[1]
        self.posicaox = posicao[0]
        self.posicaoy = posicao[1]
        self.textoexibido = textoexibido
        self.fundo = fundo
        self.cortexto = cortexto
        self.fundo = fundo
        self.limite = limite
        self.rect = pygame.Rect(self.posicaox, self.posicaoy, self.tamanhox, self.tamanhoy)
        self.rect.topleft = ((self.posicaox, self.posicaoy))
        self.rectborda = self.rect.inflate(2, 2)
        self.textosuperficie = fonte.render(self.textoexibido, True, cortexto)
        self.textorect = self.textosuperficie.get_rect()
        self.textorect.topleft = (self.posicaox + 6, self.posicaoy - 4)
        self.clicked = False
        self.input = ""

    def criar(self, tela):
        pygame.draw.rect(tela, self.fundo, self.rect)
        pygame.draw.rect(tela, PRETO, self.rectborda, 2)
        tela.blit(self.textosuperficie, self.textorect)

    def lidar_input(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.clicked = True
                self.textoexibido = ""

            else:
                self.clicked = False

        if evento.type == pygame.KEYDOWN:
            if self.clicked:
                if evento.key == pygame.K_RETURN:
                    self.input = self.textoexibido
                    self.textoexibido = ""
                    
                if evento.key == pygame.K_BACKSPACE:
                    self.textoexibido = self.textoexibido[:-1]

                else:
                    if len(self.textoexibido) < self.limite:
                        self.textoexibido += evento.unicode

                self.textosuperficie = self.fonte.render(self.textoexibido, True, self.cortexto)

class Puzzle():

    def __init__(self, frame, pos, coresregiao, estrela, ponto, tamanho, tamanhocelulas, gridcells):
        self.frame = frame
        self.estrela = estrela
        self.ponto = ponto
        self.posx = pos[0]
        self.posy = pos[1]
        self.cores = coresregiao
        self.tamanho = tamanho
        self.tamanhocelulas = tamanhocelulas
        self.gridcells = gridcells

    def gerarpuzzle(self, semente):
        self.game = generatepuzzle(8, semente)[0]
        self.coordsestrela = generatepuzzle(8, semente)[1]

        return self.game, self.coordsestrela

    def desenharframe(self, tela):
        pygame.draw.rect(tela, BRANCO, pygame.Rect(self.posx, self.posy, self.tamanho, self.tamanho))
 
    def desenharpuzzle(self, tela):
        pygame.draw.rect(tela, PRETO, pygame.Rect(self.posx, self.posy, self.tamanho, self.tamanho))
        for i, x in enumerate(range(self.posx + 1, self.posx + self.tamanho, self.tamanhocelulas + 1)):  
            for j, y in enumerate(range(self.posy + 1, self.posy + self.tamanho, self.tamanhocelulas + 1)):
                self.rect = pygame.Rect(x, y, self.tamanhocelulas, self.tamanhocelulas)
                self.celula = self.game[i][j]
                pygame.draw.rect(tela, self.cores[self.celula[1]], self.rect)
    
    def controles(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and self.posx < evento.pos[0] < self.tamanho + self.posx and self.posy < evento.pos[1] < self.tamanho + self.posy:
            x = (evento.pos[0] - self.posx) // 49
            y = (evento.pos[1] - self.posy) // 49
            
            if x > 7:
                x -= 1
            if y > 7:
                y -= 1
        
            self.gridcells[x][y] += 1

    def desenhar_ponto_estrela(self, tela):
        for i in range(len(self.gridcells)):
            for j in range(len(self.gridcells)):
                if self.gridcells[i][j] > 2:
                    self.gridcells[i][j] = 0
            
                if self.gridcells[i][j] == 1:
                    tela.blit(self.ponto, ((self.posx + (i * (self.tamanhocelulas + 1)) + 18), (self.posy + (j * (self.tamanhocelulas + 1)) + 18)))
                
                elif self.gridcells[i][j] == 2:
                    tela.blit(self.estrela, ((self.posx + (i * (self.tamanhocelulas + 1)) + 11), (self.posy + (j * (self.tamanhocelulas + 1)) + 11)))

    def limpar_ponto_estrela(self):
        self.gridcells = [[0 for _ in range(8)] for _ in range(8)]

    def vitoria(self):
        ganhou = True
        for pos in self.coordsestrela:
            if self.gridcells[pos[0]][pos[1]] != 2:
                ganhou = False

        return ganhou

                    