from flask import Flask,render_template,request


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import numpy as np







app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Name=request.form['Name']
        Age = int(request.form['Age'])
        Gender = int(request.form['Gender'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Direct_Bilirubin = float(request.form['Total_Bilirubin'])
        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        data = pd.read_csv("C:\\Users\\dell\\Downloads\\indian_liver_patient2.csv")
        data["Gender"] = data["Gender"].map({"Male": 1, "Female": 2})
        data["Dataset"] = data["Dataset"].map({1: 0, 2: 1})
        X = data.drop(columns="Dataset")
        Y = data["Dataset"]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=38)
        p3 = RandomForestClassifier()
        p3.fit(X_train, Y_train)

        input_data = (Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio)
        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction = p3.predict(input_data_reshaped)
        senddata=""
        if (prediction[0]== 1):
            senddata='According to the given details person does not have Liver Disease'
        elif (prediction[0]== 0):
            senddata='According to the given details chances of having Liver Disease are High, So Please Consult a Doctor'
        return render_template('result.html',resultvalue=senddata,name=Name,age=Age,sex=Gender,pred=prediction)
        

if __name__ == "__main__":
    app.run(debug=True)