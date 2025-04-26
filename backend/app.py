import os
from flask import Flask, request, jsonify, render_template
import eng_to_ipa as ipa
from flask_cors import CORS

# Define the absolute paths to the frontend folder
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))

app = Flask(
    __name__,
    template_folder=frontend_path,
    static_folder=os.path.join(frontend_path, 'static')
)

CORS(app)

@app.route('/')
def home():
    # Optional: remove this if you're only using this app as an API backend
    return render_template('index.html')

@app.route('/api/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        text = data.get('text', '')
        print("Received request with text:", text)

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        result = ipa.convert(text, stress_marks='both')
        return jsonify({'result': result})

    except Exception as e:
        print("Error occurred:", e)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    print("Starting Flask app on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
