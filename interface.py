from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import MedicalInsurence
import config
import traceback

app = Flask(__name__)

@app.route('/medical_insurence')
def home1():
    return render_template('index.html')

@app.route('/predict_charges', methods=['GET', 'POST'])
def predict_charges():
    try:
        if request.method == 'GET':
            data = request.args
        elif request.method == 'POST':
            data = request.form
        
        age = int(data.get('age'))
        gender = data.get('gender')
        bmi = int(data.get('bmi'))
        children = int(data.get('children'))
        smoker = data.get('smoker')
        region = data.get('region')

        Obj = MedicalInsurence(age, gender, bmi, children, smoker, region)
        pred_price = Obj.get_predicted_price()
        return render_template('index.html', prediction=pred_price)

    except Exception as e:
        print(traceback.print_exc())
        return redirect(url_for('home1'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)