def readCSV(name):
    f = open(name+".csv", "rt")
    res = list()
    line = f.readline() # jogando a primeira linha fora
    while True:
        line = f.readline()
        
        if not line:
            break

        line = line.replace(';', '\n')
        dic = line.splitlines()
        dic = {"id": int(dic[0]),
                "nome": dic[1],
                "telefone": int(dic[2]),
                "idade": int(dic[3])}
        res.append(dic)
    return sorted(res, key=lambda k: k["nome"])

