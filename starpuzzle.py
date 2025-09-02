# %%
# Código para gerar um puzzle de tamanho NxN, de 1 estrela
import random

def pos_segura_estrela(posx, posy, tabuleiro):

    if posx < 0 or posx > len(tabuleiro) - 1 or posy < 0 or posy > len(tabuleiro) - 1:
        return False
    
    for j in range(posx, len(tabuleiro)):
        if tabuleiro[posx][j][0]:
            return False
        
    for j in range(posx, -1, -1):
        if tabuleiro[posx][j][0]:
            return False
        
    for i in range(posy, len(tabuleiro)):
        if tabuleiro[i][posy][0]:
            return False
        
    for i in range(posy, -1, -1):
        if tabuleiro[i][posy][0]:
            return False
        
    cimadireita = (posx - 1, posy + 1)
    cimaesquerda = (posx - 1, posy - 1)
    baixodireita = (posx + 1, posy + 1)
    baixoesquerda = (posx + 1, posy - 1)
    diagonais = [cimadireita, cimaesquerda, baixodireita, baixoesquerda]

    for pos in diagonais:
        
        if 0 <= pos[0] < len(tabuleiro) and 0 <= pos[1] < len(tabuleiro):

            if tabuleiro[pos[0]][pos[1]][0]:
                return False
        
    return True

def escolhas_possiveis(tabuleiro):
    possiveis = []

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if pos_segura_estrela(i, j, tabuleiro):
                possiveis.append((i, j))

    if not possiveis:
        return False
    
    posicao = random.choice(possiveis)

    return (posicao[0], posicao[1])

def gerar_estrelas(tamanho):
    regiao = 1
    regioes_posicoes = {ID: [] for ID in range(1, tamanho + 1)}
    tabuleiro = [[[False, 0] for i in range(tamanho)] for i in range(tamanho)]
    coords_estrela = []
    
    while len(coords_estrela) < tamanho:

        status = escolhas_possiveis(tabuleiro)
        
        if not status:
            for i in range(len(coords_estrela) -1, -1, -1):
                tabuleiro[coords_estrela[i][0]][coords_estrela[i][1]][0] = False
                tabuleiro[coords_estrela[i][0]][coords_estrela[i][1]][1] = 0
                coords_estrela.pop(i)
                regiao -= 1
                regioes_posicoes[regiao] = []
                
        else:
            posx, posy = status[0], status[1]
            tabuleiro[posx][posy][0] = True
            tabuleiro[posx][posy][1] = regiao
            coords_estrela.append((posx, posy))
            regioes_posicoes[regiao].append((posx, posy))
            regiao += 1
        
    return tabuleiro, coords_estrela, regioes_posicoes

def celulas(target, tamanho):
    min, max  = 0, tamanho * 2
    elementos = tamanho
    
    numeros = []
    intervalo = range(min, max + 1)

    while True:
        numeros.append(random.choice(intervalo))
        if len(numeros) == elementos:
            if sum(numeros) == target:
                return numeros
            numeros = numeros[1:]

def criar_direcoes_validas(posx, posy, melhorado, tabuleiro):
    cima = (posx - 1, posy)
    baixo = (posx + 1, posy)
    direita = (posx, posy + 1)
    esquerda = (posx, posy - 1)

    direcoes = [cima, baixo, direita, esquerda]
    direcoesvalidas = []

    for direcao in direcoes:
                    
        if direcao[0] < 0 or direcao[0] > len(tabuleiro) - 1 or direcao[1] < 0 or direcao[1] > len(tabuleiro) - 1:
            continue
        
        if melhorado:
            if tabuleiro[direcao[0]][direcao[1]][0]:
                continue

            elif tabuleiro[direcao[0]][direcao[1]][1]:
                continue
                    
        direcoesvalidas.append((direcao[0], direcao[1]))

    return direcoesvalidas

def pos_segura_regiao(regiao, regioes_posicoes, tabuleiro):
    melhorado = True

    posx = regioes_posicoes[regiao][-1][0]
    posy = regioes_posicoes[regiao][-1][1]
                    
    direcoesvalidas = criar_direcoes_validas(posx, posy, melhorado, tabuleiro)
                    
    if not direcoesvalidas:
        return False
        
    else:
        direcaoescolhida = random.choice(direcoesvalidas)
        return direcaoescolhida

def tentar_criar_regioes(tabuleiro, regioes_posicoes):

    regiao = 1
    validos = celulas(len(tabuleiro) ** 2 - len(tabuleiro), len(tabuleiro))
        
    for passos in validos:
        i = 0

        while i < passos:  
            direcaoescolhida = pos_segura_regiao(regiao, regioes_posicoes, tabuleiro)

            if not direcaoescolhida:
                break
            
            else:
                tabuleiro[direcaoescolhida[0]][direcaoescolhida[1]][1] = regiao
                posx = direcaoescolhida[0]
                posy = direcaoescolhida[1]
                regioes_posicoes[regiao].append((posx, posy))
            
            i += 1  
        
        regiao += 1
    
    return tabuleiro, regioes_posicoes

def calcula_vazias(tabuleiro):
    vazias = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if not tabuleiro[i][j][1]:
                vazias.append((i, j))

    return vazias

def preenche_resto(tabuleiro, regioes_posicoes):
    vazias = []
    semmelhorado = False

    vazias = calcula_vazias(tabuleiro)

    while vazias:

        for pos in vazias:
            regioes = []
            direcoes = criar_direcoes_validas(pos[0], pos[1], semmelhorado, tabuleiro)
            
            for direcao in direcoes:
                if tabuleiro[direcao[0]][direcao[1]][1]:
                    regioes.append(tabuleiro[direcao[0]][direcao[1]][1])

            if not regioes:
                continue

            else:
                regiaoaleatoria = random.choice(regioes)
                tabuleiro[pos[0]][pos[1]][1] = regiaoaleatoria
                regioes_posicoes[regiaoaleatoria].append((pos[0], pos[1]))
        
        vazias = calcula_vazias(tabuleiro)
    
    return tabuleiro
        
def printgame(tabuleiro):

    for direcao in tabuleiro:
        print(direcao)

    print("-")

def somadoselementos(dicionario):
    return sum(len(valor) for valor in dicionario.values())

def generatepuzzle(tamanho):
   
    tabuleiro, coords_estrelas, regioes_posicoes = gerar_estrelas(tamanho)
    tabuleiro, regioes_posicoes = tentar_criar_regioes(tabuleiro, regioes_posicoes)
    tabuleiro = preenche_resto(tabuleiro, regioes_posicoes)
   
    
    return tabuleiro, coords_estrelas, regioes_posicoes

    

# %%

