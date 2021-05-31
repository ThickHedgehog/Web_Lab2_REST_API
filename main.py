from flask import Flask, jsonify, render_template, request, json
from flask_restful import Api
import json

app = Flask(__name__, static_folder="static")
api = Api(app)


# Загрузка стартовой страницы
@app.route("/")
def index():
    return render_template("index.html")


# Реализация методов GET, PUT, DELETE через получение на вход id
@app.route("/quotes/<int:id>", methods=["GET", "PUT", "DELETE"])
def requestMethods(id):
    if request.method == "GET":
        # Парсим JSON и записываем его в переменную словаря
        with open("data.json", "r") as read_file:
            quotes = json.load(read_file)
        # Возвращаем все данные с таким же id как на входе
        for quote in quotes:
            if quote["id"] == id:
                read_file.close()
                return quote, 200
        read_file.close()
        return "Quote not found", 404

    if request.method == "PUT":
        # Парсим JSON и записываем его в переменную словаря
        with open("data.json", "r") as read_file:
            quotes = json.load(read_file)
        read_file.close()
        # Получаем на вход JSON из запроса
        content = request.get_json(force=True)
        for quote in quotes:
            # Преобразуем id в int, т.к. на вход пришел string
            content['id'] = int(content['id'])
            # Заменяем данными из полученного JSON
            if content['id'] == quote['id']:
                quote['author'] = content['author']
                quote['years'] = content['years']
                quote['quote'] = content['quote']
                # Записываем в JSON
                with open("data.json", "w") as write_file:
                    json.dump(quotes, write_file)
                write_file.close()
                # Возвращаем JSON
                return jsonify(quotes), 200
        return "Quote not found", 404

    if request.method == "DELETE":
        # Парсим JSON и записываем его в переменную словаря
        with open("data.json", "r") as read_file:
            quotes = json.load(read_file)
        # Перезаписываем все данные, кроме тех, где id равен полученному
        quotes = [qoute for qoute in quotes if qoute["id"] != id]
        # Записываем в JSON
        with open("data.json", "w") as write_file:
            json.dump(quotes, write_file)
        write_file.close()
        return f"Quote with id {id} is deleted.", 200


# Реализация метода POST
@app.route("/quotes", methods=["POST"])
def post():
    # Парсим JSON и записываем его в переменную словаря
    with open("data.json", "r") as read_file:
        quotes = json.load(read_file)
    read_file.close()
    # Получаем на вход JSON из запроса
    content = request.get_json(force=True)
    for quote in quotes:
        # Преобразуем id в int, т.к. на вход пришел string
        content['id'] = int(content['id'])
        # Ошибка о том, что запись с таким id уже есть
        if content['id'] == quote['id']:
            return f"Quote with id {id} already exists", 400
    # Добавляем запись
    quotes.append(content)
    # Записываем в JSON
    with open("data.json", "w") as write_file:
        json.dump(quotes, write_file)
    write_file.close()
    # Возвращаем JSON
    return jsonify(quotes), 201


if __name__ == '__main__':
    app.run()
