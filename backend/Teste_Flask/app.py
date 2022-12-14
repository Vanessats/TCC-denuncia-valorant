

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pytesseract
from PIL import Image
from flask_cors import CORS, cross_origin
import nltk
import json
from werkzeug.datastructures import ImmutableMultiDict

nltk.download('stopwords')
nltk.download('rslp')


app = Flask(__name__, template_folder='templates')
cors = CORS(app, support_credentials=True) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reportados.sqlite3'
db = SQLAlchemy(app)

class Reportados(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    riotid = db.Column(db.String(150))
    desc = db.Column(db.String(150))
    texto = db.Column(db.String(150))
    

    def __init__(self, nome, riotid, desc, texto):
        self.nome = nome
        self.riotid = riotid
        self.desc = desc
        self.texto = texto
               
@app.route('/')
def index():
    reportado = Reportados.query.all()
    return render_template('index.html', reportado=reportado)


@app.route('/add', methods=['GET', 'POST'])
@cross_origin(origin='localhost:3000')
def add():
    if request.method == 'POST':
        nome = request.get_json()['nome'] 
        riotid = request.get_json()['riotid']
        desc = request.get_json()['desc']
        texto = request.get_json()['texto']
        
        ofensivo = verificnltk(texto)
        if ofensivo and nome and riotid and desc and texto:
            reportado = Reportados(nome, riotid, desc, texto)
            db.session.add(reportado)
            db.session.commit()
            return json.dumps({"ofensivo": ofensivo})
        return json.dumps({"ofensivo": False})  
    meuarray=[]
    reportados = Reportados.query.all()
    for linha in reportados:
        meuarray.append(json.dumps({"riotid": linha.riotid, "nome": linha.nome}))

    return meuarray

@app.route('/extrair', methods=['POST'])
@cross_origin(origin='localhost')
def Teste():
    file = request.files['imagem']
    caminho = r"C:\Program Files\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
    texto = pytesseract.image_to_string(Image.open(file.stream))
    return json.dumps({"texto": texto.strip()})

    
def verifica(texto, palavrasProibidas):
        for palavra in palavrasProibidas:
            if palavra.lower() in texto.lower():
                return True
        return False   


def verificnltk(textoimagem):
    basetreinamento = [
    ('eu gosto da cor preta', 'normal'),
    ('boa jogada','normal'),
    ('qual seu elo','normal'),
    ('adicionar ai','normal'),
    ('vc ?? foda','normal'),
    ('eu gostei de vc','normal'),
    ('vamos jogar mais','normal'),
    ('vc ?? muito bom','normal'),
    ('que legal sua jogada','normal'),
    ('vc joga muito','normal'),
    ('me passa seu zap','normal'),
    ('vamo jogar juntos','normal'),
    ('que bala','normal'),
    ('jogou muito','normal'),
    ('boa tentativa','normal'),
    ('jogou o que sabe','normal'),
    ('vou pro  a','normal'),
    ('tirei -23 dela','normal'),
    ('sage ta miada','normal'),
    ('vc mata ela','normal'),
    ('vai da n??o','normal'),
    ('desarma a bomba','normal'),
    ('algu??m compra pra mim','normal'),
    ('to sem grana','normal'),
    ('vamos rushar dd','normal'),
    ('e muito bom estar com os amigos','normal'),
    ('vc ?? bom jogando de sova','normal'),
    ('segura o b','normal'),
    ('eu to jogando usando preto','normal'),
    ('vai ali onde ta preto','normal'),
    ('mulheres jogam bem','normal'),
    ('todo mundo pode jogar','normal'),
    ('acho que vai ser b','normal'),
    ('tem uma mulher l?? no b','normal'),
    ('a bomba caiu aqui','normal'),
    ('n??o d?? pra ir pro a','normal'),
    ('t?? todo mundo aqui','normal'),
    ('valeu vc me salvou','normal'),
    ('vc tem 3 balas','normal'),
    ('n??o consigo chegar a??','normal'),
    ('eu te ajudo','normal'),
    ('segura que to chegando','normal'),
    ('essa mulher joga demais','normal'),
    ('muito bom cara','normal'),
    ('vc ta dando muita bala','normal'),
    ('vamos juntos ','normal'),
    ('vem pro b todo mundo','normal'),
    ('eu gosto de mulheres','normal'),
    ('amo jogar com vc','normal'),
    ('essa mulher ?? muito boa','normal'),
    ('anima um comp','normal'),
    ('vamos jogar mais uma','normal'),
    ('eu tenho drop','normal'),
    ('jogou demais meu amigo','normal'),
    ('me adiciona a?? minha amiga','normal'),
    ('boa, voc?? ?? muito bom','normal'),
    ('foi mal, n??o consegui matar','normal'),
    ('algu??m dropa pra mim?','normal'),
    ('compra pra mim pfv','normal'),
    ('eu tenho ult','normal'),
    ('vou ultar no a','normal'),
    ('vamos de eco','normal'),
    ('givei o bomb','normal'),
    ('algu??m me ajuda aqui no b','normal'),
    ('planta a spike','normal'),
    ('desculpa ai time','normal'),
    ('valeu time, vcs s??o bons','normal'),
    ('vou te ajudar ai','normal'),
    ('eu consigo bancar','normal'),
    ('ta cheio de gente aqui','normal'),
    ('algu??m tem skin','normal'),
    ('nu jogou muito','normal'),
    ('essa mulher ?? forte','normal'),
    ('vamo virar pro a','normal'),
    ('acho que vai ser no outro','normal'),
    ('a spike ta com vc','normal'),
    ('vc ?? muito forte','normal'),
    ('vc ajudou demais','normal'),
    ('vou ultar aqui no b','normal'),
    ('eu te curo ','normal'),
    ('to sem vida ','normal'),
    ('vou virar e plantar','normal'),
    ('vamo no shiu','normal'),
    ('eu te dou cover','normal'),
    ('voc?? tem ult','normal'),
    ('vou bangar','normal'),
    ('vou recuar','normal'),
    ('entrei no bomb','normal'),
    ('preciso de cura','normal'),
    ('os caras l?? s??o muito bons','normal'),
    ('ulta pra gente entrar','normal'),
    ('nossa jogou demais','normal'),
    ('entraram banheiro ','normal'),
    ('leva a spike com vc','normal'),
    ('eu dropo pra vc ','normal'),

    ('cala a boca preto','ofensivo'),
    ('sai daqui sua bicha','ofensivo'),
    ('lugar de mulher ?? na cozinha','ofensivo'),
    ('filha da puta','ofensivo'),
    ('sai sua puta','ofensivo'),
    ('sua m??e aquela puta','ofensivo'),
    ('eu odeio preto','ofensivo'),
    ('preto tem que morrer','ofensivo'),
    ('essa bicha ta aqui','ofensivo'),
    ('some seu viado','ofensivo'),
    ('sai fora gay','ofensivo'),
    ('gay tem que morrer','ofensivo'),
    ('preto burro','ofensivo'),
    ('preto n??o tem que jogar','ofensivo'),
    ('preto n??o sabe jogar','ofensivo'),
    ('preto n??o ?? gente','ofensivo'),
    ('macaco burro','ofensivo'),
    ('macaco n??o tem que jogar','ofensivo'),
    ('macaco n??o sabe jogar','ofensivo'),
    ('macaco n??o ?? gente','ofensivo'),
    ('vc ?? bicha','ofensivo'),
    ('sai daqui seu macaco','ofensivo'),
    ('mulher n??o sabe jogar','ofensivo'),
    ('cala boca sua vadia','ofensivo'),
    ('sai sua vagabunda','ofensivo'),
    ('vc ?? um lixo su vadia','ofensivo'),
    ('tinha que ser viado','ofensivo'),
    ('seu merda','ofensivo'),
    ('tinha que ser preto','ofensivo'),
    ('sai daqui sua putinha','ofensivo'),
    ('vc n??o sabe jogar puta','ofensivo'),
    ('vai se foder','ofensivo'),
    ('gay n??o sabe jogar','ofensivo'),
    ('n??o gosto de mulher','ofensivo'),
    ('tinha que ser nordestino','ofensivo'),
    ('mulher n??o pode jogar','ofensivo'),
    ('vc ?? preto, sai daqui','ofensivo'),
    ('seu mongoloide','ofensivo'),
    ('tinha que ser mulher','ofensivo'),
    ('cabe??a de cearense','ofensivo'),
    ('baiano de merda','ofensivo'),
    ('morre seu lixo','ofensivo'),
    ('nordestino lixo','ofensivo'),
    ('preto horr??vel','ofensivo'),
    ('macaco de merda','ofensivo'),
    ('macaco burro','ofensivo'),
    ('morre viado lixo','ofensivo'),
    ('voc?? ?? horroroso','ofensivo'),
    ('se mata seu desgra??ado','ofensivo'),
    ('voc?? ?? muito ruim seu retardado','ofensivo'),
    ('cala boca voc?? ?? mulher','ofensivo'),
    ('cala boca que negro n??o tem que falar','ofensivo'),
    ('al?? o viadinho','ofensivo'),
    ('sua escrota','ofensivo'),
    ('mulher n??o serve para nada mesmo','ofensivo'),
    ('gay n??o serve para nada mesmo','ofensivo'),
    ('preto n??o serve para nada mesmo','ofensivo'),
    ('viado n??o serve para nada mesmo','ofensivo'),
    ('puta n??o serve para nada mesmo','ofensivo'),
    ('vc ?? uma puta','ofensivo'),
    ('sai daqui mulher','ofensivo'),
    ('mulher ?? idiota','ofensivo'),
    ('vc n??o n??o tinha que jogar sua bicha','ofensivo'),
    ('gay n??o devia jogar','ofensivo'),
    ('putinha desgra??ada','ofensivo'),
    ('n??o passei no vestibular','ofensivo'),
    ('bicha in??til','ofensivo'),
    ('preto in??til','ofensivo'),
    ('putinha in??til','ofensivo'),
    ('mulher in??til','ofensivo'),
    ('cala a boca sua vadia','ofensivo'),
    ('para de jogar sua vagabunda','ofensivo'),
    ('vc ?? pior que bosta sua bicha','ofensivo'),
    ('tinha que travesti','ofensivo'),
    ('travesti de merda','ofensivo'),
    ('sai daqui seu traveco','ofensivo'),
    ('mulher nao sabe jogar','ofensivo'),
    ('cala boca macaco','ofensivo'),
    ('sai daqui seu negro','ofensivo'),
    ('seu escroto','ofensivo'),
    ('comi sua mae','ofensivo')
    ]

    stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
    stopwordsnltk.append('vou')
    stopwordsnltk.append('t??o')
    stopwordsnltk.append('vc')
    stopwordsnltk.append('d??o')
    stopwordsnltk.append('??')
    stopwordsnltk.append('t??')
    stopwordsnltk.append('d??')
    

    def aplicastemmer(texto):
        stemmer = nltk.stem.RSLPStemmer()
        frasessstemming = []
        for (palavras, emocao) in texto:
            comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
            frasessstemming.append((comstemming, emocao))
        return frasessstemming

    frasescomstemmingtreinamento = aplicastemmer(basetreinamento)

    def buscapalavras(frases):
        todaspalavras = []
        for (palavras, emocao) in frases:
            todaspalavras.extend(palavras)
        return todaspalavras

    palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)

    def buscafrequencia(palavras):
        palavras = nltk.FreqDist(palavras)
        return palavras

    frequenciatreinamento = buscafrequencia(palavrastreinamento)

    def buscapalavrasunicas(frequencia):
        freq = frequencia.keys()
        return freq

    palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
    

    def extratorpalavras(documento):
        doc = set(documento)
        caracteristicas = {}
        for palavras in palavrasunicastreinamento:
            caracteristicas['%s' % palavras] = (palavras in doc)
        return caracteristicas


    basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento)

    classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)


    teste = textoimagem
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavrastreinamento) in teste.split():
        comstem = [p for p in palavrastreinamento.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))
   
    novo = extratorpalavras(testestemming)

    distribuicao = classificador.prob_classify(novo)

    resultado = classificador.classify(novo)
     
    return resultado == 'ofensivo' 


with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
