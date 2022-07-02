from flask import Flask
from flask import request, render_template, make_response

app = Flask(__name__)
@app.route('/')
def index():
    return f"Goto {request.headers.get('host')}/vuln"


@app.route('/vuln')
def vuln():
    payload = request.args.get('payload')

    if payload is None:
        return "Give me the payload"
    
    return render_template('xss_safe.html',payload=payload)


     
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8888)