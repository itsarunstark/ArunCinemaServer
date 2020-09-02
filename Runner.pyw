from flask import Flask,render_template
import sys
print(sys.argv)

app = Flask(__name__)


@app.route("/")
def Hell():
    return render_template("index.html")
@app.route("/video")
def startvid():
    return render_template("index2.html",Mysrc="/static/MyVid.mp4")
    
app.run(host=sys.argv[1],port=sys.argv[2],debug=True)
