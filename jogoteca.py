from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Minecraft', 'SandBox', 'XBOX-360')
jogo2 = Jogo('Hotweels World Race', 'Aventura', 'Playstation 2')
jogo3 = Jogo('Roblox', 'Criatividade', 'Celular e Computador')
lista_jogos = [jogo1, jogo2, jogo3]     

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo_jogo():
    return render_template('novojogo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return render_template('lista.html', titulo='Novo Jogo', jogos=lista_jogos)

app.run(host='0.0.0.0', port=8080, debug=True)