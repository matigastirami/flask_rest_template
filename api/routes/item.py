from api import app
from api.services.item import (
    search_items_service, 
    create_item_service, 
    get_item_service, 
    update_item_service,
    delete_item_service
)
from flask import jsonify, request

@app.route('/items', methods=['GET'])
def search_items():
    items = search_items_service()
    return jsonify(items)

@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    item = get_item_service(id)
    print(item)
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    body = request.get_json()
    create_item_service(body['name'], body['description'])
    return "Successfully created"

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    body = request.get_json()
    update_item_service(id, body['name'], body['description'])
    return "Successfully updated"

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    delete_item_service(id)
    return "Successfully deleted"