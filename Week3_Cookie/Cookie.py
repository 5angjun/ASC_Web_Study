from flask import Flask
from flask import request, render_template, make_response

app = Flask(__name__)
@app.route('/')
def index():
    return f"Goto {request.headers.get('host')}/login"


@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form['id']
        response = make_response()
        response.set_cookie('ASC-cookie',data)
        print(response.headers)
        return response
    else:
        return render_template("login.html")

@app.route('/check_cookie')
def result():
    cookies = request.cookies.get('ASC-cookie') 

    if cookies:
        return cookies
    else:
        return "None Cookie"
    return   
    
     
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8888)