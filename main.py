from flask import Flask, render_template # импортируем Flask и Jinja

app = Flask(__name__) # определяем приложением Flask

@app.route('/') # Роут для главной страницы
def main():
    return render_template('index.html')

@app.route('/departures/<departure>') # Роут для страница Направлений
def departures():
    return render_template('departure.html')

@app.route('/tour/<int:id>') # роут для Туров
def tours():
    return render_template('tour.html')

app.run() # запуск приложения Flask