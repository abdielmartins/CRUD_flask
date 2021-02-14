from typing import Union
import json, csv, os.path

FIELDNAMES_DEFAULT = ["id", "name", "intelligence", "power", "strength", "agility"]

# def id_generator():
#     num = 0
#     while True:
#         yield num
#         num += 1


def id_generator(filename):
    current_id = 1
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for _ in csv_reader:
            current_id += 1
        return current_id


def fieldnames_generate(filename: str):
    with open(filename, "w") as csv_file:
        csv_write_header = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        csv_write_header.writerow(FIELDNAMES_DEFAULT)


def fieldnames_validate(filename: str) -> bool:
    if not os.path.isfile(filename) or not os.path.getsize(filename):
        return False

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", lineterminator="\n")
        list_fieldnames = (row for index, row in enumerate(csv_reader) if index == 0)
        if not (next(list_fieldnames)) == FIELDNAMES_DEFAULT:
            return False
        return True


def create_character(
    filename: str, name: str, intelligence: int = 0, power: int = 0, strength: int = 0, agility: int = 0
) -> dict:

    FIELDNAMES_DEFAULT = ["id", "name", "intelligence", "power", "strength", "agility"]
    character_id = id_generator(filename)

    if not fieldnames_validate(filename):
        fieldnames_generate(filename)

    new_character = {
        "id": character_id,
        "name": name,
        "intelligence": intelligence,
        "power": power,
        "strength": strength,
        "agility": agility,
    }

    with open(filename, "a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES_DEFAULT)
        csv_writer.writerow(new_character)

    return new_character


def find_character_by_id(filename: str, character_id: int) -> Union[dict, None]:
    with open(filename) as csv_file:
        character = None
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if int(row["id"]) == character_id:
                character = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "intelligence": int(row["intelligence"]),
                    "power": int(row["power"]),
                    "strength": int(row["strength"]),
                    "agility": int(row["agility"]),
                }
        return character


def find_all_characters(filename: str) -> list:
    with open(filename) as csv_file:
        characters = []
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            characters.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "intelligence": int(row["intelligence"]),
                    "power": int(row["power"]),
                    "strength": int(row["strength"]),
                    "agility": int(row["agility"]),
                }
            )
        return characters


def delete_character(filename: str, character_id: int) -> bool:
    has_character = False
    characters = []

    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if int(row["id"]) != character_id:
                characters.append(row)
            if int(row["id"]) == character_id:
                has_character = True

    if has_character:
        with open(filename, "w") as csv_file:
            csv_write_header = csv.writer(csv_file, delimiter=",", lineterminator="\n")
            csv_write_header.writerow(FIELDNAMES_DEFAULT)
            csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES_DEFAULT)
            for character in characters:
                csv_writer.writerow(character)

    return has_character


def update_character(filename: str, character_id: int, **kwargs: dict) -> Union[dict, None]:
    character = find_character_by_id(filename, character_id)

    if not character:
        return None

    for key in character:
        if key in kwargs:
            character[key] = kwargs[key]

    delete_character(filename, character_id)

    with open(filename, "a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES_DEFAULT)
        csv_writer.writerow(character)

    return find_character_by_id(filename, character_id)