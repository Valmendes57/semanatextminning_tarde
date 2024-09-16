# biblioteca google de texto voz
from gtts import gTTS
#bibliotexa de , flask, render_templace - renderizar a página
from flask import Flask,render_template,request
import os

#criando o objeto flask
app = Flask(__name__)

# / - pagina principal
# POST - inserir
# GET - recuperar
@app.route('/senia',methods=['GET','POST'])
def abrir_assistente():
    audio_path = None
    if request.method == 'POST':
        #pegar o valor do html <textfield>
        texto = request.form['texto']
        # configurar o idioma
        lingua = 'pt'
        # Criação do objeto
        tts = gTTS(text=texto,lang=lingua)
        # Nome do arquivo de áudio
        audio_path = "static/audio_exemplo.mp3"

        # Salvar o arquivo
        tts.save(audio_path)
    return render_template('senia.html',audio_path=audio_path)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods=['POST'])
def logar():
   return render_template('login.html')

@app.route('/autenticar',methods=['POST', 'GET'])
def autenticar():
   # mock
   if request.method == 'POST':
       if request.form['senha'] == '123'and request.form['usuario'] == 'João':
          return render_template('senia.html')
       else:
            msg='erro na autenticação'
            return render_template('login.html',msg=msg)
        


if __name__ == '__main__':
  app.run(debug=True)
