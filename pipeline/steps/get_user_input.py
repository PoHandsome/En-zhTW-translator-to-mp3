import re

from googletrans import Translator

from .step import Step

class GetUserInput(Step):
    
    """
    user input the word they want to translate in once, after input, the process will automaticly complete.
    """

    word = None
    def process(self, word, data, utils, logger):  
        translator = Translator()
        userins = []
        while True:
            userin = input('Please enter the word(s) you want to translate (double press enter to stop enter): ')
            if utils.check_files(userin):
                logger.warning('file exists')
                continue
            elif not userin:
                logger.info('start formatting!')
                break
            #check if the word is readable
            elif translator.translate(userin, dest = 'zh-TW').text == userin:
                logger.warning('Translate error: Please check your spelling.')
                continue
            #delete words that are not english
            else:
                userindet = userin.split()
                text = ''
                for i in userindet:
                    if re.search('[a-zA-Z]', i):
                        text += i + ' '
                        userins.append(text.strip())
        return userins
