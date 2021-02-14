from main import create_character, find_character_by_id, find_all_characters, delete_character, update_character


def test_create_character_1():
    filename = "characters.csv"
    name = "Hulk"
    intelligence = 9
    power = 7
    strength = 10
    agility = 8

    created_character = create_character(filename, name, intelligence, power, strength, agility)
    expected = {"id": 1, "name": "Hulk", "intelligence": 9, "power": 7, "strength": 10, "agility": 8}

    assert created_character == expected


def test_find_character():
    filename = "characters.csv"
    character_id = 1

    found_character = find_character_by_id(filename, character_id)
    expected = {"id": 1, "name": "Hulk", "intelligence": 9, "power": 7, "strength": 10, "agility": 8}

    assert found_character == expected


def test_find_all_characters():
    filename = "characters.csv"

    found_character = find_all_characters(filename)
    expected = [{"id": 1, "name": "Hulk", "intelligence": 9, "power": 7, "strength": 10, "agility": 8}]

    assert found_character == expected


def test_update_character():
    filename = "characters.csv"
    character_id = 1
    to_update = {"power": 10, "intelligence": 10}

    updated_character = update_character(filename, character_id, **to_update)
    expected = {"id": 1, "name": "Hulk", "intelligence": 10, "power": 10, "strength": 10, "agility": 8}

    assert updated_character == expected


def test_delete_character():
    filename = "characters.csv"
    character_id = 1

    was_deleted = delete_character(filename, character_id)
    expected = True

    assert was_deleted == expected
