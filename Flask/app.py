

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
logr = pickle.load(open('visa.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/test')
def test():
    return render_template('va1.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['FULL_TIME_POSITION', 'PREVAILING_WAGE', 'YEAR','SOC_N']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = logr.predict(df)  
    print(output)
    
    if(output == 0):
        output = "CERTIFIED"
        
    elif(output == 1):
        output = "CERTIFIED-WITHDRAWN"
        
    elif(output == 2):
        output = "DENIED"
    
    elif(output == 3):
        output = "WITHDRAWN"    
            
    elif(output == 4):
        output = "PENDING QUALITY AND COMPLIANCE REVIEW - UNASSIGNED"
        
    elif(output == 5):
        output = "REJECTED"
        
    else:
        output = "INVALIDATED"
    prediction_text=output    
    return render_template('va1.html', prediction_text='Applicant is {}'.format(prediction_text))

if __name__ == '__main__':
  
    app.run()









