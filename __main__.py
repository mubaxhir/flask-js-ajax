from flask import Flask, render_template,request,jsonify
import pandas as pd

app = Flask(__name__)

bank_list = [{ "salesperson": "EQUIFAX, INC.", "sales": 250 },
    { "salesperson": "TRANSUNION INTERMEDIATE HOLDINGS, INC.", "sales": 315 },
    { "salesperson": "Experian Information Solutions Inc.", "sales": 290 },
    { "salesperson": "BANK OF AMERICA, NATIONAL ASSOCIATION", "sales": 200 },
    { "salesperson": "WELLS FARGO &aml; COMPANY", "sales": 190 },
    { "salesperson": "CITIBANK, N.A.", "sales": 180 },
    { "salesperson": "JPMORGAN CHASE &amp; CO.", "sales": 170 },
    { "salesperson": "Navient Solutions, LLC.", "sales": 160 },
    { "salesperson": "CAPITAL ONE FINANCIAL CORPORATION", "sales": 120 },
    { "salesperson": "U.S. BANCORP", "sales": 80 }]
period_list=['Q1','Q2','Q3','Q4']
files_attached=[]


@app.route('/')
def index():
    return "why"

@app.route('/about')
def about():
    return render_template("example_structure.html",bank_list=bank_list,period_list=period_list)

@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    file_val = request.files['file']
    df = pd.read_csv(file_val)
    data = {str(file_val.filename):
        [{"salesperson":x[0],"sales":x[-1]} for x in df.values]
    }
    files_attached.append(data)
    return {"succes":"saved"}

@app.route('/getajax', methods = ['POST'])
def getfile():
    name = request.form['filename']
    for data in files_attached:
        try:
            if data[name]:
                return {"data":data[name]}
        except:
            continue

if __name__ == "__main__":
    app.run(debug=True,port=5000)
