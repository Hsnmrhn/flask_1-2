from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!"

@app.route("/second")
def head2():
    return "This Is The Second Page"

@app.route("/third")
def head3():
    return "This Is The Third Page"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'



if __name__ == '__main__':

   # app.run(debug=True, port=30000)
     app.run(host= '0.0.0.0', port=8081)