import sys
from googletrans import Translator
import clipboard
import keyboard



# Abrindo arquivo
def abrirArquivo():
    try:
        caminho = sys.argv[1]
    except:
        print("Passe o arquivo como arguemento na chamada do programa!" )
        exit()
    try:
        f = open(caminho, 'r', encoding='utf-8')
    except:
        print("Arquivo não encontrado!!")
        exit()
    string = f.read()
    f.close
    return string

# Tratar String
def tratarString(string):
    string = string.replace("-\n", "")
    string = string.replace("\n", " ")
    string = string.replace("\r\n", " ")
    string = string.replace("\r", "")
    return string

def gravaArquivo(string):
    caminho = sys.argv[1]
    f = open(caminho, 'w', encoding='utf-8')
    f.write(string)
    f.close

def traduzir(string):
    translator = Translator(service_urls=['translate.google.com.br',])
    string = translator.translate(string, dest='pt').text
    return string
    
def areaTransferencia():
    string = clipboard.paste()
    return string
def colarAreaTransf(string):
    clipboard.copy(string)


if __name__ == "__main__":
    
    while True:
        keyboard.wait('ctrl+x')
        string = areaTransferencia()
        string = tratarString(string)
        string = traduzir(string)
        colarAreaTransf(string)
        #string = abrirArquivo()
        #gravaArquivo(string)
        print("Pronto!")