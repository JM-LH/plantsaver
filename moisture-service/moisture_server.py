import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_moisture():
    soil_moisture = random.randint(0, 100)
    # return { 'soil_moisture': soil_moisture }
    return { 'tree_id': '1221', 'soil_moisture': soil_moisture }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
