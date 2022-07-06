from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
app = Flask(__name__)

jogo1 = Jogo('Mario Kart', 'Corrida', 'Nintendo')
jogo2 = Jogo('Counter Strike', 'FPS', 'Computador')
jogo3 = Jogo('League of Legends', 'MOBA', 'Computador')
lista = [jogo1, jogo2, jogo3]

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

app.run()