from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request,redirect, url_for, session 
import psycopg2

lab5 = Blueprint('lab5',__name__)
def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base_for_aleksey",
        user="aleksey_knowledge_base",
        password="123")
    
    return conn

@lab5.route('/lab5/str')
def lab():
    return render_template("lab5str.html")

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route('/lab5/')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"


@lab5.route('/lab5/users')
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur = conn.cursor()

    cur.execute("SELECT username FROM users;")

    results = cur.fetchall()

    dbClose(cur, conn)

    return render_template('users.html', users=results)


@lab5.route('/lab5/glavnaya_str')
def glav():
    username = session.get('user_name')
    return render_template('glavnaya_str.html',username=username)


@lab5.route('/lab5/registr', methods=["GET","POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template("registr.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните всё поле")
        print(errors)
        return render_template("registr.html", errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;",(username,))

    if cur.fetchone() is not None:
        errors.append("Пользователь с данными уже существует")
        
        conn.close()
        cur.close()
        
        return render_template("registr.html",errors=errors)
    
    cur.execute("INSERT INTO users (username,password) VALUES (%s, %s);", (username,hashPassword))
    
    conn.commit
    conn.close()
    cur.close()
    
    return redirect("/lab5/login")

@lab5.route('/lab5/login', methods=["GET","POST"])
def loginPage():
    errors = []

    if request.method == "GET":
        return render_template("login.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("login.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['user_name'] = username
        dbClose(cur, conn)
        return redirect("/lab5/glavnaya_str")
    
    else:
        errors.append("Неправильный логин или пароль")
        return render_template("login.html", errors=errors)

@lab5.route('/lab5/new_article', methods=["GET","POST"])
def createArticle():
    errors = []

    userID = session.get('id')
    username = session.get('user_name')
    
    if userID is not None:
        if request.method =="GET":
            return render_template("new_article.html", username=username)
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(article_text) == 0:
                errors.append("Заполните текст")
                return render_template("new_article.html", errors = errors)
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, article_text))
            
            
            new_articl_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_articl_id}")

    return redirect("/lab5/login")


@lab5.route('/lab5/articles')
def list_articles():
    userID = session.get('id')
    username = session.get("username")
    
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        
        cur.execute("SELECT id, title FROM articles WHERE user_id = %s;", (userID,))
        articles_data = cur.fetchall()
        
        articles = [{'id': row[0], 'title': row[1]} for row in articles_data]

        dbClose(cur, conn)

        return render_template('articles.html', articles=articles, username=username)

    return redirect("/lab5/login")

@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur,conn)

        if articleBody is None:
            return "Not found!"
            
        text = articleBody[1].splitlines()
    return render_template("articleN.html", article_text=text, title_article=articleBody[0], username=session.get("username"))

