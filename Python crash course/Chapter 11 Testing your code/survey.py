class AnonymousSurvey:
    """ Collect anonymous answer to a survey question."""

    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        """ Show the survey question. """
        print(self.question)

    def store_responses(self, new_response):
        """ Store a response to the survey. """
        self.responses.append(new_response.title())

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")