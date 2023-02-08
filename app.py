import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import time




app = Flask(__name__)



@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/convert", methods=["POST", "GET"])
def convert():
    if request.method == "POST":
        file = request.files["image"]
        format = request.form.get("format")
        outputimage, x = file.filename.split('.')
        outputimage = outputimage + "." + format
        print(format.lower())
        with Image.open(file) as image:
            image.convert('RGB').save( outputimage)
            path = 'static/images/' + outputimage 
            os.rename(outputimage, path )
            filepath = 'images/' + outputimage
            image_url = url_for('static', filename=filepath)
        return render_template("convert.html", image_url=image_url)
    return redirect("/")
    
    

if __name__ == '__main__':
    app.run(debug=True)