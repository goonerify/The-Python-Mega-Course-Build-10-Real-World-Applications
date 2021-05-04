from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'Home page content goes here!'

@app.route('/about')
def about():
    return 'About page content goes here!'

if __name__=='__main__':
    app.run(debug=True)
