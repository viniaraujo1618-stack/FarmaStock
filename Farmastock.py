from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmastock.db'

db = SQLAlchemy(app)
class Product (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    


@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json

    if 'name' in data and 'price' in data:
        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", "")
        )

        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Product added successfully"}), 200

    return jsonify({"message": "Invalid product data"}), 400
@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)

    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200

    return jsonify({"message": "Product not found"}), 404


@app.route('/')
def home():
    return render_template('index.html')
   

@app.route('/produtos')
def listar_produtos():
    produtos = Product.query.all()

    return render_template(
        'produtos.html',
        produtos=produtos
    )
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():

    if request.method == 'POST':

        nome = request.form['nome']
        preco = float(request.form['preco'])
        descricao = request.form['descricao']

        novo_produto = Product(
            name=nome,
            price=preco,
            description=descricao
        )

        db.session.add(novo_produto)
        db.session.commit()

        return redirect('/produtos')

    return render_template('adicionar.html')
@app.route('/deletar/<int:id>')
def deletar(id):
    produto = Product.query.get_or_404(id)

    db.session.delete(produto)
    db.session.commit()

    return redirect('/produtos')
    


    

if __name__ == '__main__':
    app.run(debug=True)
    
