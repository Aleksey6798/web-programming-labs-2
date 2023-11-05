from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def f():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == "coffee":
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)  

#@lab3.route('/lab3/success')
#def success():
#    return render_template('success.html')

@lab3.route('/lab3/ticket')
def ticket():
    errors = {} 
    return render_template('ticket.html',errors=errors)
    
@lab3.route('/lab3/info_ticket')
def info_ticket():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    
    typ = request.args.get('typ')
    
    shelf = request.args.get('shelf')
    
    baggage = request.args.get('baggage')
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    
    exit_point = request.args.get('exit_point')
    if exit_point == '':
        errors['exit_point'] = 'Заполните поле!'
    
    destination = request.args.get('destination')
    if destination == '':
        errors['destination'] = 'Заполните поле!'
    
    date = request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    
    if len(errors) > 0:
        return render_template('ticket.html', user=user, typ=typ, errors=errors, age=age, exit_point=exit_point, destination=destination, date=date, baggage=baggage, shelf=shelf )
    return render_template('info_ticket.html', user=user, typ=typ, errors=errors, age=age, exit_point=exit_point, destination=destination, date=date, baggage=baggage, shelf=shelf)