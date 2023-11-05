from flask import Flask, request, jsonify
from ShirtService import ShirtService
import json

class ShirtController:
    _shirtService = None
    app = Flask(__name__)
    def __init__(self, service: ShirtService) -> None:
        global _shirtService
        _shirtService = service

    @app.route('/shirts', methods=['GET'])
    async def GetShirts():
        result = await _shirtService.GetShirts()

        if result.Success:
            return json.dumps([obj.__dict__ for obj in result.Data]), 200
        else:
            return jsonify({"message":result.Message}), 404


    @app.route('/shirts', methods=['POST'])
    async def CreateShirf():
        new_shirt = request.get_json()
        color = new_shirt['Color']
        if not isinstance(color,str):
            return jsonify({'res': 'failure', "message": "Invalid type for color of shirt"}),422
        design = new_shirt['Design']
        if not isinstance(design,str):
            return jsonify({'res': 'failure', "message": "Invalid type for design of shirt"}),422
        
        result = await _shirtService.AddShirt(color,design)
        if result.Success:
            return jsonify({"message": "Shirt created successfully"}), 201
        else:
            return jsonify({"message":result.Message}), 404
    

    @app.route('/shirts/<int:shirt_id>', methods=['PUT'])
    async def update_shirt(shirt_id):
        result = await _shirtService.ChangeShirt(shirt_id)
        if result.Success:
            return jsonify({"message": "Shirt updated successfully"}), 201
        else:
            return jsonify({"message":result.Message}), 404

    @app.route('/shirts/<int:shirt_id>', methods=['DELETE'])
    async def delete_shirt(shirt_id):
        result = await _shirtService.DeleteShirt(shirt_id)
        if result.Success:
            return jsonify({"message": "Shirt deleted successfully"}), 201
        else:
            return jsonify({"message":result.Message}), 404

    def run(self) :
        self.app.run()
