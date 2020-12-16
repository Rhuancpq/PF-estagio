def getKeys(lista):
    res = set()
    for x in lista:
        if "nome" in x:
            res.add(x.get("nome"))
    return list(res)
