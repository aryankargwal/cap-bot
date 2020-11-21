import os
from csv import writer
from numpy.lib.type_check import imag
import pandas as pd
from flask import Flask, flash, request, redirect, url_for 
from werkzeug.utils import secure_filename 
import secrets
import sys 
from datetime import datetime 
sys.path.insert(0, './models/attention')
try:
    from attention import *
except ImportError:
    print('Import not possible')
# from db import db_init, db, Image
 
IMAGE_FOLDER = 'images'
DATABASE_FOLDER = 'databases'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
SECRET = secrets.token_urlsafe(32)
 
app = Flask(__name__) 
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER 
app.config['DATABASE_FOLDER'] = DATABASE_FOLDER
app.config['CSV_FILE'] = ''
app.secret_key = SECRET

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

def update_csv(img_path):
    caption = caption_image_beam_search(img_path, 5)
    row_no = pd.read_csv(os.path.join(app.config['DATABASE_FOLDER'],app.config['CSV_FILE'])).shape[0]+1
    print(row_no)
    row_contents = [row_no]
    if (len(caption) >=10):
        row_contents = [row_no,caption[0],caption[1], caption[2], caption[3], caption[4], caption[5], caption[6], caption[7], caption[8], caption[9], datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Camera 1', img_path]
    else:
        for i in range(len(caption)):
            row_contents.append(caption[i])
        
        for j in range(10-len(caption)):
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
            csvwriter.writerow(['id','w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10','time', 'camera', 'image_path'])

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

@app.route('/caption/<int:img_id>', methods=['GET'])
def caption(img_id):
    if request.method == 'GET':
        if app.config['CSV_FILE'] !='':
            df = pd.read_csv(app.config['CSV_FILE'])
            df.loc[img_id, 'caption']

 
if __name__ == '__main__': 
	app.run()