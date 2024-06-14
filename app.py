from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

class FlowerShop:
    def __init__(self, filename='flowers1.txt'):
        self.filename = filename
        self.flowers = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        flowers = []
        with open(self.filename, 'r') as f:
            for line in f:
                name, price, quantity = line.strip().split(',')
                flowers.append({'name': name, 'price': float(price), 'quantity': int(quantity)})
        return flowers

    def save_data(self):
        with open(self.filename, 'w') as f:
            for flower in self.flowers:
                f.write(f"{flower['name']},{flower['price']},{flower['quantity']}\n")

    def add_flower(self, name, price, quantity):
        for flower in self.flowers:
            if flower['name'] == name:
                return {'message': f"'{name}'已经有啦~"}
        self.flowers.append({'name': name, 'price': price, 'quantity': quantity})
        self.save_data()
        return {'message': '添加成功'}

    def delete_flower(self, name):
        self.flowers = [flower for flower in self.flowers if flower['name'] != name]
        self.save_data()
        return {'message': '删除成功'}

    def update_flower(self, name, price=None, quantity=None):
        for flower in self.flowers:
            if flower['name'] == name:
                if price is not None:
                    flower['price'] = price
                if quantity is not None:
                    flower['quantity'] = quantity
                self.save_data()
                return {'message': '更新成功'}
        return {'message': f"'{name}' not found."}

    def purchase_flower(self, name, quantity):
        for flower in self.flowers:
            if flower['name'] == name:
                if flower['quantity'] < quantity:
                    return {'message': f"您所需的花朵 '{name}' 本店库存不足，已帮您反馈给老板啦."}
                flower['quantity'] -= quantity
                self.save_data()
                return {'message': f"您已成功购买{quantity}支'{name}'."}
        return {'message': f"您需要的花朵 '{name}' 本店暂无哦，已反馈给老板~"}

    def search_flower(self, name):
        for flower in self.flowers:
            if flower['name'] == name:
                return flower
        return {'message': f"Flower '{name}' not found."}

    def display_flowers(self):
        return self.flowers

shop = FlowerShop()

@app.route('/flowers', methods=['GET'])
def get_flowers():
    return jsonify(shop.display_flowers())

@app.route('/flowers', methods=['POST'])
def add_flower():
    data = request.json
    return jsonify(shop.add_flower(data['name'], data['price'], data['quantity']))

@app.route('/flowers/<name>', methods=['DELETE'])
def delete_flower(name):
    return jsonify(shop.delete_flower(name))

@app.route('/flowers/<name>', methods=['PUT'])
def update_flower(name):
    data = request.json
    return jsonify(shop.update_flower(name, data.get('price'), data.get('quantity')))

@app.route('/flowers/purchase', methods=['POST'])
def purchase_flower():
    data = request.json
    return jsonify(shop.purchase_flower(data['name'], data['quantity']))

@app.route('/flowers/search/<name>', methods=['GET'])
def search_flower(name):
    return jsonify(shop.search_flower(name))

if __name__ == '__main__':
    app.run(debug=True)
