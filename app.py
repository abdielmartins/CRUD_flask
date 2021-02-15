from flask import Flask, jsonify, request, make_response
from main import delete_character, find_all_characters, find_character_by_id, update_character, create_character

app = Flask(__name__)

FILENAME = "characters.csv"


@app.route("/", methods=["GET"])
def all_characters():
    found_characters = find_all_characters(FILENAME)

    if found_characters:
        response = make_response(jsonify({"message": "Characters found", "data": found_characters}), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    elif found_characters == []:
        response = make_response(jsonify([]), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(jsonify({"message": "Unknown error"}), 500)
        response.headers["Content-Type"] = "application/json"
        return response


@app.route("/character", methods=["GET"])
def character_by_id():
    request_data = request.get_json()

    character_id = None

    if request_data:
        if "character_id" in request_data:
            character_id = request_data["character_id"]

    if character_id == None:
        response = make_response(
            jsonify({"message": "Missing 'character_id' parameter"}),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    found_character = find_character_by_id(FILENAME, character_id)

    if found_character:
        response = make_response(jsonify({"message": "Character found", "data": found_character}), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(jsonify({"message": "Unknown error"}), 500)
        response.headers["Content-Type"] = "application/json"
        return response


@app.route("/character", methods=["POST"])
def create_new_character():
    request_data = request.get_json()

    name = None
    intelligence = 0
    power = 0
    strength = 0
    agility = 0

    if request_data:
        if "name" in request_data:
            name = request_data["name"]
        if "intelligence" in request_data:
            intelligence = request_data["intelligence"]
        if "power" in request_data:
            power = request_data["power"]
        if "strength" in request_data:
            strength = request_data["strength"]
        if "agility" in request_data:
            agility = request_data["agility"]

    if name == None:
        response = make_response(
            jsonify({"message": "Missing 'name' parameter"}),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    created_character = create_character(FILENAME, name, intelligence, power, strength, agility)

    if create_character:
        response = make_response(jsonify({"message": "Character created", "data": created_character}), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(jsonify({"message": "Unknown error"}), 500)
        response.headers["Content-Type"] = "application/json"
        return response


@app.route("/update", methods=["PATCH"])
def update_character_by_id():
    request_data = request.get_json()

    character_id = None
    to_update = {}

    if request_data:
        if "character_id" in request_data:
            character_id = request_data["character_id"]
        if "intelligence" in request_data:
            to_update["intelligence"] = request_data["intelligence"]
        if "power" in request_data:
            to_update["power"] = request_data["power"]
        if "strength" in request_data:
            to_update["strength"] = request_data["strength"]
        if "agility" in request_data:
            to_update["agility"] = request_data["agility"]

    if character_id == None:
        response = make_response(
            jsonify({"message": "Missing 'character_id' parameter"}),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    updated_character = update_character(FILENAME, character_id, **to_update)

    if updated_character:
        response = make_response(jsonify({"message": "Character updated", "data": updated_character}), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(jsonify({"message": "Unknown error"}), 500)
        response.headers["Content-Type"] = "application/json"
        return response


@app.route("/delete", methods=["DELETE"])
def delete_character_by_id():
    request_data = request.get_json()

    character_id = None

    if request_data:
        if "character_id" in request_data:
            character_id = request_data["character_id"]

    if character_id == None:
        response = make_response(
            jsonify({"message": "Missing 'character_id' parameter"}),
            400,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    deleted_character = delete_character(FILENAME, character_id)

    if deleted_character:
        response = make_response(jsonify({"message": "Character deleted", "data": deleted_character}), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(jsonify({"message": "Unknown error"}), 500)
        response.headers["Content-Type"] = "application/json"
        return response