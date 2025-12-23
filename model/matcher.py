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

def calculate_ats_score(matching_keywords, job_text):
    job_keywords = set(job_text.split())
    matched = set(matching_keywords)

    if not job_keywords:
        return 0

    ats_score = (len(matched) / len(job_keywords)) * 100
    return round(min(ats_score, 100), 2)
from nltk.util import ngrams

def get_ngrams(text, n=2):
    words = text.split()
    return set([" ".join(gram) for gram in ngrams(words, n)])
def phrase_ats_score(resume_text, job_text):
    # Generate phrases
    resume_phrases = set()
    job_phrases = set()

    for n in [2, 3]:  # bigrams + trigrams
        resume_phrases |= get_ngrams(resume_text, n)
        job_phrases |= get_ngrams(job_text, n)

    if not job_phrases:
        return 0, []

    matched_phrases = resume_phrases.intersection(job_phrases)

    score = (len(matched_phrases) / len(job_phrases)) * 100
    score = round(min(score, 100), 2)

    return score, list(matched_phrases)

