from flask import Flask, redirect, make_response, abort

app = Flask(__name__)
a = [{'name': 'Alex', 'id': '1', 'surname': 'Turner', 'age': 36},
     {'name': 'Thom', 'id': '2', 'surname': 'Yorke', 'age': 53}]


@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def users():
    c = ''
    for i in range(len(a)):
        b = a[i]['name'] + ' ' + a[i]['surname'] + '<br>'
        c = c + '<a href="http://127.0.0.1:5000/user/%s" > %s</a>' % (a[i]['id'], b)
    response = make_response('<h1> %s</h1> ' %(c))
    return response


@app.route('/user/<n>')
def user(n):
    for i in range(len(a)):
        if n == a[i]['id']:
            response = make_response('<h1> Name: %s ' ' %s <br> Age: %s </h1> ' % (a[i]['name'], a[i]['surname'], a[i]['age']))
            return response
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)