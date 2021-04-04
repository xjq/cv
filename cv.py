from flask import Flask
from flask import render_template
import json


app = Flask(__name__)
#f = open('cv.json')
#cv_text = f.readlines()
#print cv_text
#cv_dict = json.loads(cv_text)
#f.close()

#print cv_dict


@app.route('/')
def cv():

    return render_template('cv.html')

if __name__ == "__main__":
    
    app.debug = True
    app.run( host='0.0.0.0', port=80)