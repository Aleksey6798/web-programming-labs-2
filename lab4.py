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
        return render_template('success.html', username=username,password=password)

    if username == '':
        error_username = "Не введён логин"

    if password == '':
        error_password = "Не введён пароль"
    
    error = 'Невeрные логин и/или пароль'
    return render_template('login.html', error=error, error_username=error_username, error_password=error_password, username=username,password=password)

@lab4.route('/lab4/success')
def success():
    return render_template('success.html', username=username,password=password)

@lab4.route('/lab4/fridge',methods = ['GET','POST'])
def fridge():
    error_temperature = ""
    error_temperature1 = ""
    temperature = request.form.get('temperature')
    
    if request.method == 'GET':
        return render_template('fridge.html')
        
        
    if  not temperature:
        error_temperature = "ошибка: не задана температура"
    else: 
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

    
    if int(weight) > 500:
        discount = "такого объёма сейчас нет в наличии."
    elif int(weight) > 50:
        discount = "Применена скидка за большой объём."
    else :
        discount = ""

    if weight == '':
        error_weight = "Не введён вес"
        
    
    if int(weight) <= 0:
        discount = "Неверное значение веса"
        
    
    if grain == "barley":
        price = 12000
    elif grain == "oats":
        price = 8500
    elif grain == "wheat":
        price = 8700
    else:
        price = 14000
    
    weight = int(weight)
    price1 = price * weight
    
    if weight > 50:
        price1 = int(price1)
        price1 = 0.9 * price1

    return render_template('orger_success.html',grain = grain, weight=weight, error_orger=error_orger,error_wight=error_weight, discount=discount,price1=price1)






@lab4.route('/lab4/cookies',methods = ['GET','POST'])
def cookies():
    error = None
    if request.method == 'GET':
        return render_template('cookies.html')
    color = request.form.get('color')
    bg_color = request.form.get('bg_color')
    font_size = request.form.get('font-size')
    font_size = int(font_size)
    if color == bg_color:
        error = "Цвет текста не должен совпадать с цветом фона."

    if font_size is None or font_size == "":
        error = "Введите размер шрифта"
    elif font_size < 5 or font_size > 30:
        error = "Размер шрифта должен быть от 5px до 30px."
    
    headers = {
        'Set-Cookie': [ 
            'color=' + color + '; path=/',
            'bg_color=' + bg_color + '; path=/',
            'font_size=' + str(font_size) + "px" + '; path=/'      
        ],
        'Location': '/lab4/cookies'
    }
    return '', 303, headers