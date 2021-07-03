import pytest
import os
import glob

from gtranstomp3.main import main
from gtranstomp3.utils import Utils
from gtranstomp3.logger import Logger
from gtranstomp3.pipeline.pipeline import Pipeline
from gtranstomp3.pipeline.steps import get_user_input, get_sentence, translate_to_mp3, read_files 

class Test:  
    
    def setup(self):
        
        # setup global variable for the test and remove all exist output files
        
        self.utils = Utils()
        self.logger = Logger.logger()
        files = glob.glob(self.utils.outdir + '*.mp3')
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print(f'Error: {f} {e.strerror}')

    def test_read_files(self):
        rf = read_files.Readfile()
        words = rf.process(self.utils, self.logger)
        assert isinstance(words, list)

    def _test_u_input(self, set_input, exp_output):       
        d = []
        ci = get_user_input.CheckInput()
        set_output = ci.process(set_input, d, self.utils, self.logger)
        assert set_output == exp_output

    def test_u_input(self):
        self._test_u_input('word', 'word')
        self._test_u_input('I am good', ['I am good'])
        self._test_u_input(['I am good', 'You are bad'], ['I am good', 'You are bad']) 
        self._test_u_input(['old','' , 'new', ''], ['old', 'new'])
        self._test_u_input(['old', 'new', '', 'good', '65413', '', '', 'fkjg', '.'], ['old', 'new', 'good'])
        self._test_u_input(['yes', 'no', '', 'hi', '65413', '', '', 'fkjgkl', '.'], ['yes', 'no', 'hi'])

    def _test_g_sentence(self, set_input):
        d = []
        gs = get_sentence.GetSentence()
        set_output = gs.process(set_input, d, self.utils, self.logger)
        
        if set_output != []:
            assert isinstance(set_output, list)
            for sentence in set_output:
                assert set_input in sentence
        else:
            assert set_output == []

    def test_g_sentence(self):
        self._test_g_sentence('word')
        self._test_g_sentence('warm up')
        self._test_g_sentence('')
        self._test_g_sentence('dkjfkjflf')
       
    def _test_transmp3(self, word, sentence, exp_fail=False):
        self.utils.check_dir()
        assert os.path.exists(self.utils.outdir)
        
        ttm = translate_to_mp3.TranslateToMp3()
        ttm.process(word, sentence, self.utils, self.logger)
        
        if exp_fail:
            assert self.utils.check_files(word) == False
        else:
            assert self.utils.check_files(word)

    def test_transmp3(self):
        self._test_transmp3('old', ['how old are you'])
        self._test_transmp3('old', [])
        self._test_transmp3('', '', exp_fail=True)
        self._test_transmp3('ooo', ['aaaaaaaaaaa'])

    def test_pipeline(self): 
        steps = [
            get_user_input.CheckInput(),
            get_sentence.GetSentence(),
            translate_to_mp3.TranslateToMp3(),
        ]
        pl = Pipeline(steps)
        assert pl.steps == steps
        self.steps = steps

    def test_project(self):
        main()
        


        
