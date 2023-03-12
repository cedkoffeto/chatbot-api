import openai
from flask import Flask, request
from gpt.gpt_utils import extract_answer_from_gpt_response_text
from config import QUESTION_PREFIX, ANSWER_PREFIX, CHAT_GENERAL_CONTEXT_TEXT
from gpt.chat_context import ChatContext
from models.User import User
import json

app = Flask(__name__)
openai.api_key =  "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"

@app.route('/', methods=['GET'])
def index():
    return 'Hello World'


@app.route('/api/question-answering', methods=['POST'])
def question_answering():
    data = request.get_json()
    question = data['question']
    model = data.get('model', 'davinci')


    user = User(
        username='Francis',
        business_name='BestEvents',
        bio="""
I am an event planner. I organize events for companies and individuals.
I have been doing this for 10 years.
I have a lot of experience in organizing events.
I have organized events for companies like Google, Facebook, Microsoft, etc.
        """,
        services=[
            'Event planning',
            'Event organization',
            'Event management',
            'Event marketing',
        ]
    )

    chat_session_context = ChatContext()

    final_question = chat_session_context \
        .add_answer(CHAT_GENERAL_CONTEXT_TEXT) \
        .add_context(user.get_context()) \
        .add_question(question) \
        .wait_for_answer()


    print(final_question)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            { "role": "system", "content": CHAT_GENERAL_CONTEXT_TEXT },
            { "role": "user", "content": str(user.get_context()) },
            { "role": "user", "content": question },
        ],
    )

    answer = response.choices[0]["message"]["content"]

    return {'answer': answer}

