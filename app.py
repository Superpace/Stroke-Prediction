# Importing essential libraries
from flask import Flask, render_template, request, redirect, url_for, flash,session
import pickle
import numpy as np
import joblib
import pandas as pd
from PIL import Image

filename = 'Models/xgb_best.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        location = request.form.get('location')
        work_type = request.form.get('work_type')
        married = request.form.get('married')
        hypertension = request.form.get('hypertension')
        heart = request.form.get('heart')
        cigaratte = request.form.get('cigaratte')
        avg_glucose = request.form['avg_glucose']

        bmi = (weight/height**2)*10000 # 10000 ile çarpmamız paydanın metreye dönüşmesidir

        datapoint = pd.DataFrame({"gender": [gender],
                                  "age": [age],
                                  "hypertension":[hypertension], 
                                  "heart_disease":[heart],
                                  "ever_married":[married],
                                  "Residence_type":[location],
                                  "avg_glucose_level":[avg_glucose],
                                  "bmi":[bmi],
                                  "smoking_status":[cigaratte],
                                  "work_type_Govt_job":[("work_type_Govt_job" == work_type)],
                                  "work_type_Never_worked":[("work_type_Never_worked" == work_type)],
                                  "work_type_Private":[("work_type_Private" == work_type)],
                                  "work_type_Self-employed":[("work_type_Self-employed" == work_type)],
                                  "work_type_children":[("work_type_Self-employed" == work_type)],
                                  })

        predictions = classifier.predict_proba(datapoint)[0]
        for i in range(len(predictions)):
            print(i," = %",int(predictions[i]*100))

        session["stroke"] = int(predictions[1]*100)

        return redirect('/showResult')
    else:
        return render_template('index.html')

@app.route('/showResult', methods=['GET','POST'])
def showResult():

    percantage = session['stroke']

    text = ""

    if percantage<20:
        text= "Durumunuz iyi gözüküyor fakat yine de sağlıklı yaşama devam edip tedbiri elden bırakmamanızda fayda var !"
    
    elif percantage<40:
        text= "Durumunuz kötü olmasa da dikkatli olmalısınız !"
    
    else:
        text= "Doktorunuzla birlikte bir taramadan geçmeniz, durumunuz hakkında detaylı bilgi almanız çok çok önemli !"

    return render_template('showResult.html',percantage=percantage,text=text)

if __name__ == '__main__':
    app.run(debug=True)