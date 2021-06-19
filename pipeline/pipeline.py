from .steps.step import StepException



class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self):
        data = None
        word = None
        words = self.steps[0].process(word, data)
        for word in words:
            for step in self.steps[1:]:
                try:
                    data = step.process(word, data)
                except StepException as e:
                    print('Exception happened:', e)
                    break
