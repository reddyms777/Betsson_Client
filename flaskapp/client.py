from flask import Flask, render_template, request, redirect
import requests
import urllib
app = Flask(__name__)
#app = bottle()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    if request.method == 'POST':
        # Fetch form data
       # userDetails = request.form
        name = request.forms.get('name')
        email1 = request.form['email']
        username1 = request.form['email']
        password1 = request.form['email']
       
        
payload= {'name': {name}, 'email':'email1','username':'username1' , 'password':'password1'}

r = requests.post('http://localhost:8066/users',json=payload)



if __name__ == "__main__":
     app.run(debug=True)
