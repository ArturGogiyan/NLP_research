from flask import Flask
from flask import request

app = Flask(__name__)


@app.get('/echo')
def root():
    echo = request.args.get('echo')
    if echo is not None:
        return echo
    else:
        return 'Hello!'


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=4242)
