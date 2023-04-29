from flask import Flask, request, render_template
from main import questions, display_question, get_answer, calculate_score, provide_feedback

app = Flask(__name__)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # record answers
        answers = []
        for question in questions:
            answers.append(request.form[f'answer_{question["id"]}'])

        # calculate score and give answer
        score = calculate_score(answers)
        feedback = provide_feedback(score)

        return render_template('feedback.html', feedback=feedback)

    return render_template('questions.html', questions=questions, display_question=display_question)

if __name__ == '__main__':
    app.run()
