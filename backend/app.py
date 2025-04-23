import os
from flask import Flask, render_template, request
import eng_to_ipa as ipa
from flask_cors import CORS

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../frontend'),
    static_folder=os.path.join(os.path.dirname(__file__), '../frontend/static')
)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = ipa.convert(text, stress_marks='both')
    return render_template('index.html', result=result)

if __name__ == "__main__":
    print("Starting Flask app on http://localhost:5000")
    app.run(debug=True)