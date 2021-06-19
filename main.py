from pipeline.steps.get_user_input import GetUserInput
from pipeline.steps.get_sentence import GetSentence
from pipeline.steps.translate_to_mp3 import TranslateToMp3
from pipeline.pipeline import Pipeline
from utils import Utils

def main():
    steps = [
        GetUserInput(),
        GetSentence(),
        TranslateToMp3(),
    ]
    utils = Utils()

    p = Pipeline(steps)
    p.run(utils)
    print('Transform complete!')

if __name__ == '__main__':
    main()
