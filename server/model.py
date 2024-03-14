from json import load, dump


with open("models/user.json","r") as fp:
    dados = load(fp)
    for idd in dados:
        for v in dados[idd].values():
            print(v)