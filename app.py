from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_view.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template(
        'prediction.html',
        prediction=None
    )

if __name__ == '__main__':
    app.run(debug=True)
    
