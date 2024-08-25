from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user_info', methods=['POST'])
def post_user_info():
    data = request.json.get('data', [])
    
    # Separating numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Finding the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets, default=None)
    
    # Preparing the response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    
    return jsonify(response)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
