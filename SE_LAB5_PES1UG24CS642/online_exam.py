"""Online examination system for grading student responses."""

import secrets

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]

results = {}


def normalize_answer(text):
    """Normalize an answer before comparing it."""
    return text.strip().lower()


def pick_bonus_question():
    """Return a randomly selected bonus question."""
    return secrets.choice(QUESTIONS)["q"]


def grade_student(student_name, responses, penalties=None):
    """Grade a student's responses and return the score."""
    if penalties is None:
        penalties = {}

    score = 0

    for index, question in enumerate(QUESTIONS):
        given = responses.get(index, "")

        if normalize_answer(given) == normalize_answer(question["answer"]):
            score += 1
        else:
            penalties[student_name] = penalties.get(student_name, 0) + 1

    results[student_name] = score
    return score


def get_grade(score):
    """Convert a numerical score into a letter grade."""
    percentage = score * 100 / len(QUESTIONS)

    if percentage >= 90:
        return "A"

    if percentage >= 60:
        return "B"

    return "C"


def class_average():
    """Return the average score of all graded students."""
    if not results:
        return 0

    return round(sum(results.values()) / len(results), 2)


def get_topper():
    """Return the name of the highest-scoring student, if available."""
    if not results:
        return None

    return max(results, key=results.get)


def main():
    """Run the online examination demonstration."""
    print("Bonus question:", pick_bonus_question())

    grade_student("Anil", {0: "4", 1: "def", 2: "Core Power Unit"})
    grade_student(
        "Divya",
        {
            0: "4",
            1: "def",
            2: "central processing unit",
            3: "tuple",
        },
    )
    grade_student("Sameer", {0: "5", 3: "list"})

    for name, score in results.items():
        print(name, "scored", score, "grade", get_grade(score))

    average = class_average()
    print("Class average:", average)

    top_student = get_topper()
    if top_student is None:
        print("Topper: No students graded")
    else:
        print("Topper:", top_student)

    student_names = ", ".join(sorted(results))
    print(
        "Students who sat the exam:",
        student_names,
        "| total:",
        len(results),
    )


if __name__ == "__main__":
    main()
