from json import load, dump
from os.path import join, exists





def readjson(filename:str) -> dict | bool:
    if exists(filename) == True:
        with open(filename, "r") as fp:
            d = load(fp)
        return d
    return False



if __name__ == "__main__":
    ROOT_MODEL = "models"
    NAME_FILE = "admin.json"
    FILE = join(ROOT_MODEL,NAME_FILE)
    dados_json = readjson(FILE)
    print(dados_json)