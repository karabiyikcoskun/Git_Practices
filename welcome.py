from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>WELCOME TO TURAN CYBER HUB</h1>"
            "<h1> the conflict</h1>" \
            "<h3> the tird line/h3>"
            "<h4> the forth line</h4>"
            "<h5> the fifth line</h5>"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80) 

ali veli 









