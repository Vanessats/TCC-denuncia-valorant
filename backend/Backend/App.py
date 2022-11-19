from unittest import result
import os
import cv2
import pytesseract
import numpy as np
import requests
import base64
import json
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import re
import nltk
from PIL import Image


app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
cors = CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload(): 
    file = request.files['imagem']
    
    caminho = r"C:\Program Files\Tesseract-OCR"

    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
    
    texto = pytesseract.image_to_string(Image.open(file.stream))
    
    proibido = ['Preto','gay','puta']
    
    ofensivo = verifica(texto, proibido)
    if ofensivo:
        return "texto ofensivo" 
    
    return ("texto nao ofensivo")



def verifica(texto, palavrasProibidas):
        for palavra in palavrasProibidas:
            if palavra.lower() in texto.lower():
                return True
        return False








    


    
      

   

if __name__ == "__main__":
    app.run(debug=True)
    
    

    
