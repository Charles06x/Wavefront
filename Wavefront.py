list = [[" ", " ", " ", " ", " "], [" ", " ", "-1", "-1", " "], [" ", " ", " ", "-1", " "], [" ", " ", " ", "-1", " "]]; obstacles = ["(2,1)", "(3,1)", "(3,2)", "(3,3)"]
def extractCoordinates(s):
    s = s[1:4]
    s = s.split(",")
    s[0] = int(s[0]);    s[1] = int(s[1])
    return s

def askForCoordinates():
    x = True
    while x == True:
        pass
        c = input("Coordinate: ")
        if c not in obstacles:
            x = False
    c = extractCoordinates(c)
    return c

def perseption(c, l):
    coords = []
    value = []
    if type(c) is str:
        c = extractCoordinates(c)
    x = c[0];    y = c[1]
    if l[c[1]][c[0]] == "I":
        print("Inicio.")
        return([], [])
    else:
        if (x >= 0 and x <= 4 and y >= 0 and y <= 3): #Verify its neighbors.
            if x+1 <= 4:
                if l[y][x+1] != " ":
                    s = "(" + str(x+1) + "," + str(y) + ")"
                    coords.append(s)
                    value.append("NA")
                else:
                    s = "(" + str(x+1) + "," + str(y) + ")"
                    coords.append(s)
                    value.append("A")
            if x - 1 >= 0:
                if l[y][x-1] != " ":
                    s = "(" + str(x-1) + "," + str(y) + ")"
                    coords.append(s)
                    value.append("NA")
                else:
                    s = "(" + str(x-1) + "," + str(y) + ")"
                    coords.append(s)
                    value.append("A")
            if y + 1 <= 3:
                if l[y+1][x] != " ":
                    s = "(" + str(x) + "," + str(y+1) + ")"
                    coords.append(s)
                    value.append("NA")
                else:
                    s = "(" + str(x) + "," + str(y+1) + ")"
                    coords.append(s)
                    value.append("A")
            if y - 1 >= 0:
                 if l[y-1][x] != " ":
                     s = "(" + str(x) + "," + str(y-1) + ")"
                     coords.append(s)
                     value.append("NA")
                 else:
                     s = "(" + str(x) + "," + str(y-1) + ")"
                     coords.append(s)
                     value.append("A")
        currentValue = l[c[1]][c[0]]
        return coords, value, currentValue

def move(l, pi):
    x = pi[0]; y = pi[1]
    val = []
    coords = []
    if (x >= 0 and x <= 4 and y >= 0 and y <= 3): #Verify its neighbors.
        if x+1 <= 4:
            if l[y][x+1] != " " and type(l[y][x+1]) is int :
                s = "(" + str(x+1) + "," + str(y) + ")"
                coords.append(s)
                val.append(l[y][x+1])
        if x - 1 >= 0:
            if l[y][x-1] != " " and type(l[y][x-1]) is int:
                s = "(" + str(x-1) + "," + str(y) + ")"
                coords.append(s)
                val.append(l[y][x-1])
        if y + 1 <= 3:
            if l[y+1][x] != " " and type(l[y+1][x]) is int:
                s = "(" + str(x) + "," + str(y+1) + ")"
                coords.append(s)
                val.append(l[y+1][x])
        if y - 1 >= 0:
             if l[y-1][x] != " " and type(l[y-1][x]) is int:
                 s = "(" + str(x) + "," + str(y-1) + ")"
                 coords.append(s)
                 val.append(l[y-1][x])
    ind = val.index(min(val))

    nCoodinate = extractCoordinates(coords[ind])
    l[y][x] = "*"
    v = 0
    if min(val) == 1:
        v = 1
    return nCoodinate, v, l

def next(coordinatesInfo, coordinates,  l, currentValue):
    nc = []
    for i in range(0,len(coordinatesInfo)):
        aux = extractCoordinates(coordinates[i])
        x = aux[0]; y = aux[1]
        if coordinatesInfo[i] == "A":
            l[y][x] = int(cv) + 1
            nc.append(coordinates[i])
    return nc, l
print("\nInsert initial coordinates. Please make sure to insert a coordinate between (0,0) and (4,3).\nAditional info: if you insert a coordinates that results being an obstacle, you'll be asked for anoher one.")
ci = askForCoordinates()
print("\nInsert final coordinates. Please make sure to insert a coordinate between (0,0) and (4,3).\nPlease consider the additinal info given above.\n")
cf = askForCoordinates()
nc = []; nl = []
if ci == cf:
    print("Starting point is the same destination point.")
else:
    list[ci[1]][ci[0]] = "I";    list[cf[1]][cf[0]] = 1
    print("\n#################################\n#################################\nThe matrix before being traveled.\n#################################\n#################################\n\n")
    for i in list:
        print(i)
    nc.append(cf)
    op = True
    while op:
        for i in nc:
            nco, values, cv = perseption(i, list)
            nc, nl = next(values, nco, list, cv)
            if not nc:
                op = False
    print("\n#################################\n#################################\n\tThe best route.\n#################################\n#################################\n\n")
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == " ":
                list[i][j] = 0
    for i in nl:
        print("\t".join(str(val) for val in i))

    op = True; pi = ci
    while op:
        pi, v, nl = move(list, pi)
        if v == 1:
            op = False
    print("\n#################################\n#################################\n\tRoute taken.\n#################################\n#################################\n\n")
    for i in nl:
        print("\t".join(str(val) for val in i))
