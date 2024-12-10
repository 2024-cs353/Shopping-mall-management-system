from flask import Flask, request, jsonify
from flask_cors import CORS
from AI_Process import get_ai_response
from AI_Key import keyword_detection

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求


@app.route('/get_response', methods=['POST'])
def get_response():
    """
    Handle POST requests to the /get_response endpoint.
    This function receives user input, checks for specific keywords,
    and returns either a predefined response or an AI-generated response.
    """
    data = request.get_json()
    user_input = data.get('user_input')
    print(f"Received user input: {user_input}")

    # Keyword detection
    response = keyword_detection(user_input)
    if response is None:
        print("No keyword detected, getting AI response.")
        response = get_ai_response(user_input)
    else:
        print(f"Keyword detected, returning response: {response}")

    print(f"Response to be sent: {response}")
    return jsonify({'response': response})


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
    print("Flask server started.")
