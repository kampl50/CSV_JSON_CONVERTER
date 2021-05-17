import errno
import os

from flask import Flask
from flask import request
from flask.helpers import send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv', 'xml'}
app = Flask(__name__)
CORS(app)

uploads_dir = os.path.join(app.instance_path, 'uploads_files')

try:
    os.makedirs(uploads_dir)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/parse', methods=['POST'])
def upload_file():
    print(request.files)
    if 'file' not in request.files:
        print('no file in request')
    receivedFile = request.files['file']
    if receivedFile.filename == '':
        print('no selected file')
    if receivedFile and allowed_file(receivedFile.filename):
        receivedFile. \
            save(os.path.join(uploads_dir, secure_filename(receivedFile.filename)))
        return "file was saved correctly"
    print("end")

@app.route('/download')
def download_file():
	path = "converted\example.txt"

	return send_file(path, as_attachment=True)  


if __name__ == '__main__':
    app.run()
