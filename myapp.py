from flask import Flask, request, render_template
from main import questions, display_question, get_answer, calculate_score, provide_feedback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # get user information
        name = request.form['name']
        age = request.form['age']
        education_level = request.form['education_level']
        interests = []
        skills = []

        num_interests = int(request.form['num_interests'])
        num_skills = int(request.form['num_skills'])

        for i in range(num_interests):
            interest = request.form[f'interest_{i+1}']
            interests.append(interest)

        for i in range(num_skills):
            skill = request.form[f'skill_{i+1}']
            skills.append(skill)

        # display questions and record answers
        answers = []
        for question in questions:
            answers.append(request.form[f'answer_{question["question"]}'])

        # calculate score and give answer
        score = calculate_score(answers)
        feedback = provide_feedback(score)

        return render_template('result.html', name=name, age=age, education_level=education_level, interests=interests, skills=skills, feedback=feedback)

    return render_template('index.html', questions=questions, display_question=display_question)

if __name__ == '__main__':
    app.run()
