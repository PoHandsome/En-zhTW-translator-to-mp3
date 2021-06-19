from pipeline.steps.get_user_input import GetUserInput
from pipeline.steps.get_sentence import GetSentence
from pipeline.steps.translate_to_mp3 import TranslateToMp3
from pipeline.pipeline import Pipeline


def main():
    steps = [
        GetUserInput(),
        GetSentence(),
        TranslateToMp3(),
    ]

    p = Pipeline(steps)
    p.run()
    print('Transform complete! mp3 files are in the same file directory!')

if __name__ == '__main__':
    main()
