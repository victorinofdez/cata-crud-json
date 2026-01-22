import json

DATA_FILE = "persistencia/data.json"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_file(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def create(path, section, key, value):
    data = read_file(path)

    if section not in data:
        data[section] = {}

    if str(key) in data[section]:
        print("Ya existe")
        return

    data[section][str(key)] = value
    write_file(path, data)


def get(path, section, key):
    data = read_file(path)
    return data.get(section, {}).get(str(key), None)


def update(path, section, key, value):
    data = read_file(path)

    if str(key) not in data.get(section, {}):
        print("No existe")
        return

    data[section][str(key)] = value
    write_file(path, data)


def delete(path, section, key):
    data = read_file(path)

    if str(key) not in data.get(section, {}):
        print("No existe")
        return

    del data[section][str(key)]
    write_file(path, data)


def get_all(path, section):
    data = read_file(path)
    return data.get(section, {})


def main():
    hola = get(DATA_FILE, "games", 1)
    create(
        DATA_FILE,
        "games",
        3,
        {"id": 3, "name": "Mario", "year": 1985}
    )
    mario = get(DATA_FILE, "games", 3)
    print(mario)
if __name__ == "__main__":
    main()
