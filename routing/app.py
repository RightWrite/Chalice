from chalice import Chalice

app = Chalice(app_name='routing')


@app.route('/')
def index():
    return {'view': 'index'}


@app.route('/a')
def a():
    return {'view': 'a'}


@app.route('/b')
def b():
    return {'view': 'b'}


@app.route('/user/{name}')
def user(name):
    return {'name': name}


@app.route('/country/{country}/city/{city}')
def user(city, country):
    return {'country': country, 'city': city}


@app.route('/greet/{name}')
def greet(name):
    result = {'name': name}
    parmas = app.current_request.query_params
    if parmas and parmas.get('include-greeting', 'false') == 'true':
        result['greeting'] = f'Hello, {name}'
    return result
