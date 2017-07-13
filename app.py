import plivo, plivoxml
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/make_outgoing', methods=['GET','POST'])
def make_outgoing():

    username = "darfat21170710162618"
    password = "asdf1234"
    # Render the html file
    return render_template('make_outgoing.html', username=username, password=password)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')