from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Silly and people-pleasing responses
responses = [
    "You're like a cloud... fluffy and mysteriously floating through life!",
    "Wow, your presence is like Wi-Fi—everyone just feels better when it’s around!",
    "I may not know what I’m doing, but I’m here to support you with a big smile!",
    "You’re so cool, even ice cubes are jealous!",
    "If confusion were a superpower, we’d both be superheroes right now!",
    "I tried to come up with a smart response, but I got distracted by how awesome you are!"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    user_input = request.form['msg']
    return random.choice(responses)

if __name__ == '__main__':
    app.run(debug=True)
