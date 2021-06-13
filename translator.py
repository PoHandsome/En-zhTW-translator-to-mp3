from googletrans import Translator
from gtts import gTTS
from selenium import webdriver

translator = Translator()

def userinput():
    userins = []
    while True:
        userin = input('Please enter the word(s) or sentence(s) you want to translate: ')
        if userin:
            userins.append(userin)
        else:
            break
    return userins

def get_sentences(userin):
    driver = webdriver.Chrome()

    driver.get('https://translate.google.com.au/?hl=zh-TW&tab=rT&sl=en&tl=zh-TW&text='+ userin +'&op=translate')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[2]/c-wiz/section/div/div/div[1]/div[2]/div/div[2]/div[1]').click()

    ex_sentences = driver.find_elements_by_tag_name('html-blob')
    sens = []
    for i in ex_sentences:
        sen = i.text
        if sen:
            sens.append(sen)
        else:
            pass
    driver.close()
    return sens

def trans_to_mp3(userin, sens):
    dest_text = translator.translate(userin, dest = 'zh-TW').text
    i = userin
    tts_en1 = gTTS(i + '. ' + i + '. ' + i, slow = True)
    tts_zh = gTTS(dest_text, lang = 'zh-TW')
    tts_en2 = gTTS('. '.join(sens))
    tts_end = gTTS('This is the end of ' + userin)
    with open(userin + '.mp3', 'wb') as f:
        tts_en1.write_to_fp(f)
        tts_zh.write_to_fp(f)
        tts_en2.write_to_fp(f)
        tts_end.write_to_fp(f)

def main():
    userins = userinput()
    for userin in userins:
        sens = get_sentences(userin)
        trans_to_mp3(userin, sens)

if __name__ == '__main__':
    main()