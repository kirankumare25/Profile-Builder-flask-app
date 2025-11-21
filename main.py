import os
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route('/image', methods=['POST'])
def image():
    name = request.form.get('profile_name')
    fact = request.form.get('facts')
    facts = fact.split(',')

    font = request.form.get("font_opt")
    color = request.form.get("favcolor")

    if 'files' in request.files:
        file_name = request.files['files']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name.filename)
        file_name.save(file_path)
        
        return render_template('profile.html', in_image=file_name.filename, name=name , facts=facts, font=font, color=color)

    
if __name__ == '__main__':
    app.run()
