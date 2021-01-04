from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/predict' , methods=['POST'])
def predict():
    a = request.form.get('exp')
    b = request.form.get('test_Score')
    c = request.form.get('interview_score')

    print(a , b, c)

    return 'Form is submitted successfully'


    

app.run(debug=True)