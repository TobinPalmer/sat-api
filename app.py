import re

from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/math/', methods=['GET'])
def hello_world():
    # get the request params
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

        if choices != '<ul></ul>':
            # return f'{data[random_key]["domain"]} {question} \n {choices} \n {ans}'
            data = {
                'type': 'multiple_choice',
                'domain': data[random_key]["domain"],
                'question': question,
                'choices': choices,
                # Correct Choice is right after "Answer :"
                'correctChoice': correct_choice,
                'answer': ans
            }
            return data
        else:
            data = {
                'type': 'short_answer',
                'domain': data[random_key]["domain"],
                'question': question,
                'answer': ans
            }
            return data

if __name__ == '__main__':
    app.run()
