from googletrans import Translator
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from time import time

translator = Translator()

def userinput():
    userins = []
    while True:
        userin = input('Please enter the word(s) you want to translate (double press enter to stop enter): ')
        if not userin:
            break
        elif translator.translate(userin, dest = 'zh-TW').text == userin:
            print('Translate error: Please check your spelling.')
            continue
        else:
            userindet = userin.split()
            text = ''
            for i in userindet:
                if re.search('[a-zA-Z]', i):
                    text += i + ' '
            userins.append(text.strip())
    return userins

def get_sentences(userin):
    driver = webdriver.Chrome()

    driver.get('https://translate.google.com.au/?hl=zh-TW&tab=rT&sl=en&tl=zh-TW&text='+ userin +'&op=translate')
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span'))) # Wait until translate finish
    try:
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[2]/c-wiz/section/div/div/div[1]/div[2]/div/div[2]/div[1]').click()
    except:
        pass
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
    if sens == []:
        tts_en2 = gTTS('No example sentence for this word.')
    else:
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
        start_time = time()
        sens = get_sentences(userin)
        trans_to_mp3(userin, sens)
        end_time = time()
        print(f'The time spend on formatting this mp3 is {end_time - start_time}')

if __name__ == '__main__':
    main()