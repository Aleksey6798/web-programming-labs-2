from flask import Blueprint, render_template

lab7 = Blueprint('lab7',__name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

@lab7.route('/lab7/drink')
def main():
    return render_template('lab7/drink.html')

@lab7.route('/lab7/api', methods = ['POST'])
def api():
    data = request.json

    if data['method'] == 'get-price':
        return get_price(data['params'])
    
    if data['method'] == 'pay':
        return pay(data['params'])
    
    abort(400)

def get_price(params):
    return {"result": calculate_price(params), "error": None}