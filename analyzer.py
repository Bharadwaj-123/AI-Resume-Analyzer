skills_database = [

    "python",
    "sql",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "git",
    "github",
    "docker",
    "aws",
    "linux",
    "flask",
    "django",
    "streamlit",
    "tensorflow",
    "pytorch",
    "numpy",
    "pandas",
    "excel",
    "power bi",
    "communication",
    "problem solving"
]


def analyze_resume(text):

    found = []

    missing = []

    for skill in skills_database:

        if skill in text:

            found.append(skill.title())

        else:

            missing.append(skill.title())

    score = min(100, len(found) * 5)

    ats = min(100, score + 10)

    return {

        "score": score,
        "ats": ats,
        "found": found,
        "missing": missing

    }