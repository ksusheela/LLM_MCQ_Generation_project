from flask import Flask
from src.mcq_generation.log import logging

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    logging.info("We are testing our logging module")
    
    return "This is MCQ_Generator_Peoject"

if __name__ == '__main__':
    app.run(debug=True)  #5000  localhost:5000
