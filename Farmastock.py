from flask import Flask, request, jsonify
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
  


