from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sentence_transformers import SentenceTransformer, util
import fitz  # PyMuPDF

app = Flask(__name__)
CORS(app)
model = SentenceTransformer('all-MiniLM-L6-v2')


@app.route('/')
def home():
    return render_template('index.html')  # serves templates/index.html


def extract_text_from_pdf(file_stream):
    doc = fitz.open(stream=file_stream.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text


@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form['job_description']

    resume_text = extract_text_from_pdf(resume_file)

    embeddings = model.encode([resume_text, job_description])
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

    return jsonify({
        'match_score': round(similarity * 100, 2)
    })


if __name__ == '__main__':
    app.run(debug=True)
