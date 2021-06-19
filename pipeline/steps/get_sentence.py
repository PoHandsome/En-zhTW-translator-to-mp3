from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .step import Step

class GetSentence(Step):

    def process(self, word, data, utils):

        driver = webdriver.Firefox()
        
        driver.get('https://translate.google.com.au/?hl=zh-TW&tab=rT&sl=en&tl=zh-TW&text='+ word +'&op=translate')
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
