import requests
from flask import Flask, render_template, request, redirect, url_for, session, render_template_string
import hashlib
# from flask_mysqldb import MySQLpip
#import mysql.connector
import re
import sys
import json
from datetime import date
from datetime import datetime

#from flask_bootstrap import Bootstrap


app = Flask(__name__, static_url_path="")
#(app)
#app.secret_key = 'cs4400fall2021'


@app.route('/', methods=['POST', 'GET'])
def generate():
    #urls=None
    res=None
    urls1=None
    urls2=None
    
 
    if request.method == 'POST' :
        #res=None
       # cursor = db_connection.cursor(buffered=True)
        prompt = request.form['prompt']
        #password = request.form['password']
        #select_statement = "SELECT * FROM Accounts WHERE Email = %s AND Pass = %s "
        #cursor.execute(select_statement, (email, password))
        #result = cursor.fetchall()
        print(prompt)
        headers = {
         # Already added when you pass json=
         # 'Content-Type': 'application/json',
        'Authorization': 'Bearer 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',
           }

        json_data2 = {
            'prompt': prompt,
            'n': 2,
            'size': '1024x1024',
        }

        response2 = requests.post('https://api.openai.com/v1/images/generations', headers=headers, json=json_data2)
                #print(result)
        print("Response is ", response2)
        response2 = response2.json()
        res = True 
        urls1= response2["data"][0]["url"]
        urls2= response2["data"][1]["url"]
                
    return render_template('input.html',response=res, urls1=urls1, urls2=urls2)

if __name__ == '__main__':
    app.run(debug=True)