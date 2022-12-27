#Importing Required Libraries
from flask import Flask, render_template,request,jsonify,url_for
import pickle
import sklearn
import numpy as np
import pandas

app = Flask(__name__)
model = pickle.load(open('reg_model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():    
    Year = int(request.form['Year'])
    Year=2022-Year

    Present_Price=float(request.form['Present_Price'])

    Kms_Driven=int(request.form['Kms_Driven'])

    Owner=int(request.form['Owner'])
    
    Fuel_Type=request.form['Fuel_Type']
    if Fuel_Type=='Petrol':
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif Fuel_Type=='Diesel':
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

    
    Seller_Type=request.form['Seller_Type']
    if Seller_Type=='Individual':
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0

    Transmission=request.form['Transmission']
    if Transmission=='Mannual':
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    if output<0:
        return render_template('index.html',prediction_texts="This Car is not for Sale!!")
    else:
        return render_template('index.html',prediction_text=f"The Predicted Price of this Car is :  {output} lac.")
    

if __name__=="__main__":
    app.run(debug=True)