import audioop
import speech_recognition as sr
import gtts 
from playsound import playsound

frase = ""

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Diga alguma coisa: ')
        audio  = microfone.listen(source)
        
    try:
        frase = microfone.recognize_google(audio,language='pt-br')
        if(
            frase=='Guideon' 
            or frase=='Gideon' 
        ):
            print('Estou aqui senhor')
            print(f'\n {frase}')
            with open('frase.txt') as arquivo:
                for linha in arquivo:
                    frasef = gtts.gTTS(linha, lang='pt-br')
                    frasef.save('frase.mp3')
                    playsound('frase.mp3')
            exit()
        else:
            print(frase)
    except sr.UnknownValueError:
        print("Repita por favor")
    return frase

ouvir_microfone()