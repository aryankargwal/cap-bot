import os
from csv import writer
from numpy.lib.type_check import imag
import pandas as pd
from flask import Flask, flash, request
from pyngrok import ngrok
from tokener import *
# from flask import redirect, url_for 
from werkzeug.utils import secure_filename 
import secrets
import sys 
from datetime import datetime 
sys.path.insert(0, './models/vgg')
try:
    from vgg import *
except ImportError:
    print('Import not possible')
# from db import db_init, db, Image
 
IMAGE_FOLDER = 'images'
DATABASE_FOLDER = 'databases'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
SECRET = secrets.token_urlsafe(32)
 
url = ngrok.connect(5000)
print(' * Tunnel URL:', url)

app = Flask(__name__) 
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER 
app.config['DATABASE_FOLDER'] = DATABASE_FOLDER
app.config['CSV_FILE'] = ''
app.secret_key = SECRET

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

def update_csv(img_path):
    caption = test(img_path)
    caption = tlk(caption)
    row_no = pd.read_csv(os.path.join(app.config['DATABASE_FOLDER'],app.config['CSV_FILE'])).shape[0]+1
    print(row_no)
    row_contents = [row_no]
    if (len(caption) >=16):
        row_contents = [row_no,caption[0],caption[1], caption[2], caption[3], caption[4], caption[5], caption[6], caption[7], caption[8], caption[9], datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Camera 1', img_path]
    else:
        for i in range(len(caption)):
            row_contents.append(caption[i])
        
        for j in range(16-len(caption)):
            row_contents.append('')
        row_contents.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))    
        row_contents.append('Camera 1')
        row_contents.append(img_path)

    with open(os.path.join(app.config['DATABASE_FOLDER'],app.config['CSV_FILE']), 'a+', newline='') as csvfile:
        #creating a csv writer object
        csvwriter = writer(csvfile)
        #writing  the data rows
        csvwriter.writerow(row_contents)
    return row_contents

@app.route('/session', methods=['POST'])
def db_init():
    if request.method == 'POST' and app.config['CSV_FILE']=='':
        app.config['CSV_FILE'] = request.args['csv_file']
        with open(os.path.join(app.config['DATABASE_FOLDER'],app.config['CSV_FILE']), 'w') as csvfile:
            # creating a csv writer objject
            csvwriter = writer(csvfile)
            #writing the fields
            csvwriter.writerow(['id','w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'w11', 'w12', 'w13', 'w14', 'w15', 'w16', 'time', 'camera', 'image_path'])

        # df.to_csv(os.path.join(app.config['DATABASE_FOLDER'],app.config['CSV_FILE']), index=False)

        return app.config['CSV_FILE']+" created", 201
    else:
        return "Session already started", 409
        
 
@app.route('/upload', methods=['POST']) 
def upload_file(): 
    if request.method == 'POST': 
        # check if the post request has the file part 
        if 'file' not in request.files: 
            flash('No file part') 
            return 'No file part', 400 
        file = request.files['file'] 
        # if user does not select file, browser also 
        # submit an empty part without filename 
        if file.filename == '': 
            flash('No selected file') 
            return 'No selected file', 404 
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename) 
            flash('file {} saved'.format(file.filename)) 
            img_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
            file.save(img_path)
            cpt = update_csv(img_path)
            return str(cpt), 200

@app.route('/search', methods=['POST'])
def img_search():
    fd = None
    if request.method == 'POST':
        if app.config['CSV_FILE'] !='':
            # keyword = request.args['keyword']
            keywords = ['beard', 'man']
            df = pd.read_csv(os.path.join(app.config['DATABASE_FOLDER'],'trial.csv'))
            
            for i in df.index:
                res = checkInFirst(df.iloc[i], keywords)
                if res == True:
                    fd = df.loc[i:i, ['time', 'camera']]
                    fd = fd.to_string()
                    print(fd)
                    print(type(fd))
                    break
                # return fd, 200
    return str(fd), 201


 
if __name__ == '__main__': 
	app.run()
    
