import re

from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import json

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/math/', methods=['GET'])
def hello_world():
    question_type = request.args.get('type') or ''
    with open('math.json') as f:
        import random

        data = json.load(f)
        possible = list(data.keys())
        print(len(possible))
        if question_type:
            possible = [key for key in possible if data[key]['domain'] == question_type]

        keys = list(possible)
        random_key = random.choice(keys)
        question = data[random_key]['question']
        ans = data[random_key]['answer']
        choices = data[random_key]['answerChoices']

        try:
            correct_choice = re.search(r'Answer: (.)', ans).group(1)
        except AttributeError:
            correct_choice = None

        data = {
            'domain': data[random_key]["domain"],
            'question': question,
            'answer': ans
        }

        if choices != '<ul></ul>':
            choice_html = BeautifulSoup(choices)

            data['type'] = 'multiple_choice'
            data['correctChoice'] = correct_choice
            data['correctChoiceIndex'] = ord(correct_choice) - ord('A')
            data['choices'] = [str(choice) for choice in choice_html.select('li')]
        else:
            data['type'] = 'short_answer'

        data_response = jsonify(data)

        data_response.headers.add('Access-Control-Allow-Origin', '*')
        return data_response


if __name__ == '__main__':
    app.run()
