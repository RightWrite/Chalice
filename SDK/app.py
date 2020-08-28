from chalice import Chalice

app = Chalice(app_name='sdktest')

@app.route('/', cors=True)
def index():
    return {'hello': 'world'}

@app.route('/foo', cors=True)
def foo():
    return {'foo': True}

@app.route('/hello/{name}', cors=True)
def hello_name(name):
    return {'hello': name}

@app.route('/users/{user_id}', methods=['PUT'], cors=True)
def update_user(user_id):
    return {"msg": "fake updated user", "userId": user_id}