from flask import Flask, render_template, request, Markup
import apiai
import json
import sys


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
    else:
        print("Непонятно")


app = Flask(__name__)

@app.route("/")  # Root for login page is index "/"
def face():

    return render_template(
        "face.html", **locals())


if __name__ == "__main__":
    # It creates https access by last argument. It is need to be give to web-page permission to microphone
    app.run(host='0.0.0.0', port=8090) #, ssl_context='adhoc')  # If no need in https, just delete last argument
