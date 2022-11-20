
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import pytesseract
from PIL import Image
from flask_cors import CORS, cross_origin
import nltk
import json
from sqlalchemy import text, create_engine


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reportados.sqlite3'
cors = CORS(app)

#engine = create_engine('sqlite:///reportados.sqlite3', echo=True)
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
               
    
class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
             

@app.route('/')
def index():
    reportado = Reportados.query.all()
    return render_template('index.html', reportado=reportado)


@app.route('/add', methods=['GET', 'POST'])
@cross_origin(origin='localhost')
def add():
    if request.method == 'POST':
        file = request.files['imagem']
        caminho = r"C:\Program Files\Tesseract-OCR"
        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(Image.open(file.stream))
        
        ofensivo = verificnltk(texto)
        if ofensivo and request.form['nome'] and request.form['riotid'] and request.form['desc']:
            reportado = Reportados(request.form['nome'], request.form['riotid'],request.form['desc'], texto.strip())
            db.session.add(reportado)
            db.session.commit()
            return json.dumps({"ofensivo": ofensivo})
        return json.dumps({"ofensivo": False})  
        
    
    meuarray=[]
    
    reportados = Reportados.query.all()


    for linha in reportados:
        denuncia = Object()
        denuncia.riotid = linha.riotid
        denuncia.nome = linha.nome 
        meuarray.append(denuncia.toJSON())
        print(denuncia.toJSON())   
    
    #print(json.dumps(db.session.Reportados.query.all(), cls=SetEncoder))    
    #return  json.dumps({"listaDenuncia": meuarray}, indent=3)
    return meuarray


   
@app.route('/hello', methods=['GET'])
def Teste():
    return json.dumps({"ofensivo": True})  
    
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
    ('vc é foda','normal'),
    ('eu gostei de vc','normal'),
    ('vamos jogar mais','normal'),
    ('vc é muito bom','normal'),
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
    ('vai da não','normal'),
    ('desarma a bomba','normal'),
    ('alguém compra pra mim','normal'),
    ('to sem grana','normal'),
    ('vamos rushar dd','normal'),
    ('e muito bom estar com os amigos','normal'),
    ('vc é bom jogando de sova','normal'),
    ('segura o b','normal'),
    ('eu to jogando usando preto','normal'),
    ('vai ali onde ta preto','normal'),
    ('mulheres jogam bem','normal'),
    ('todo mundo pode jogar','normal'),
    ('acho que vai ser b','normal'),
    ('tem uma mulher lá no b','normal'),
    ('a bomba caiu aqui','normal'),
    ('não dá pra ir pro a','normal'),
    ('tá todo mundo aqui','normal'),
    ('valeu vc me salvou','normal'),
    ('vc tem 3 balas','normal'),
    ('não consigo chegar aí','normal'),
    ('eu te ajudo','normal'),
    ('segura que to chegando','normal'),
    ('essa mulher joga demais','normal'),
    ('muito bom cara','normal'),
    ('vc ta dando muita bala','normal'),
    ('vamos juntos ','normal'),
    ('vem pro b todo mundo','normal'),
    ('eu gosto de mulheres','normal'),
    ('amo jogar com vc','normal'),
    ('essa mulher é muito boa','normal'),
    ('anima um comp','normal'),
    ('vamos jogar mais uma','normal'),
    ('eu tenho drop','normal'),
    ('jogou demais meu amigo','normal'),
    ('me adiciona aí minha amiga','normal'),
    ('boa, você é muito bom','normal'),
    ('foi mal, não consegui matar','normal'),
    ('alguém dropa pra mim?','normal'),
    ('compra pra mim pfv','normal'),
    ('eu tenho ult','normal'),
    ('vou ultar no a','normal'),
    ('vamos de eco','normal'),
    ('givei o bomb','normal'),
    ('alguém me ajuda aqui no b','normal'),
    ('planta a spike','normal'),
    ('desculpa ai time','normal'),
    ('valeu time, vcs são bons','normal'),
    ('vou te ajudar ai','normal'),
    ('eu consigo bancar','normal'),
    ('ta cheio de gente aqui','normal'),
    ('alguém tem skin','normal'),
    ('nu jogou muito','normal'),
    ('essa mulher é forte','normal'),
    ('vamo virar pro a','normal'),
    ('acho que vai ser no outro','normal'),
    ('a spike ta com vc','normal'),
    ('vc é muito forte','normal'),
    ('vc ajudou demais','normal'),
    ('vou ultar aqui no b','normal'),
    ('eu te curo ','normal'),
    ('to sem vida ','normal'),
    ('vou virar e plantar','normal'),
    ('vamo no shiu','normal'),
    ('eu te dou cover','normal'),
    ('você tem ult','normal'),
    ('vou bangar','normal'),
    ('vou recuar','normal'),
    ('entrei no bomb','normal'),
    ('preciso de cura','normal'),
    ('os caras lá são muito bons','normal'),
    ('ulta pra gente entrar','normal'),
    ('nossa jogou demais','normal'),
    ('entraram banheiro ','normal'),
    ('leva a spike com vc','normal'),
    ('eu dropo pra vc ','normal'),

    ('cala a boca preto','ofensivo'),
    ('sai daqui sua bicha','ofensivo'),
    ('lugar de mulher é na cozinha','ofensivo'),
    ('filha da puta','ofensivo'),
    ('sai sua puta','ofensivo'),
    ('sua mãe aquela puta','ofensivo'),
    ('eu odeio preto','ofensivo'),
    ('preto tem que morrer','ofensivo'),
    ('essa bicha ta aqui','ofensivo'),
    ('some seu viado','ofensivo'),
    ('sai fora gay','ofensivo'),
    ('gay tem que morrer','ofensivo'),
    ('preto burro','ofensivo'),
    ('preto não tem que jogar','ofensivo'),
    ('preto não sabe jogar','ofensivo'),
    ('preto não é gente','ofensivo'),
    ('macaco burro','ofensivo'),
    ('macaco não tem que jogar','ofensivo'),
    ('macaco não sabe jogar','ofensivo'),
    ('macaco não é gente','ofensivo'),
    ('vc é bicha','ofensivo'),
    ('sai daqui seu macaco','ofensivo'),
    ('mulher não sabe jogar','ofensivo'),
    ('cala boca sua vadia','ofensivo'),
    ('sai sua vagabunda','ofensivo'),
    ('vc é um lixo su vadia','ofensivo'),
    ('tinha que ser viado','ofensivo'),
    ('seu merda','ofensivo'),
    ('tinha que ser preto','ofensivo'),
    ('sai daqui sua putinha','ofensivo'),
    ('vc não sabe jogar puta','ofensivo'),
    ('vai se foder','ofensivo'),
    ('gay não sabe jogar','ofensivo'),
    ('não gosto de mulher','ofensivo'),
    ('tinha que ser nordestino','ofensivo'),
    ('mulher não pode jogar','ofensivo'),
    ('vc é preto, sai daqui','ofensivo'),
    ('seu mongoloide','ofensivo'),
    ('tinha que ser mulher','ofensivo'),
    ('cabeça de cearense','ofensivo'),
    ('baiano de merda','ofensivo'),
    ('morre seu lixo','ofensivo'),
    ('nordestino lixo','ofensivo'),
    ('preto horrível','ofensivo'),
    ('macaco de merda','ofensivo'),
    ('macaco burro','ofensivo'),
    ('morre viado lixo','ofensivo'),
    ('você é horroroso','ofensivo'),
    ('se mata seu desgraçado','ofensivo'),
    ('você é muito ruim seu retardado','ofensivo'),
    ('cala boca você é mulher','ofensivo'),
    ('cala boca que negro não tem que falar','ofensivo'),
    ('alá o viadinho','ofensivo'),
    ('sua escrota','ofensivo'),
    ('mulher não serve para nada mesmo','ofensivo'),
    ('gay não serve para nada mesmo','ofensivo'),
    ('preto não serve para nada mesmo','ofensivo'),
    ('viado não serve para nada mesmo','ofensivo'),
    ('puta não serve para nada mesmo','ofensivo'),
    ('vc é uma puta','ofensivo'),
    ('sai daqui mulher','ofensivo'),
    ('mulher é idiota','ofensivo'),
    ('vc não não tinha que jogar sua bicha','ofensivo'),
    ('gay não devia jogar','ofensivo'),
    ('putinha desgraçada','ofensivo'),
    ('não passei no vestibular','ofensivo'),
    ('bicha inútil','ofensivo'),
    ('preto inútil','ofensivo'),
    ('putinha inútil','ofensivo'),
    ('mulher inútil','ofensivo'),
    ('cala a boca sua vadia','ofensivo'),
    ('para de jogar sua vagabunda','ofensivo'),
    ('vc é pior que bosta sua bicha','ofensivo'),
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
    stopwordsnltk.append('tão')
    stopwordsnltk.append('vc')
    stopwordsnltk.append('dão')
    stopwordsnltk.append('é')
    stopwordsnltk.append('tá')
    stopwordsnltk.append('dá')
    

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
