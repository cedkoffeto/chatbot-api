#
# Class for utils related to GPT treatment
#
from config import QUESTION_PREFIX, ANSWER_PREFIX


'''
Extracts the answer from the GPT response 
Example of resposonse text:
fine\nA: and you ?

Extracted answer:fine
'''
def extract_answer_from_gpt_response_text(response_text: str):
    return response_text.split(f'\n{QUESTION_PREFIX}')[0].strip().replace(f'{ANSWER_PREFIX}', '')


'''
Builds a question with context to be used in GPT
Example of context:
fine\nA: and you ?

Example of question: How are you?

Built question:
fine\nA: and you ?\nQ: How are you?\nA:
'''
def build_gpt_question_with_context(question: str, context: str):
    return f"{context}\n\n{QUESTION_PREFIX}{question}\n{ANSWER_PREFIX}"


def remove_all_occurences_of_string_from_string(string: str, to_remove: str):
    return string.replace(to_remove, '')