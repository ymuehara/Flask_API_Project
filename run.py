from flask import Flask

app = Flask(__name__)


@app.route("/<int:number>", methods=["GET", "POST"])
def Hello(number):
    return f"Hello World =) {number}"


if __name__=="__main__":
    app.run(debug=True)