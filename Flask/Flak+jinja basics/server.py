from flask import Flask,render_template
from datetime import datetime as dt
import random
app=Flask(__name__)

@app.route('/')
def home():
    year = dt.now().year
    random_number=random.randint(1,78956)
    return render_template("index.html",num=random_number,yr=year,name="Juwairia")

if __name__=="__main__":
    app.run(debug=True)