
from flask import Flask, request
from db import Smartphone
app = Flask(__name__)


## view all smartphone
@app.route('/smartphones', methods=['GET'])
def get_all_smartphones():
    son=Smartphone('smartphone_store.db')
    """Returns all smartphones in the database"""
    return son.sql_get_all_smartphones()
# view all smartphones by id
@app.route('/smartphones/id/<id>', methods=['GET'])
def get_product_by_id(id):
    son=Smartphone('smartphone_store.db')
    """Returns smartphones in the database by id"""
    return son.sql_get_product_by_id(int(id))

# view smartphone by name
@app.route('/smartphones/name/<name>', methods=['GET'])
def get_smartphone_by_name(name):
    """Returns a product by name"""
    return 

# view all smartphones names
@app.route('/smartphones/names', methods=['GET'])
def get_smartphone_all_names():
    """Returns all smartphones names"""
    return

# view smartphone by color
@app.route('/smartphones/color/<color>', methods=['GET'])
def get_smartphone_by_color(color):
    """Returns a smartphones by color"""
    return 

# view smartphone by ram
@app.route('/smartphones/ram/<ram>', methods=['GET'])
def get_smartphone_by_ram(ram):
    """Returns a smartphones by ram"""
    return 

# view smartphone by memory
@app.route('/smartphones/memory/<memory>', methods=['GET'])
def get_smartphone_by_memory(memory):
    """Returns a smartphones by memory"""
    return 

# view smartphone by price
@app.route('/smartphones/price/<price>', methods=['GET'])
def get_smartphone_by_price(price):
    """Returns a smartphones if database in price bigger from price"""
    return 

# view add smartphone
@app.route('/smartphone/add', methods=['POST'])
def add_smartphone():
    """Adds a product to the database"""
    return

# view delete smartphone
@app.route('/smartphone/delete/<int:id>', methods=['DELETE'])
def delete_smartphone(id):
    """Deletes a smartphone from the database"""
    return 

if __name__ == '__main__':
    app.run(debug=True)
