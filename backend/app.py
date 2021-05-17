from flask.helpers import send_file
from Json2CsvTest import AlgorithmJson2CsvTest
import errno
import os

from flask import Flask
from flask import request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import Response
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

    print(receivedFile.filename)
    receivedFile. \
            save(os.path.join(uploads_dir, secure_filename(receivedFile.filename)))
    
    
    splicedFileName = receivedFile.filename.split(".")[0]

    test=AlgorithmJson2CsvTest()
    test.testJson2Csv('instance/uploads_files/' + receivedFile.filename,'instance/converted_files/' + splicedFileName + '.csv','|')
    return Response(splicedFileName + '.csv')

@app.route('/download')
def download_file():
	path = "instance/converted_files/" + request.args.get('filename')
	return send_file(path, as_attachment=True)  


if __name__ == '__main__':
    app.run()
