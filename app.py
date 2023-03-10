from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from preprocess import resized_image, resize
import base64

 
app = Flask(__name__)
 
@app.route('/')



#def hello():
    #return "Hello World"
    
#@app.route('/about')
#def about():
    #return "About Page"

#@app.route('/user/<username>')
#def show_user(username):
    #return f"Welcome {username}"

#@app.route('/number/<int:num>')
#def return_number(num):
    #return f"Number {num}"

##path

##http://127.0.0.1:5000/members?first_name=Ahmed&last_name=Essam
#@app.route('/members')
#def show_user_profile():
    #first_name=request.args.get("first_name")
    #last_name=request.args.get("last_name")
    #return f"first name is {first_name}<br>last name is {last_name}"

#@app.route("/admin")
#def admin():
    #return "Hello Admin"

#@app.route('/users/<name>')
#def hello_user(name):
    #if name=="admin":
        #return redirect(url_for("admin"))
    #else:
        #return redirect(url_for("hello"))
#@app.route('/method', methods=["Get","Post"])
#def method():
    #if request.methods=="Post":
        #return "Post"
    #else:
        #return "Get"


@app.route("/index")
def home():
    
    #image=''
    #image = resized_image(r"static\images\2.jpg")
    return render_template("index.html")
    
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

print(allowed_file)
  
@app.route('/uploader', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename="1.jpg"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')   
        number_of_potholes = resize(r"static\\uploads\\1.jpg")
        number_of_potholes = str(number_of_potholes)
        PIC_FOLDER = os.path.join(r'static', 'uploads')
        app.config['UPLOAD_FOLDER'] = PIC_FOLDER
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '2.jpg')
        return render_template('result.html', filename=filename , img=full_filename, number_of_potholes=number_of_potholes)


@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    #return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.debug = True
    app.run()