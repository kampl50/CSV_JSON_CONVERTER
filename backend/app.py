from flask.helpers import send_file
from AlgorithmJson import AlgorithmJson
from AlgorithmCsv import AlgorithmCsv
from AlgorithmXML import AlgorithmXML
import errno
import os
import shutil
from flask import Flask
from flask import request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import Response
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv', 'xml'}
app = Flask(__name__)
CORS(app)

uploads_dir = os.path.join(app.instance_path, 'uploads_files')
converted_dir = os.path.join(app.instance_path, 'converted_files')
try:
    os.makedirs(uploads_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

try:
    os.makedirs(converted_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/parse', methods=['POST'])
def upload_file():
    # shutil.rmtree('instance/uploads_files/')
    # shutil.rmtree('instance/converted_files/')
    
    # os.makedirs(uploads_dir)
    # os.makedirs(converted_dir)
  
    
    if 'file' not in request.files:
         print('no file in request')
    receivedFile = request.files['file']
    if receivedFile.filename == '':
        print('no selected file')

    receivedFile. \
            save(os.path.join(uploads_dir, secure_filename(receivedFile.filename)))
    splicedFileName = receivedFile.filename.split(".")[0]

    if request.args.get('from') == 'CSV' and request.args.get('to') == 'JSON':
        test = AlgorithmCsv()
        test.convertCSV2JSON('instance/uploads_files/' + receivedFile.filename,'instance/converted_files/' + splicedFileName + '.' + request.args.get('to').lower(),request.args.get('separator'))
    if request.args.get('from') == 'CSV' and request.args.get('to') == 'XML':
        test = AlgorithmCsv()
        test.convertCSV2XML('instance/uploads_files/' + receivedFile.filename,'instance/converted_files/' + splicedFileName + '.' + request.args.get('to').lower(),request.args.get('separator'))
    if request.args.get('from') == 'JSON' and request.args.get('to') == 'CSV':
        test=AlgorithmJson()
        test.convertJSON2CSV('instance/uploads_files/' + receivedFile.filename,'instance/converted_files/' + splicedFileName + '.' + request.args.get('to').lower(),'|')
    if request.args.get('from') == 'XML' and request.args.get('to') == 'CSV':
        test = AlgorithmXML()
        test.convertXML2CSV('instance/uploads_files/' + receivedFile.filename,'instance/converted_files/' + splicedFileName + '.' + request.args.get('to').lower(),request.args.get('separator'))

    return Response(splicedFileName + '.' + request.args.get('to').lower())

@app.route('/download')
def download_file():
	path = "instance/converted_files/" + request.args.get('filename')
	return send_file(path, as_attachment=True)  


if __name__ == '__main__':
    app.run()
