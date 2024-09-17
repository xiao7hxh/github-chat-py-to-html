from flask import Flask, request, jsonify, render_template
from chat import get_gpt_response  # 从 chat.py 中导入 get_gpt_response 函数

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    response = get_gpt_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
