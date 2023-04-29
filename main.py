# define the questions (questions gathered from sourcing many career tests across the internet)
questions = [{
    'id': 1,
    "question": "What are your favorite subjects in school?",
    "options": ["Math", "Science", "English", "Social Studies"]
}, {
    'id': 2,
    "question":
    "Which of these activities do you enjoy most?",
    "options":
    ["Playing sports", "Playing music", "Reading", "Watching movies"]
}, {
    'id': 3,
    "question":
    "What skills do you possess?",
    "options": ["Leadership", "Problem-solving", "Creativity", "Organization"]
}, {
    'id': 4,
    "question":
    "What type of work environment do you prefer?",
    "options": [
        "Fast-paced and competitive", "Quiet and structured",
        "Collaborative and creative", "Independent and flexible"
    ]
}, {
    'id': 5,
    "question":
    "What motivates you in your work?",
    "options": [
        "Money and financial rewards", "Personal satisfaction and achievement",
        "Helping others and making a difference",
        "Opportunities for growth and advancement"
    ]
}, {
    'id': 6,
    "question":
    "How do you handle stress and pressure?",
    "options": [
        "I thrive under pressure and deadlines",
        "I prefer to work at a steady pace without too much stress",
        "I like to take breaks and practice relaxation techniques",
        "I prefer to avoid stressful situations altogether"
    ]
}, {
    'id': 7,
    "question":
    "What are your long-term career goals?",
    "options": [
        "I want to become a manager or executive in my field",
        "I want to start my own business or organization",
        "I want to make a positive impact on society or the environment",
        "I want to continuously learn and develop new skills"
    ]
}, {
    'id': 8,
    "question":
    "How do you adapt to change?",
    "options": [
        "I enjoy new challenges and opportunities for growth",
        "I prefer stability and routine in my work",
        "I can handle change as long as it's not too sudden or disruptive",
        "I find change difficult and stressful"
    ]
}]


# define the UI
def display_question(question):
    print(question["question"])  # print question
    for i, option in enumerate(
            question["options"]
    ):  # for each question, print each option, looked up enumerate function
        print(f"{i+1}. {option}")  # print options for the question


def get_answer(question):
    answer = input("Enter the number of your answer: ")
    # if the input isn't a number or outside 1-4, prompt to retype
    while not answer.isnumeric() or int(answer) < 1 or int(answer) > len(
            question["options"]):
        answer = input("Invalid answer. Please try again: ")
    # retrieve the selected option
    return question["options"][int(answer) - 1]


# define the scoring system
def calculate_score(answers):
    score = 0
    for answer in answers:
        if answer in [
                "Math", "Science", "Problem-solving", "Leadership",
                "Fast-paced and competitive", "Money and financial rewards",
                "I thrive under pressure and deadlines",
                "I want to become a manager or executive in my field",
                "I enjoy new challenges and opportunities for growth"
        ]:
            score += 1
        elif answer in [
                "English", "Social Studies", "Creativity", "Organization",
                "Quiet and structured",
                "Personal satisfaction and achievement",
                "I prefer to work at a steady pace without too much stress",
                "I want to make a positive impact on society or the environment",
                "I prefer stability and routine in my work"
        ]:
            score += 0.5
        else:
            score += 0
    return score


# define the feedback
# check this scoring system again
def provide_feedback(score):
    if score >= 4:
        print(
            "You might be interested in pursuing a career as a: Engineer, Lawyer, Surgeon, Investment Banker, Management Consultant, Sales Manager, Entrepreneur, or Software Developer."
        )
    elif score >= 3:
        print(
            "You might be interested in pursuing a career as a: Writer, Journalist, Teacher, Social Worker, Nonprofit Manager, Accountant, HR Manager, Librarian, Archivist, or Museum Curator."
        )
    elif score >= 2:
        print(
            "You might be interested in pursuing a career as a: Graphic Designer, Event Planner, Travel Agent, Social Media Manager, Voice actor, or Public speaker."
        )
    else:
        print(
            "You might be interested in pursuing a career as a: Writer, Musician, Artist, Fitness Trainer, Personal Chef, Life Coach or Stand-up comedian "
        )

