import qrcode
import os
from flask import Flask
from flask import send_file,send_from_directory,request
app = Flask(__name__)


@app.route('/getqr',methods=["POST"])
def getqr():
    #os.remove("text.png")
    inputtext=request.form['url']
    qr= qrcode.make(inputtext)
    
    qr.save('text.png')
    #filename='text.png'
    return send_from_directory('.',
                               'text.png', mimetype='image/png')

@app.route('/getqr_rest')
def getqr_rest(text):
    inputtext=text
    qr= qrcode.make(inputtext)
    
    qr.save('text.png')
    #filename='text.png'
    return send_from_directory('.',
                               'text.png', mimetype='image/png')



if __name__ == '__main__':
    app.run()

