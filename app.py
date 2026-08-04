from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    data = {'message': 'this is json response'}
    return jsonify(data)

@app.route('/notetaking')
def noteTaking():
    return render_template('notetaking.html')

if __name__=='__main__':
    app.run(debug=True)