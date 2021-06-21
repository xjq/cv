# -*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
import json
import io


app = Flask(__name__)


@app.route('/')
def cv():
    code = 'en'
    f = io.open('cvs/' + code + '.json', 'r', encoding='utf-8')
    cv_text = f.read()
    cv_dict = json.loads(cv_text)
    f.close()

    basic = cv_dict['basic']
    skillset = cv_dict['skillset']
    certs = cv_dict['certs']
    education= cv_dict['education']
    career = cv_dict['career']
    portfolio = cv_dict['portfolio']

    return render_template( code + '.html', \
                            basic=basic, \
                            skillset=skillset, \
                            certs=certs, \
                            education=education, \
                            career=career, \
                            portfolio=portfolio)
                            

if __name__ == "__main__":
    
    app.debug = True
    app.run( host='0.0.0.0', port=80)