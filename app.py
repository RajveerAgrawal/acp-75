from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        date1_str = request.form['date1']
        date2_str = request.form['date2']
        
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        
        difference = abs((date2 - date1).days)
        
        return f"The difference between the two dates is {difference} days."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(port=5000, debug=True)