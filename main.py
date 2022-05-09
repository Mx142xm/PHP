from flask import Flask, redirect, render_template, abort

app = Flask(__name__)
a = [{'name': 'Alex', 'id': '1', 'surname': 'Turner', 'age': 36},
     {'name': 'Thom', 'id': '2', 'surname': 'Yorke', 'age': 53}]


@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('template1.html', a=a)


@app.route('/user/<n>')
def user(n):
    for i in a:
        if i['id'] == n:
            return render_template('template2.html', i=i)


if __name__ == '__main__':
    app.run(debug=True)
