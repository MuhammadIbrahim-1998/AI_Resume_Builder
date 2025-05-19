from flask import Flask, request, jsonify, render_template
import os
from resume_parser import parse_resume

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = parse_resume(filepath)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

