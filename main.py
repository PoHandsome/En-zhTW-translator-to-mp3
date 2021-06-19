from pipeline.steps.get_user_input import GetUserInput
from pipeline.steps.get_sentence import GetSentence
from pipeline.steps.translate_to_mp3 import TranslateToMp3
from pipeline.pipeline import Pipeline
from utils import Utils
from pipeline.steps.logger import Logger

def main():
    steps = [
        GetUserInput(),
        GetSentence(),
        TranslateToMp3(),
    ]
    utils = Utils()

    logger = Logger.logger()
    p = Pipeline(steps)
    p.run(utils, logger)
    logger.info('Transform complete!')

if __name__ == '__main__':
    main()
