from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def mission():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    text = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
            "Присоединяйся!"]
    return "</br>".join(text)


@app.route("/image_mars")
def show_image():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас Марс!</h1>
                        <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                      </body>
                    </html>"""


@app.route("/promotion_image")
def promotion_image():
    text = ["", "Человечество вырастает из детства.", "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
            "Присоединяйся!"]
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          </head>
                          <body>
                            <h1>Жди нас Марс!</h1>
                            <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                            {'</br>'.join(text)}
                          </body>
                        </html>"""


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
