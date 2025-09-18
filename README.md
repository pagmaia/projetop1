
# Star Battle 🌟
<img width="795" height="590" alt="Captura de tela 2025-09-15 202657" src="https://github.com/user-attachments/assets/8ab8a3c3-de2f-40ff-af53-f10cd619c1e1" /> 


Jogo semelhante ao [Star Battle](https://starbattle.puzzlebaron.com/play.php) ou [Queens](https://www.linkedin.com/games/queens).  
Funciona gerando um puzzle 8x8, em que há apenas uma solução com uma estrela por linha/coluna/cor, sem que duas estrelas se toquem diagonalmente.  
A interface gráfica foi criada utilizando Pygame.  
# Requisitos 
-- Python 3.12.7 --  
-- Pip (Versão mais recente) --  
-- Pygame 2.6.1 -- 

# Vídeo
https://www.youtube.com/watch?v=-pV63buh3p4  

# Instruções para instalação:
1. No terminal Linux ou Windows, clone o repositório usando o seguinte comando (Necessário que o usuário tenha [Git](https://git-scm.com/downloads) instalado):
   ```
   git clone https://github.com/pagmaia/projetop1.git
   ```
2. Após clonar, entre no diretório e crie um enviroment em python usando [virtual env](https://virtualenv.pypa.io/en/latest/installation.html).
   ```
   python3 -m venv .venv
   ```
3. Ative o enviroment:

   Linux:
   ```
   source .venv/bin/activate
   ```
   Windows (cmd):
   ```
   .\venv\Scripts\activate
   ```
5. Depois de ser ativado, instale o Pygame:  
   Cheque se o enviroment possui Pip instalado com o seguinte comando:  
   ```
   pip --version
   ```
   Se o Pip estiver instalado, instale o Pygame:    
   ```
   pip install pygame==2.6.1
   ```
   Se o enviroment não tiver Pip instalado, instale o Pip e o Pygame utilizando esses comandos:
   ```
   python3 -m ensurepip
   ```
   ```
   python3 -m pip install pygame==2.6.1
   ```
7. Depois de instalado, para jogar, utilize o seguinte comando:
   ```
   python3 game.py
   ```
8. Divirta-se!

Feito por Pedro Arthur Gomes Maia
