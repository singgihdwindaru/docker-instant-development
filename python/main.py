from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # change the result value to test the real-time update by restarting 
    # this containered application
    result = 'Hello, World!'
    return result

if __name__ == '__main__':
    app.run(debug=True)