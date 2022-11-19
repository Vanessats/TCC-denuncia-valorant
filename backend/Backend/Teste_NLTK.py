# coding: utf-8
import nltk

#nltk.download()

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

#print(base[1])

basetreinamento = [
('eu gosto', 'alegria'),
('este trabalho e agradável','alegria'),
('gosto de ficar no seu aconchego','alegria'),
('fiz a adesão ao curso hoje','alegria'),
('eu sou admirada por muitos','alegria'),
('adoro como você e','alegria'),
('adoro seu cabelo macio','alegria'),
('adoro a cor dos seus olhos','alegria'),
('somo tão amáveis um com o outro','alegria'),
('sinto uma grande afeição por ele','alegria'),
('quero agradar meus filhos','alegria'),
('me sinto completamente amado','alegria'),
('eu amo você','alegria'),
('que grande alivio','alegria'),
('a dor esta amenizando finalmente','alegria'),
('acho que me apaixonei','alegria'),
('amar e maravilhoso','alegria'),
('estou me sentindo muito animada','alegria'),
('me sinto muito bem hoje','alegria'),
('como o luar e belo','alegria'),
('o dia esta muito bonito','alegria'),
('nossa como sou afortunado','alegria'),
('as maravilhas do mundo','alegria'),
('recebi muito carinho hoje do meus colegas','alegria'),
('estou me sentindo reconfortada hoje','alegria'),
('e muito bom estar com os amigos','alegria'),
('estou muito contente com o resultado dos testes','alegria'),
('essa pintura esta bem brilhante','alegria'),
('temos água em abundancia','alegria'),
('que roupa delicada','alegria'),
('você e um grande comediante','alegria'),
('que bondade a sua em vir aqui','alegria'),
('o amor e lindo','alegria'),
('nossa amizade vai durar para sempre','alegria'),
('estou eufórica com a noticia','alegria'),
('ele e realmente fiel a mim','alegria'),
('vou dar uma grande festa para comemorar meu aniversário','alegria'),
('graças a deus que eu enxerguei o certo','alegria'),
('essa e a melhor escolhas de todas','alegria'),
('o mais incrível e você minha bela','alegria'),
('e tão engraçado tentar explicar','alegria'),
('e emocionante estar neste lugar','alegria'),
('estou cativada pelo seu olhar','alegria'),
('estou loucamente apaixonada','alegria'),
('eu nunca tive duvidas','alegria'),
('estou rodeada pelo seu abraço','alegria'),
('eu vejo estrelas pelo caminho','alegria'),
('eu sinto o sol sempre que você esta por perto','alegria'),
('eu estou sorrindo de orelha a orelha','alegria'),
('isso vale a pena','alegria'),
('finalmente você colocou meu amor em primeiro lugar','alegria'),
('nós dançamos noite adentro','alegria'),
('seu amor e brilhante','alegria'),
('toquei muitos corações durante o meu caminho','alegria'),
('eu serei sua amiga e companheira','alegria'),
('você me traz de volta a vida','alegria'),
('você e como um sonho doce','alegria'),
('adoro este doce de frutas','alegria'),
('meu suco favorito','alegria'),
('estou agradecida pela ajuda','alegria'),
('e um enorme prazer ter você em nossa equipe','alegria'),
('trabalhar em equipe e o melhor','alegria'),
('me sinto flutuando no ar','alegria'),
('a brisa esta agradável hoje','alegria'),
('ótimo e compatível','alegria'),
('somos compatíveis um com o outro','alegria'),
('o órgão e compatível com o paciente','alegria'),
('estou contente fui aceita na faculdade','alegria'),
('fui aprovada no meu exame','alegria'),
('fui beneficiada pela minha empresa','alegria'),
('eu sou muito cativante','alegria'),
('estou contente com o apoio','alegria'),
('como este lugar e confortável','alegria'),
('e bom estar quente neste frio','alegria'),
('um elogio nunca e demais','alegria'),
('vou te chamar para comemorar','alegria'),
('e desejável a sua presença em nossa apresentação','alegria'),
('sou muito grata a você','alegria'),
('me dedico muito naquilo que faço','alegria'),
('estou completamente apaixonada ','alegria'),
('vamos agitar essa noite ','alegria'),
('você significa muito para mim','alegria'),
('vamos agir sem preconceitos e julgamentos','alegria'),
('finalmente completei a minha coleção, maravilhoso','alegria'),
('eu sou sua rainha ','alegria'),
('satisfatoriamente eu anuncio o vencedor dos jogos','alegria'),
('você me atrai facilmente ','alegria'),
('aquele rapaz e extremamente atraente','alegria'),
('sinto-me viva ','alegria'),
('sinto-me em paz ','alegria'),
('estamos tendo muito lucro','alegria'),
('muito bem esta tudo em ordem agora ','alegria'),
('podemos arrumar um emprego juntos ','alegria'),
('a arrumação esta terminada, que alívio','alegria'),
('o câncer e benigno ','alegria'),
('o amor e abundante','alegria'),
('vamos ser caridosos este natal','alegria'),
('com todo esse charme você irá atrair a todos','alegria'),
('nossa como você e charmoso querido ','alegria'),
('sou querida pelos meu amigos','alegria'),
('seja cuidadoso com os meus sentimentos','alegria'),
('estou comovido com tamanha caridade','alegria'),
('um chá quente e reconfortante','alegria'),
('que alegria ter vocês aqui ','alegria'),
('vamos aplaudir o vencedor ','alegria'),
('palmas para a aniversariante','alegria'),
('desejo a você tudo de bom','alegria'),
('hora de apreciar um bom vinho','alegria'),
('aprecio sua presença em minha escola','alegria'),
('anseio por seus próximos trabalhos','alegria'),
('maravilhoso jogo amistoso','alegria'),
('e ótimo que os ânimos tenham se apaziguado','alegria'),
('concretizei finalmente meu sonho','alegria'),

('por favor não me abandone','tristeza'),
('não quero ficar sozinha','tristeza'),
('não me deixe sozinha','tristeza'),
('estou abatida','tristeza'),
('ele esta todo abatido','tristeza'),
('tão triste suas palavras','tristeza'),
('seu amor não e mais meu','tristeza'),
('estou aborrecida','tristeza'),
('isso vai me aborrecer','tristeza'),
('estou com muita aflição','tristeza'),
('me aflige o modo como fala','tristeza'),
('estou em agonia com meu intimo','tristeza'),
('não quero fazer nada','tristeza'),
('me sinto ansiosa e tensa','tristeza'),
('não consigo parar de chorar','tristeza'),
('não consigo segurar as lagrimas','tristeza'),
('e muita dor perder um ente querido','tristeza'),
('estou realmente arrependida','tristeza'),
('acho que o carma volta, pois agora sou eu quem sofro','tristeza'),
('você não cumpriu suas promessas','tristeza'),
('me sinto amargurada','tristeza'),
('coitado esta tão triste','tristeza'),
('já e tarde de mais','tristeza'),
('nosso amor acabou','tristeza'),
('essa noite machuca só para mim','tristeza'),
('eu não estou mais no seu coração','tristeza'),
('você mudou comigo','tristeza'),
('quando eu penso em você realmente dói','tristeza'),
('como se fosse nada você vê minhas lagrimas','tristeza'),
('você disse cruelmente que não se arrependeu','tristeza'),
('eu nunca mais vou te ver','tristeza'),
('ela esta com depressão','tristeza'),
('a depressão aflige as pessoas','tristeza'),
('estar depressivo e muito ruim','tristeza'),
('estou derrotada e deprimida depois deste dia','tristeza'),
('e comovente te ver dessa maneira','tristeza'),
('e comovente ver o que os filhos do brasil passam','tristeza'),
('como me sinto culpada','tristeza'),
('estou abatida','tristeza'),
('a ansiedade tomou conta de mim','tristeza'),
('as pessoas não gostam do meu jeito','tristeza'),
('adeus passamos bons momentos juntos','tristeza'),
('sinto sua falta','tristeza'),
('ele não gostou da minha comida','tristeza'),
('estou sem dinheiro para a comida','tristeza'),
('queria que fosse o ultimo dia da minha vida','tristeza'),
('você está com vergonha de mim','tristeza'),
('ela não aceitou a minha proposta','tristeza'),
('era o meu ultimo centavo','tristeza'),
('reprovei de ano na faculdade','tristeza'),
('afinal você só sabe me desfazer','tristeza'),
('eu falhei em tudo nessa vida','tristeza'),
('eu fui muito humilhado','tristeza'),
('e uma história muito triste','tristeza'),
('ninguem acredita em mim','tristeza'),
('eu não sirvo para nada mesmo','tristeza'),
('droga, não faço nada direito','tristeza'),
('sofrimento em dobro na minha vida','tristeza'),
('fui demitida essa semana','tristeza'),
('as crianças sofrem ainda mais que os adultos','tristeza'),
('pra mim um dia e ruim, o outro e pior','tristeza'),
('de repente perdi o apetite','tristeza'),
('oh que dia infeliz','tristeza'),
('estamos afundados em contas','tristeza'),
('nem um milagre pode nos salvar','tristeza'),
('só me resta a esperança','tristeza'),
('pior que isso não pode ficar','tristeza'),
('meu salário e baixo','tristeza'),
('não passei no vestibular','tristeza'),
('ninguem se importa comigo','tristeza'),
('ninguem lembrou do meu aniversário','tristeza'),
('tenho tanto azar','tristeza'),
('o gosto da vingança e amargo','tristeza'),
('sou uma mulher amargurada depois de que você me deixou','tristeza'),
('estou desanimada com a vida','tristeza'),
('e um desanimo só coitadinha','tristeza'),
('a derrota e depressiva','tristeza'),
('discriminar e desumano','tristeza'),
('que desanimo','tristeza'),
('e uma desonra para o pais','tristeza'),
('a preocupação deveria nos levar a ação não a depressão','tristeza'),
('passamos ao desalento e a loucura','tristeza'),
('aquele que nunca viu a tristeza nunca reconhecerá a alegria','tristeza'),
('cuidado com a tristeza ela e um vicio','tristeza')
]

baseteste =[('não precisei pagar o ingresso','alegria'),
('se eu ajeitar tudo fica bem','alegria'),
('minha fortuna ultrapassa a sua','alegria'),
('sou muito afortunado','alegria'),
('e benefico para todos esta nova medida','alegria'),
('ficou lindo','alegria'),
('achei esse sapato muito simpático','alegria'),
('estou ansiosa pela sua chegada','alegria'),
('congratulações pelo seu aniversário','alegria'),
('delicadamente ele a colocou para dormir','alegria'),
('a musica e linda','alegria'),
('sem musica eu não vivo','alegria'),
('conclui uma tarefa muito difícil','alegria'),
('conclui minha graduação','alegria'),
('estou muito contente com tudo','alegria'),
('eu confio em você','alegria'),
('e um prazer conhecê-lo','alegria'),
('o coleguismo de vocês e animador','alegria'),
('estou aproveitando as ferias','alegria'),
('vamos aproveitar as ferias','alegria'),
('e muito divertido este jogo','alegria'),
('vamos ter muita diversão','alegria'),
('não achei que me divertiria tanto assim','alegria'),
('vou consentir o orçamento ao cliente','alegria'),
('com o consentimento dos meus pais podemos nos casar','alegria'),
('eu adorei este perfume','alegria'),
('sua bondade e cativante','alegria'),
('estou despreocupada','alegria'),
('não me preocupo com o que aconteceu','alegria'),
('me sinto completamente segura','alegria'),
('estimo muito o seu trabalho','alegria'),
('somos estimados por nossa família','alegria'),
('concretizamos nossa ideia','alegria'),
('nosso ideal foi alcançado','alegria'),
('estamos muito felizes juntos','alegria'),
('estou tão animada com os preparativos para o casamento','alegria'),
('você será muito amado meu filho','alegria'),
('os apaixonados são maravilhosos','alegria'),
('agradeço imensamente o seu apoio nestes dias','alegria'),
('esta comida me parece muito atraente','alegria'),
('você me completa','alegria'),
('poderemos completar o projeto hoje!','alegria'),
('estamos namorando','alegria'),
('estou namorando este vestido a um tempo','alegria'),
('pude comprar meu celular hoje','alegria'),
('e um deleite poder compartilhar minhas vitórias','alegria'),
('ela e um boa garota','alegria'),
('estivemos em um ótimo show','alegria'),
('isso tudo e um erro','tristeza'),
('eu sou errada eu sou errante','tristeza'),
('tenho muito dó do cachorro','tristeza'),
('e dolorida a perda de um filho','tristeza'),
('essa tragedia vai nos abalar para sempre','tristeza'),
('perdi meus filhos','tristeza'),
('perdi meu curso','tristeza'),
('sou só uma chorona','tristeza'),
('você e um chorão','tristeza'),
('se arrependimento matasse','tristeza'),
('me sinto deslocado em sala de aula','tristeza'),
('foi uma passagem fúnebre','tristeza'),
('nossa condolências e tristeza a sua perda','tristeza'),
('desanimo, raiva, solidão ou vazies, depressão','tristeza'),
('vivo te desanimando','tristeza'),
('estou desanimado','tristeza'),
('imperador sanguinário, depravado e temeroso','tristeza'),
('meu ser esta em agonia','tristeza'),
('este atrito entre nos tem que acabar','tristeza'),
('a escuridão desola meu ser','tristeza'),
('sua falsa preocupação','tristeza'),
('sua falsidade me entristece','tristeza'),
('quem esta descontente com os outros esta descontente consigo próprio','tristeza'),
('a torcida esta descontente com a demissão do tecnico','tristeza'),
('estou bastante aborrecido com o jornal','tristeza'),
('me sinto solitário e entediado','tristeza'),
('a vida e solitária para aqueles que não são falsos','tristeza'),
('como com compulsão depois da depressão','tristeza'),
('estou me desencorajando a viver','tristeza'),
('ele desencoraja minhas vontades','tristeza'),
('isso vai deprimindo por dentro','tristeza'),
('acho que isso e defeituoso','tristeza'),
('os remedios me derrubam na cama','tristeza'),
('a depressão vai me derrubar','tristeza'),
('suas desculpas são falsas','tristeza'),
('não magoe as pessoas','tristeza')]


stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
stopwordsnltk.append('vou')
stopwordsnltk.append('tão')
#print(stopwordsnltk)

def removestopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases

#print(removestopwords(base))

def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming

frasescomstemmingtreinamento = aplicastemmer(basetreinamento)
frasescomstemmingteste = aplicastemmer(baseteste)
#print(frasescomstemming)

def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras

palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)
palavrasteste = buscapalavras(frasescomstemmingteste)
#print(palavras)

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequenciatreinamento = buscafrequencia(palavrastreinamento)
frequenciateste = buscafrequencia(palavrasteste)
#print(frequencia.most_common(50))

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = buscapalavrasunicas(frequenciateste)
#print(palavrasunicastreinamento)

#print(palavrasunicas)

def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicastreinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

caracteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])
#print(caracteristicasfrase)

basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento)
basecompletateste = nltk.classify.apply_features(extratorpalavras, frasescomstemmingteste)
#print(basecompleta[15])

# constroi a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)
print(classificador.labels())
#print(classificador.show_most_informative_features(20))

print(nltk.classify.accuracy(classificador, basecompletateste))

erros = []
for (frase, classe) in basecompletateste:
    #print(frase)
    #print(classe)
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado, frase))
#for (classe, resultado, frase) in erros:
#    print(classe, resultado, frase)

from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []
for (frase, classe) in basecompletateste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)

#esperado = 'alegria alegria alegria alegria medo medo surpresa surpresa'.split()
#previsto = 'alegria alegria medo surpresa medo medo medo surpresa'.split()
matriz = ConfusionMatrix(esperado, previsto)
print(matriz)

# 1. Cenário
# 2. Número de classes - 16%
# 3. ZeroRules - 21,05%

