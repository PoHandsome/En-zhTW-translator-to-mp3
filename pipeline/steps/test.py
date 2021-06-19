from googletrans import Translator

translator = Translator()
dest_text = translator.translate('old', dest = 'zh-TW').text
print(dest_text)
