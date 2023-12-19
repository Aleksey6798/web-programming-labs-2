from flask import Blueprint, render_template

lab9 = Blueprint('lab9',__name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/Error.html'), 404


@lab9.route('/lab9/500')
def server_error():
    raise Exception("Произошла некоторая ошибка")

@lab9.app_errorhandler(Exception)
def er500(e):
    return render_template('lab9/500.html', error=e), 500