from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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
""""