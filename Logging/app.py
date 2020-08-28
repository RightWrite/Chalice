from chalice import Chalice
import logging

app = Chalice(app_name='Logging')
# Enable DEBUG logs.
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    app.log.debug("This is a debug statement")
    app.log.error("This is an error statement")
    return {'hello': 'world'}