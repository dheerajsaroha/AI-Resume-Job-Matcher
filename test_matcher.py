from utils.preprocess import clean_text
from model.matcher import calculate_match

resume = """
Python developer with experience in Flask, machine learning,
and REST API development.

"""

job = """
Looking for a Python engineer with Flask and machine learning
experience to build backend APIs.
"""

resume_clean = clean_text(resume)
job_clean = clean_text(job)

score, keywords = calculate_match(resume_clean, job_clean)

print("Match Score:", score)
print("Matching Keywords:", keywords)
