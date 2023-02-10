"""
Produces speach mp3 from text
"""

from gtts import gTTS

lvl = 20
eng = 'ice'
rus = 'лёд'
legend = 'Айс кользкий лёд'

engine = gTTS(text=eng, lang='en')
engine.save('./../static/audio/' + str(lvl) + '_en.mp3')

engine = gTTS(text=rus, lang='ru')
engine.save('./../static/audio/' + str(lvl) + '_ru.mp3')

engine = gTTS(text=legend, lang='ru')
engine.save('./../static/audio/' + str(lvl) + '_legend.mp3')
