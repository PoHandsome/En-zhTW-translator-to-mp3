from googletrans import Translator
from gtts import gTTS

from .step import Step

class TranslateToMp3(Step):

    def process(self, word, data):
        translator = Translator()
        i = word
        dest_text = translator.translate(i, dest = 'zh-TW').text
        tts_en1 = gTTS(i + '. ' + i + '. ' + i, slow = True)
        tts_zh = gTTS(dest_text, lang = 'zh-TW')
        sens = data
        if sens == []:
            tts_en2 = gTTS('No example sentence for this word.')
        else:
            tts_en2 = gTTS('. '.join(sens))
        tts_end = gTTS('This is the end of ' + i)
        with open(i + '.mp3', 'wb') as f:
            tts_en1.write_to_fp(f)
            tts_zh.write_to_fp(f)
            tts_en2.write_to_fp(f)
            tts_end.write_to_fp(f)

