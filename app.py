from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

notes = [{'id':1,'title':'title1', 'des':'descripton of first note'},{'id':2,'title':'title2','des':'description of second note'}]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/notes')
def get_notes():
    return render_template('notes.html',notes=notes)

@app.route('/data', methods=['GET'])
def get_data():
    data = {'message': 'this is json response'}
    return jsonify(data)

@app.route('/notetaking')
def noteTaking():
    return render_template('notetaking.html')

if __name__=='__main__':
    app.run(debug=True)