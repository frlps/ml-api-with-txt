import os
from flask import Flask, request, redirect, url_for, flash,jsonify
from werkzeug.utils import secure_filename
from textblob import TextBlob



app = Flask('__name__')

@app.route('/', methods=['GET'])
def home():
    return 'Bem vindo ao teste de sentimento!!!'


@app.route('/getfile', methods=['POST'])
def getfile():
    file = request.files['file']
    file_r = file.read()
    return file_r 


@app.route('/sentimento/<frase>', methods=['GET'])
def sentimento(frase):
    text_Blob_Test = TextBlob(frase)
    text_Blob_Test_ING = text_Blob_Test.translate(to='en')
    polaridade = text_Blob_Test_ING.sentiment.polarity
    return f'A polaridade da frase é: {polaridade}'

@app.route('/sentimentotxt/getfile', methods=['POST'])
def sentimentotxt():
    file = request.files['file']
    file_r = file.read()
    file_r_s = file_r.decode("utf-8") 
    text_Blob_Test = TextBlob(file_r_s)
    text_Blob_Test_ING = text_Blob_Test.translate(to='en')
    polaridade = text_Blob_Test_ING.sentiment.polarity
    return f'A polaridade da frase é: {polaridade}'
    #return str(text_Blob_Test_ING)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=3001)