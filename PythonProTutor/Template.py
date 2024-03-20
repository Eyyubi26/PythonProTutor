from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "What is your name?", "answer": "username"},
    {"question": "Where is the capital of Turkey?", "answer": "ankara"},
    {"question": "Who is the founder of Turkey?", "answer": "atatürk"},
    {"question": "How many cities does Turkey have?", "answer": "81"}
]

def calculate_score(answers):
    score = 0
    for question, answer in zip(questions, answers):
        if answer is not None and question["answer"].lower() == answer.lower():
            score += 25
    return score

highest_score = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global highest_score

    if request.method == 'POST':
        answers = [request.form.get('username'),
                   request.form.get('answer1'),
                   request.form.get('answer2'),
                   request.form.get('answer3')]
        score = calculate_score(answers)
        if score > highest_score:
            highest_score = score
        return render_template('result.html', score=score, highest_score=highest_score)
    return render_template('index.html', questions=questions, highest_score=highest_score)

if __name__ == '__main__':
    app.run(debug=True)
