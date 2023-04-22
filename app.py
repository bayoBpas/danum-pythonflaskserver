from flask import Flask

app = Flask("My Flask Application")


@app.route("/")
def hello():
    return "<h1>My First Hello World!</h1>"

def add(val_1, val_2):
    added_vals = val_1 + val_2
    return added_vals

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
