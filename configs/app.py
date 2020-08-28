from chalice import Chalice

app = Chalice(app_name='demo')

@app.lambda_function()
def foo(event, context):
    pass

@app.lambda_function()
def bar(event, context):
    pass