import pygame
from gerador import generatepuzzle

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

class Texto():
    def __init__(self, pos, texto, fonte, cor):
        self.posx = pos[0]
        self.posy = pos[1]
        self.texto = texto
        self.fonte = fonte
        self.entrelinhas = 5
        self.cor = cor

    def criar_texto(self, tela):
        for i, linha in enumerate(self.texto.split("\n")):
            self.superficie = self.fonte.render(linha, True, self.cor)
            tela.blit(self.superficie, (self.posx, self.posy + i * (self.fonte.size(linha)[1] + self.entrelinhas)))
            
class Botao():

    def __init__(self, posicao, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (posicao[0], posicao[1])

    def criar_botao(self, tela):

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
        self.fonte = fonte
        self.fundo = fundo
        self.cortexto = cortexto
        self.fundo = fundo
        self.limite = limite
        self.rect = pygame.Rect(self.posicaox, self.posicaoy, self.tamanhox, self.tamanhoy)
        self.rect.topleft = ((self.posicaox, self.posicaoy))
        self.rectborda = self.rect.inflate(2, 2)
        self.textosuperficie = self.fonte.render(self.textoexibido, True, cortexto)
        self.textorect = self.textosuperficie.get_rect()
        self.textorect.topleft = (self.posicaox + 6, self.posicaoy - 4)
        self.clicked = False
        self.input = ""

    def criar_inputbox(self, tela):
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
                    if len(self.textoexibido) < self.limite and evento.unicode != " ":
                        self.textoexibido += evento.unicode

                self.textosuperficie = self.fonte.render(self.textoexibido, True, self.cortexto)

    def reset(self):
        self.input = ""

class Puzzle():

    def __init__(self, frame, pos, coresregiao, estrela, ponto, tamanho, tamanhocelulas, gridcells, seedsgeradas):
        self.frame = frame
        self.estrela = estrela
        self.ponto = ponto
        self.posx = pos[0]
        self.posy = pos[1]
        self.cores = coresregiao
        self.tamanho = tamanho
        self.tamanhocelulas = tamanhocelulas
        self.gridcells = gridcells
        self.seedsgeradas = seedsgeradas
        self.log = []
        self.segurando = False

    def gerar_puzzle(self, semente):
        self.game = generatepuzzle(8, semente)[0]
        self.coordsestrela = generatepuzzle(8, semente)[1]
        if len(semente) > 1:
            self.seedsgeradas.append(semente)

        return self.game, self.coordsestrela

    def desenhar_frame(self, tela):
        pygame.draw.rect(tela, BRANCO, pygame.Rect(self.posx, self.posy, self.tamanho, self.tamanho))
 
    def desenhar_puzzle(self, tela):
        pygame.draw.rect(tela, PRETO, pygame.Rect(self.posx, self.posy, self.tamanho, self.tamanho))
        for i, x in enumerate(range(self.posx + 1, self.posx + self.tamanho, self.tamanhocelulas + 1)):  
            for j, y in enumerate(range(self.posy + 1, self.posy + self.tamanho, self.tamanhocelulas + 1)):
                self.rect = pygame.Rect(x, y, self.tamanhocelulas, self.tamanhocelulas)
                self.celula = self.game[i][j]
                pygame.draw.rect(tela, self.cores[self.celula[1]], self.rect)
    
    def calcular_pos(self):

        posmousex, posmousey = pygame.mouse.get_pos()

        if self.posx < posmousex < self.tamanho + self.posx and self.posy < posmousey < self.tamanho + self.posy:
            x = (posmousex - self.posx) // 49
            y = (posmousey - self.posy) // 49
            
            if x > 7:
                x = 7
            if y > 7:
                y = 7

            return (x, y)

    def ativar_click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = self.calcular_pos()

            if pos != None:
                x = pos[0]
                y = pos[1]        
                self.gridcells[x][y] += 1
                self.log.append((x, y))

    def ativar_hold(self):
        if pygame.mouse.get_pressed()[0]:
            self.segurando = True
        else:
            self.segurando = False

        if self.segurando:
            pos = self.calcular_pos()

            if pos != None:
                x = pos[0]
                y = pos[1]

                if not self.gridcells[x][y]:        
                    self.gridcells[x][y] += 1
                    self.log.append((x, y))
                
    def desenhar_ponto_estrela(self, tela):
        for pos in self.log:
                i = pos[0]
                j = pos[1]

                if self.gridcells[i][j] > 3:
                    self.gridcells[i][j] = 0
            
                if self.gridcells[i][j] == 1:
                    tela.blit(self.ponto, ((self.posx + (i * (self.tamanhocelulas + 1)) + 18), (self.posy + (j * (self.tamanhocelulas + 1)) + 18)))
                
                elif self.gridcells[i][j] == 2:
                    tela.blit(self.estrela, ((self.posx + (i * (self.tamanhocelulas + 1)) + 11), (self.posy + (j * (self.tamanhocelulas + 1)) + 11)))

    def limpar_ponto_estrela(self):
        self.gridcells = [[0 for _ in range(8)] for _ in range(8)]

    def celulas_com_estrela(self):
        contador = 0
        for i in range(len(self.gridcells)):
            for j in range(len(self.gridcells)):
                if self.gridcells[i][j] == 2:
                    contador += 1
        return contador
    
    def celulas_com_marcacao(self):
        for i in range(len(self.gridcells)):
            for j in range(len(self.gridcells)):
                if self.gridcells[i][j]:
                    return True
        
        return False

    def voltar(self):
        if not self.log:
            return False
         
        x, y = self.log[-1]
        self.gridcells[x][y] -= 1
        self.log.pop(-1)

    def vitoria(self):
        ganhou = True
        for pos in self.coordsestrela:
            if self.gridcells[pos[0]][pos[1]] != 2:
                ganhou = False

        if self.celulas_com_estrela() != 8:
            ganhou = False

        return ganhou
    
    
class Timer():
    def __init__(self, pos, fonte, cor, evento, textopadrao):
        self.posx = pos[0]
        self.posy = pos[1]
        self.fonte = fonte
        self.cor = cor
        self.evento = evento
        self.textopadrao = textopadrao
        self.tempopassado = 0
        self.inicio = 0
        self.iniciou = False

    def criar_timer(self, tela):
        if self.iniciou:
            self.tempopassado = pygame.time.get_ticks() // 1000 - self.inicio

        self.minutos = self.tempopassado // 60
        self.segundos = self.tempopassado % 60
        self.texto = f"{self.textopadrao} {self.minutos:02d}:{self.segundos:02d}"
        self.textosuperficie = self.fonte.render(self.texto, True, self.cor)
        tela.blit(self.textosuperficie, (self.posx, self.posy))

    def start(self, evento):
        if evento.key == self.evento:
            self.inicio = pygame.time.get_ticks() // 1000
            self.iniciou = True

    def reset(self):
        self.iniciou = False
        self.tempopassado = 0

        



    


            

                    
