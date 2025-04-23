from flask import Flask, render_template, request
import eng_to_ipa as ipa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = ipa.convert(text, stress_marks='both')
    return render_template('index.html', result=result)