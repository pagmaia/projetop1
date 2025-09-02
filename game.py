# %%
from starpuzzle import generatepuzzle
from starpuzzle import printgame
from starpuzzle import somadoselementos

for i in range(50):
    jogo, coords_estrelas, regioes_posicoes= generatepuzzle(8)
    print(coords_estrelas)
    print(somadoselementos(regioes_posicoes))
    printgame(jogo)

# %%