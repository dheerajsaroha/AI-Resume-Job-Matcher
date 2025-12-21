from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text,job_text):
    """Calclates the similarity score b/w resume and job description"""
    documents = [resume_text,job_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])[0][0]
    score_percentage = round(similarity_score * 100, 2)

    feature_names = vectorizer.get_feature_names_out()
    resume_vector = tfidf_matrix[0].toarray()[0]
    job_vector = tfidf_matrix[1].toarray()[0]

    matching_keywords = [
        feature_names[i]
        for i in range(len(feature_names))
        if resume_vector[i] > 0 and job_vector[i] > 0
    ]

    return score_percentage, matching_keywords