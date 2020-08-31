from chalice import Chalice, Rate

app = Chalice(app_name='lambdaEventSource')


@app.schedule(Rate(5, unit=Rate.MINUTES))
def every_five_min(event):
    print(event.to_dict())


@app.on_cw_event({"source": ["aws.codecommit"]})
def on_code_commit_changes(event):
    print(event.to_dict())


@app.on_s3_event(bucket="my-mumbai-bucket123", events=["s3:ObjectCreated:*"],)
def handle_s3_event(event):
    app.log.error(f"Received event from bucket: {event.bucket} , Key: {event.key}")
