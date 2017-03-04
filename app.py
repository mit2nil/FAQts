from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def downloadFile():

    if request.method == 'GET':
        return render_template("index.html")
    
@app.route('/query', methods=['GET'])
def my_form_post():

    text = request.form['search']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":
    app.run()


    
