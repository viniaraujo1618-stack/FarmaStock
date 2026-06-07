from flask import Flask
from pip._internal.commands import index
app = Flask(__name__)



produtos = [
    {"nome": "Dipirona", "quantidade": 15},
    {"nome": "Paracetamol", "quantidade": 20},
    {"nome": "Ibuprofeno", "quantidade": 8}
]

@app.route('/')
def home():
    return """
    <h1>FarmaStock</h1>
    <p>Sistema de Controle de Estoque</p>
    <a href="/produtos">Ver Estoque</a>
    """

@app.route('/produtos')
def listar_produtos():

    html = "<h1>Estoque</h1>"

    for produto in produtos:
        html += f"""
        <p>
        {produto['nome']} -
        Quantidade: {produto['quantidade']}
        </p>
        """

    return html

if __name__ == '__main__':
    app.run(debug=True)
    README.md


