from json import load, dump
from os.path import join, exists
from faker import Faker



def readjson(filename:str) -> dict | bool:
    if exists(filename) == True:
        with open(filename, "r") as fp:
            d = load(fp)
        return d
    return False


def writejson(filename:str,data:dict) ->  bool:
    if exists(filename) == True:
        with open(filename, "w") as fp:
            d = dump(data,fp)
        return True
    return False


fk = Faker()
def gerardados():
    dados = list()
    for n in range(1000):
        nome = fk.name()
        cep = fk.postcode()
        tel = fk.phone_number()
        d = dict(nome=nome,cep=cep,tel=tel)
        dados.append(d.copy())
        d.clear()
    return dados



if __name__ == "__main__":
    ROOT_MODEL = "models"
    NAME_FILE = "clientes.json"
    FILE = join(ROOT_MODEL,NAME_FILE)
    dados = dict(map(lambda v: v, enumerate(gerardados())))
    # print(dados.\keys())
    writejson(FILE,dados)