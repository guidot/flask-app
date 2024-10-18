from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "<html>Hi! <a href=/2>Goto 2</a></html>"


@app.route("/2")
def second():
    return "<html>See me? <a href=/>Go back</a></html>"


if __name__ == "__main__":
    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)  # for ec2 usage
