from json import load, dump
from os.path import join, exists



def readjson(filename:str) -> dict | bool:
    if exists(filename) == True:
        with open(filename, "r") as fp:
            d = load(fp)
        return d
    return False


def writejson(filename:str,data:dict) ->  bool:
    if exists(filename) == True:
        with open(filename, "a") as fp:
            d = dump(data,fp)
        return True
    return False



if __name__ == "__main__":
    ROOT_MODEL = "models"
    NAME_FILE = "clientes.json"
    FILE = join(ROOT_MODEL,NAME_FILE)
    produtos = [
    ["1", "Agua Mineral", "12", "2021", "12.70"],
    ["1", "Agua Mineral", "12", "2021", "12.70"],
    ]
    for produto in produtos:
        for d in produto:
            print(d)
    