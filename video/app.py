from flask import Flask, render_template, request
import os 
from deeplearning import video_anpr
# webserver gateway interface
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text_list = video_anpr(path_save)
        
        print(text_list)

        return render_template('index.html',upload=True,text=text_list,no=len(text_list))

    return render_template('index.html',upload=False)


if __name__ =="__main__":
    app.run(debug=True)