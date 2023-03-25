from flask import *
from werkzeug.utils import secure_filename
from flask import Flask, redirect, url_for, render_template, request, flash
import os
from process import *
import cv2 
import numpy as np
from PIL import Image
app = Flask(__name__,template_folder='C:/Users/bouzi/cartoon/templates')
print(app)
print(__name__)
upload_folder = os.path.join('C:/Users/bouzi/cartoon/static/','store/')
print(upload_folder)
app.config['UPLOAD'] = upload_folder
@app.route('/',methods = ['GET', 'POST'])
def upload_file(): 
    app.config['UPLOAD'] = upload_folder
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            #flash('No selected file')
            return redirect("/")
        filename= secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOAD'],filename))
         #print(file)
        img=os.path.join(app.config['UPLOAD'],filename)
        print(img)
        # cartoonize image picture using Canny filter
        a=combine(smothing(cartoonize(readoriginalfun(img),16)),LUT_Inverse(cannyfun(graytocolor(readoriginalfun(img)))),filename)
        print(a)
        #cartoonize image picture using adaptative filter 
        l=adaptative(img,8,filename)
        print(l)
        title="Original picture"
        return render_template('index.html',img="static/store/"+filename,img1=a,img2=l,title=title)
        #return redirect(url_for('static', filename='/store/' +filename), code=301)        
    return render_template("index.html")

#for downald this application is 
""""
@app.route('/store',methods = ['GET', 'POST'])
def download_file():
    return send_from_directory(app.config['UPLOAD'],
                               'cat.jpg', as_attachment=True)
"""
if __name__ == '__main__':
   app.run(debug=True)

   