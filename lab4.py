from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4',__name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET','POST'])
def login():
    error_username = None
    error_password = None
    
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html', username=username)

    if username == '':
        error_username = "Не введён логин"

    if password == '':
        error_password = "Не введён пароль"
    
    error = 'Невeрные логин и/или пароль'
    return render_template('login.html', error=error, error_username=error_username, error_password=error_password)

@lab4.route('/lab4/success')
def success():
    return render_template('success.html', username=username)

@lab4.route('/lab4/fridge',methods = ['GET','POST'])
def fridge():
    error_temperature = ""
    error_temperature1 = ""
    temperature = request.form.get('temperature')
    
    if request.method == 'POST':
        return render_template('fridge.html')
        
        
    if temperature == '':
        error_temperature = "ошибка: не задана температура"
        
    if int(temperature) < -12:
        error_temperature = "не удалось установить температуру — слишком низкое значение"
    
    if int(temperature) > -1:
        error_temperature = "не удалось установить температуру — слишком высокое значение"
    
    if int(temperature) in range(-12,-8):
        error_temperature1 = "Установлена температура:" + temperature + "°С***"
    
    if int(temperature) in range(-8,-4):
        error_temperature1 = "Установлена температура:" + temperature + "°С**"

    if int(temperature) in range(-4,0):
        error_temperature1 = "Установлена температура:" + temperature + "°С*"

    return render_template('fridge.html',error_temperature=error_temperature, temperature=temperature, error_temperature1=error_temperature1)


@lab4.route('/lab4/Order_grain',methods = ['GET','POST'])
def Order_grain():
    error_orger = None
    error_weight = None
    discount = None
    Result = None
    price = 0
    if request.method == 'GET':
        return render_template('Order_grain.html')
            
    grain = request.form.get('grain')
    weight = request.form.get('weight')
    sss = request.form.get('sss')
    price1 = price * weight

    Result = 'Заказ успешно сформирован. Вы заказали'+ ' ' + grain + ' ' + 'Вес:' + weight + 'т.' + ' ' + 'Cумма к оплате:' + price1 + 'руб' 
    
    if int(weight) > 500:
        discount = "такого объёма сейчас нет в наличии."

    if weight == '':
        error_weight = "Не введён вес"
        return render_template('Order_grain.html',error_weight=error_weight)
    
    if weight <= 0:
        discount = "Неверное значение веса"

    if grain == "barley":
        price = 12000
    elif grain == "oats":
        price = 8500
    elif grain == "wheat":
        price = 8700
    else:
        price = 14000

    
    if int(weight) > 50:
        disk = 0.1 * price1
        discount = "применена скидка за большой объём."
        

    return render_template('Order_grain.html',grain = grain, weight=weight, error_orger=error_orger,error_wight=error_weight, discount=discount, Result=Result,price1=price1)
