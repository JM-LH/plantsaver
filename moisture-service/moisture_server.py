import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_moisture():
    moisture_per_centage = random.randint(0, 100)
    return { 'moisture_per_centage': moisture_per_centage }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
