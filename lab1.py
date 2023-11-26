from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/lab1")
def lab():
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


@lab1.route("/menu")
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
        <h1><a href="/lab2" target="_blank">Лабораторная работа 2</a></h1>
        <h1><a href="/lab3" target="_blank">Лабораторная работа 3</a></h1>
        <h1><a href="/lab4" target="_blank">Лабораторная работа 4</a></h1>
        <h1><a href="/lab5/glavnaya_str" target="_blank">Лабораторная работа 5</a></h1>
        <footer>
            &copy; Алексей Носаков, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1/oak")
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


@lab1.route("/lab1/student")
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


@lab1.route("/lab1/python")
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


@lab1.route("/lab1/CХЭШ")
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

