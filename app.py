#Importação
from flask import Flask

app = Flask(__name__)

# Definição de rota raiz (página inicial e função que será executada ao requisitar)
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
