from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

        
app = Flask(__name__)

@app.route('/inicio')
def index():
    jogo1 = Jogo('Minecraft', 'SandBox', 'XBOX-360')
    jogo2 = Jogo('Hotweels World Race', 'Aventura', 'Playstation 2')
    jogo3 = Jogo('Roblox', 'Criatividade', 'Celular e Computador')
    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo = 'Jogos', jogos=lista_jogos)
app.run(host='0.0.0.0', port=8080)