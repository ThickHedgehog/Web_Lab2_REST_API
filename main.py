from flask import Flask, jsonify, render_template, request, json
from flask_restful import Api
import json

app = Flask(__name__, static_folder="static")
api = Api(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quotes/<int:id>", methods=["GET", "PUT", "DELETE"])
def requestMethods(id):
    if request.method == "GET":
        with open("data.json", "r") as read_file:
            quotes = json.load(read_file)
        for quote in quotes:
            if quote["id"] == id:
                read_file.close()
                return quote, 200
        read_file.close()
        return "Quote not found", 404

    if request.method == "PUT":
        with open("data.json", "r") as read_file:
            quotes = json.load(read_file)
        read_file.close()
        content = request.get_json(force=True)
        for quote in quotes:
            content['id'] = int(content['id'])
            if content['id'] == quote['id']:
                quote['author'] = content['author']
                quote['years'] = content['years']
                quote['quote'] = content['quote']
                with open("data.json", "w") as write_file:
                    json.dump(quotes, write_file)
                write_file.close()
                return jsonify(quotes), 200
        return "Quote not found", 404

    if request.method == "DELETE":
        with open("data.json", "r") as read_file:
            quotes = json.load(read_file)
        quotes = [qoute for qoute in quotes if qoute["id"] != id]
        with open("data.json", "w") as write_file:
            json.dump(quotes, write_file)
        write_file.close()
        return f"Quote with id {id} is deleted.", 200


@app.route("/quotes", methods=["POST"])
def post():
    with open("data.json", "r") as read_file:
        quotes = json.load(read_file)
    read_file.close()
    content = request.get_json(force=True)
    for quote in quotes:
        content['id'] = int(content['id'])
        if content['id'] == quote['id']:
            return f"Quote with id {id} already exists", 400
    quotes.append(content)
    with open("data.json", "w") as write_file:
        json.dump(quotes, write_file)
    write_file.close()
    return jsonify(quotes), 201


if __name__ == '__main__':
    app.run()
