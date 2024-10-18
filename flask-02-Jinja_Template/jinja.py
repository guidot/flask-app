from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", n1=2, n2="BLA")


@app.route("/calc")
def number():
    num1 = 11
    num2 = 12
    return render_template("body.html", value1=num1, value2=num2, sum=num1 + num2)


if __name__ == "__main__":
    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)  # for ec2 instances
