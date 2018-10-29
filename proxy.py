def OpenProxy(file1):
    prx = {}
    with open(file1, "r") as file:
        for line in file:
            key, value = line.split()
            prx[key] = value
        return prx



