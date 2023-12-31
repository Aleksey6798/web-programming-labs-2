from flask import Blueprint, redirect, url_for
lab2 = Blueprint('lab2',__name__)


@lab2.route("/lab2/example")
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



@lab2.route('/lab2/')
def la():
    return render_template('lab2.html')


@lab2.route('/lab2/hobbies')
def hob():
    return render_template('hobbies.html')


@lab2.route('/lab2/base')
def h():
    return render_template('base.html')