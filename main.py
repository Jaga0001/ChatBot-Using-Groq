from flask import Flask, request, jsonify
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()  # Use get_json() instead of json
    message = data.get("message")
    if message:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            model="llama3-8b-8192"
        )
        return jsonify({"response": chat_completion.choices[0].message.content})
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Add host='0.0.0.0' to allow external access