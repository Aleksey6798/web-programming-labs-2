from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
<head>
    <title> Носаков Алексей Иванович, Лабораторная 1</title>
    <link rel="stylesheet" href="static/lab1.css">
</head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <b><p>Flask — фреймворк для создания веб-приложений на языке
        <b><br/>программирования Python, использующий набор инструментов
        <b><br/>Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        <b><br/>называемых микрофреймворков — минималистичных каркасов
        <b><br/>веб-приложений, сознательно предоставляющих лишь самые базовые возможности.<p>
        
        <h1><a href="/menu" target="_blank">Меню</a></h1>
        
        <h2><b>Реализованные роуты<h2>
            <io>
                <li><a href="/lab1/oak" target="_blank">/lab1/oak-дуб</a></li>
                <li><a href="/lab1/student" target="_blank">/lab1/student-студент</a></li>
                <li><a href="/lab1/python" target="_blank">/lab1/python-python</a></li>
                <li><a href="/lab1/CХЭШ" target="_blank">/lab1/CХЭШ-C#</a></li>
            </io>
        <footer>
            &copy; Алексей Носаков, ФБи-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторная работа</title>
        <link rel="stylesheet" href="static/lab1.css">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирования, часть 2. Список лаботраторных
        </header>

        <h1><a href="/lab1" target="_blank">Лабораторная работа 1</a></h1>

        <footer>
            &copy; Алексей Носаков, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <header>
        <link rel="stylesheet" href="static/lab1.css">
    </header>
    <h1 style= "color: blue";>Дуб</h1>
    <div style= "background-color: rgb(120, 215, 247);">
        <img src="'''+ url_for('static',filename='oak.jpg') + '''" style= "height: 500px"; "width: 500px";>
    </div>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <header>
        <link rel="stylesheet" href="static/lab1.css">
    </header>
    <body>
        <h1>Носаков Алексей Иванович</h1>
        <img src="'''+ url_for('static',filename='НГТУ.jpg') + '''">  
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <header>
        <link rel="stylesheet" href="static/lab1.css">
    </header>
    <body>
        <p>
        <br/><b>Python — это высокоуровневый язык программирования, отличающийся эффективностью, простотой и универсальностью использования. 
        <br/><b>Он широко применяется в разработке веб-приложений и прикладного программного обеспечения. А также в машинном обучении и обработке больших данных.<p>
        <p><br/><b>За счет простого и интуитивно понятного синтаксиса является одним из распространенных языков для обучения программированию.<p> 
        <img src="'''+ url_for('static',filename='Питон.jpg') + '''">   
    </body>
</html>
'''
@app.route("/lab1/CХЭШ")
def С():
    return '''
<!doctype html>
<html>
    <header>
        <link rel="stylesheet" href="static/lab1.css">
    </header>
    <body>
        <p>
        <br />C# — объектно-ориентированный язык программирования. Разработан в 1998—2001 годах группой инженеров компании Microsoft под руководством 
        <br />Андерса Хейлсберга и Скотта Вильтаумота как язык разработки приложений для платформы Microsoft .NET Framework.</p>
        <p><br/C# — объектно-ориентированный, ориентированный на компоненты язык программирования. C# предоставляет языковые конструкции для непосредственной поддержки такой концепции работы. 
        <br/>Благодаря этому C# подходит для создания и применения программных компонентов. С момента создания язык C# обогатился функциями для поддержки новых рабочих нагрузок и современными рекомендациями по разработке ПО. 
        <br/>В основном C# — объектно-ориентированный язык. Вы определяете типы и их поведение.<p>
        <img src="'''+ url_for('static',filename='сишка.jpg') + '''">   
    </body>
</html>
'''

@app.route("/lab2/example")
def example():
    name = 'Носаков Алексей'
    numberlab = '2'
    numbercurs = '3 курс'
    group = 'ФБИ-13'
    fruits = [
        {'name':'яблоки','price': 100},
        {'name':'груши','price': 120},
        {'name':'апельсины','price': 80},
        {'name':'мандарины','price': 95},
        {'name':'манго','price': 321}
    ]
    
    books = [
        {'namebook':'Убить пересмешника','author':'Харпер Ли', 'genre':'Роман','number_of_pages': 416},
        {'namebook':'Гордость и предубеждение','author':'Джейн Остен', 'genre':'Роман','number_of_pages': 384},
        {'namebook':'Дневник Анны Франк','author':'Анна Франк', 'genre':'Биография','number_of_pages': 296},
        {'namebook':'1984','author':'Джордж Оруэлл', 'genre':'Научная фантастика','number_of_pages': 320},
        {'namebook':'Гарри Поттер и философский камень','author':'Джоан Роулинг', 'genre':'Фэнтези','number_of_pages': 3636},
        {'namebook':'Властелин колец','author':'Дж.Р.Р.Толкин', 'genre':'Фэнтези','number_of_pages': 752},
        {'namebook':'Великий Гэтсби','author':'Ф. С. Фицджеральд', 'genre':'Драма','number_of_pages': 256},
        {'namebook':'Паутина Шарлотты','author':'Элвин Брукс Уайт', 'genre':'Фэнтези','number_of_pages': 288},
        {'namebook':'Маленькие женщины','author':'Луиза Мэй Олкотт', 'genre':'','number_of_pages': 382},
        {'namebook':'Хоббит','author':'Дж. Р. Р. Толкин', 'genre':'Фэнтези','number_of_pages': 256}
    ]
    return render_template('example.html', name=name,numberlab=numberlab,numbercurs=numbercurs, group=group, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/hobbies')
def hob():
    return render_template('hobbies.html')