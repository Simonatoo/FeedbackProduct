from flask import Flask, request
import json
import re
from controles.default import Default_data

CON = Default_data()
app = Flask(__name__)



@app.route(rule='/product/comments', methods=['GET'])
def comments():
    product = request.args.get('product')
    
    if product:
        try:
            product = str(product) 
        except ValueError:
            return json.dumps({"error": "apenas números são aceitos como argumento para limite"}), 400
    
    return json.dumps(CON.search_product(re.sub('\s','-',product).lower()))


if __name__ == '__main__':
    app.run(port=8080,debug=True)