from flask import Blueprint, Flask, blueprints, jsonify, render_template

product_blueprint = Blueprint('product', '__name__')

products = ['milk', 'ghee', 'butter', 'cheese', 'mayo']

@product_blueprint.route('/list')
def product_list():
    return jsonify({"products": products})
