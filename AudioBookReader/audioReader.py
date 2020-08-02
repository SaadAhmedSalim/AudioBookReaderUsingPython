import pyttsx3
import PyPDF2

book = open('German.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print('Total page found ',pages)

engine= pyttsx3.init()

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')


print('Previous Rate was ',rate)
print('Previous volume was ',volume)
print('Previous voice was ',voice)

newVoiceRate = 50
while newVoiceRate <= 200:
    engine.setProperty('rate', newVoiceRate)
    engine.say('Testing different voice rates.')
    engine.runAndWait()
    newVoiceRate = newVoiceRate + 50

engine.setProperty('rate', 125)
engine.setProperty('voice','english+f2')

newVolume = 0.1
while newVolume <= 1:
    engine.setProperty('volume', newVolume)
    engine.say('Testing different voice volumes.')
    engine.runAndWait()
    newVolume = newVolume + 0.4


print('New Voice Rate is ',newVoiceRate)
print('New Volume is',newVolume)

engine.say('Testing Completed!')
engine.say('Hello Master Saad, I am Edith! thanks for your waiting. I’m glad you’re here!')
engine.say('Searching Book. Book is found.')
engine.say('Initiating reading')
engine.runAndWait()

for num in range(5,6):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
