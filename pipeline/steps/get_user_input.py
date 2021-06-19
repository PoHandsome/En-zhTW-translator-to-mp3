import re

from googletrans import Translator

from .step import Step


class GetUserInput(Step):
    
    word = None
    def process(self, word, data, utils):  
        translator = Translator()
        userins = []
        while True:
            userin = input('Please enter the word(s) you want to translate (double press enter to stop enter): ')
            if utils.check_files(userin):
                print('file exists')
                continue
            elif not userin:
                print('start formatting!')
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
