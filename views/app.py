from chalice import Chalice
from chalice import BadRequestError, Response

app = Chalice(app_name="views")


@app.route("/")
def badrequest():
    raise BadRequestError("This is a default request")


@app.route("/badrequest")
def badrequest():
    raise BadRequestError("This is a bad request")


@app.route("/badrequest1")
def badrequest1():
    return Response(
        body="This is a custom bad request",
        status_code=400,
        headers={"Content-Type": "text/plain"},
    )


@app.route("/resource/{value}", methods=["PUT"])
def put_test(value):
    return {"value": value}


@app.route("/myview", methods=["POST", "PUT"])
def request_method():

    if app.current_request.method == "PUT":
        return {"method": "PUT"}
    return {"method": "post"}


@app.route("/myview1", methods=["POST"])
def request_method():
    return {"method": "post"}


@app.route("/myview1", methods=["PUT"])
def request_method():
    return {"method": "put"}


@app.route("/bin-echo", methods=["POST"], content_types=["application/octet-stream"])
def bin_echo():
    raw_request_body = app.current_request.raw_body
    return Response(
        body=raw_request_body,
        status_code=200,
        headers={"Content-Type": "application/octet-stream"},
    )
