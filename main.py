# -*- coding: utf-8 -*-
from flask import Flask, render_template, json, request
import apiai
import sys


app = Flask(__name__)


def textMessage(update):
    request = apiai.ApiAI('167a082419914df2b44700f2bcda6087').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'ZhuldyzAIbot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        print("Действие: " + str(responseJson['result']['action']))
        print("Ответ: " + str(responseJson['result']['fulfillment']['speech']))
        print("Вероятность: " + str(responseJson['result']['score']*100))
        return str(responseJson['result']['fulfillment']['speech'])
    else:
        print("Непонятно")
        return "Простите, я не поняла Вас"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    #name = request.speechText["saidText"]
    #name = input("Passs: ")
    if request.form['text']:
        print(request.form['text'])
        phrase2 = textMessage(request.form['text'])
    else:
        phrase2 = ''
    name = "Happy"
    mood = name
    return json.dumps({'face': 1, 'len': str(name), 'path': str("/static/" + str(mood) + ".png"), 'phrase': phrase2})


if __name__ == '__main__':
    app.run(debug=True)
