# %%
from starpuzzle import generatepuzzle
from starpuzzle import printgame
from starpuzzle import somadoselementos

for i in range(1):
    jogo, coords_estrelas, regioes_posicoes= generatepuzzle(8, 2)
    print(coords_estrelas)
    print(somadoselementos(regioes_posicoes))
    printgame(jogo)

# %%