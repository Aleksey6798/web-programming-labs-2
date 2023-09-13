from flask import Flask, redirect, url_for
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
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке
        <br/>программирования Python, использующий набор инструментов
        <br/>Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        <br/>называемых микрофреймворков — минималистичных каркасов
        <br/>веб-приложений, сознательно предоставляющих лишь самые базовые возможности.<p>
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
    <body>
        <h1>Дуб</h1>
        <img src="'''+ url_for('static',filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
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
    <body>
        <p>
        <br />Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, 
        <br />ориентированный на повышение производительности разработчика, 
        <br />читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.</p>
        <img src="'''+ url_for('static',filename='Питон.jpg') + '''">   
    </body>
</html>
'''
@app.route("/lab1/CХЭШ")
def С():
    return '''
<!doctype html>
<html>
    <body>
        <p>
        <br />C# — объектно-ориентированный язык программирования. Разработан в 1998—2001 годах группой инженеров компании Microsoft под руководством 
        <br />Андерса Хейлсберга и Скотта Вильтаумота как язык разработки приложений для платформы Microsoft .NET Framework.</p>
        <img src="'''+ url_for('static',filename='сишка.jpg') + '''">   
    </body>
</html>
'''