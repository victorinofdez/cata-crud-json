import json

DATA_FILE = "../data/data.json"

def read_file():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def write_file(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def create(game_id, name, year):
    data = read_file()

    if str(game_id) in data["games"]:
        print("El juego ya existe")
        return

    data["games"][str(game_id)] = {
        "id": game_id,
        "name": name,
        "year": year
    }

    write_file(data)
    print("Juego creado")

def get(game_id):
    data = read_file()
    return data["games"].get(str(game_id), "Juego no encontrado")

def update(game_id, name=None, year=None):
    data = read_file()
    game = data["games"].get(str(game_id))

    if not game:
        print("Juego no encontrado")
        return

    if name:
        game["name"] = name
    if year:
        game["year"] = year

    write_file(data)
    print("Juego actualizado")

def delete(game_id):
    data = read_file()

    if str(game_id) not in data["games"]:
        print("Juego no encontrado")
        return

    del data["games"][str(game_id)]
    write_file(data)
    print("Juego eliminado")

def get_all_games():
    data = read_file()
    return data["games"]


def main():
    create(1, "Resident evil 4", "2004")

    re4 = get(1)
    print(re4)

    create(2, "Metal Gear Solid 3", "2004")
    mgs3 = get(2)
    print(mgs3)

    #delete(1)
    mgs3 = get(1)
    print(mgs3)

if __name__ == "__main__":
    main()
