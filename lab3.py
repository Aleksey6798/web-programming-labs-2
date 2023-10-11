from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def f():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    user = request.args.get('user')
    return render_template('form1.html', user=user)