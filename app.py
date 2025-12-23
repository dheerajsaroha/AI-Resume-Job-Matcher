from flask import Flask,request, jsonify,render_template
import os

from utils.preprocess import clean_text, extract_text_from_pdf
from model.matcher import calculate_match
# from flask import render_template


app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route("/")
def home():
    return "AI Resume Job Matcher is running!"

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/match",methods=["POST"])
def match_job_resume():
    if "resume" not in request.files or "job_description" not in request.form:
        return jsonify({"error":"Resume file and job description are required"}),400
    resume_file = request.files["resume"]
    job_description = request.form["job_description"]

    resume_path = os.path.join(UPLOAD_FOLDER,resume_file.filename)
    resume_file.save(resume_path) # Save the file

    resume_text = extract_text_from_pdf(resume_path)
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)

    score, keywords = calculate_match(resume_clean,job_clean)
    return jsonify({
        "match_score":score,
        "matching_keywords":keywords
    })

if __name__ == "__main__":
    app.run(debug=True)
