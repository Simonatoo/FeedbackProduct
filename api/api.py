from flask import Flask, request
import json
from control.default import Default_data

CON = Default_data()
app = Flask(__name__)

@app.route(rule='/product/comments', methods=['GET'])
def comments():
    return json.dumps(CON.mercado_livre()),200

if __name__ == '__main__':
    app.run(port=8080,debug=True)
