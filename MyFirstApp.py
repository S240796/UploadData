from flask import Flask, render_template, request
import os,dftodb

UploadData = Flask(__name__)

# Specify the folder where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
UploadData.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@UploadData.route('/')
def index():
    return render_template('upload.html')

@UploadData.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the file to the specified folder
        file.save(os.path.join(UploadData.config['UPLOAD_FOLDER'], file.filename))
        dftodb.CreateTable(os.path.join(UploadData.config['UPLOAD_FOLDER'], file.filename),file.filename[:-5])
        return 'File uploaded successfully'

if __name__ == '__main__':
    UploadData.run(debug=True)
