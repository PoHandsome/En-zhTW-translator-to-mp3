from .steps.step import StepException

class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, utils):
        data = None
        word = None
        utils.check_dir()
        words = self.steps[0].process(word, data, utils)
        for word in words:
            for step in self.steps[1:]:
                try:
                    data = step.process(word, data, utils)
                except StepException as e:
                    print('Exception happened:', e)
                    break
