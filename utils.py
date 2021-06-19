import os

class Utils:

    def __init__(self):
        self.outdir = 'output/'

    def check_dir(self):
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

    def check_files(self, word):
        filename = word + '.mp3'
        return os.path.isfile(self.outdir + filename)

