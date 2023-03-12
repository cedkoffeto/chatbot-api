from config import QUESTION_PREFIX, ANSWER_PREFIX


class ChatContext:
    ''' ChatContext class
    '''
    context = ''

    def __init__(self, init_context_text = ""):
        self.context = str(init_context_text)


    def add_question(self, question):
        self.context += f"\n{QUESTION_PREFIX}{question}"
        return self

    def add_answer(self, answer):
        self.context += f"\n{ANSWER_PREFIX}{answer}"
        return self
    
    def wait_for_answer(self):
        self.context += f"\n{ANSWER_PREFIX}"
        return self
    
    def add_context(self, context):
        self.context += f"\n{context}"
        return self

    def __str__(self) -> str:
        return self.context
    