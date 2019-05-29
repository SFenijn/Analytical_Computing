import numpy as np

magicSq1 = [[8,0,0],[0,0,9],[0,0,2]]

print(magicSq1)


def hor_loop(magcsq):
    aMatrix = []
    bArray = []
    # horizontaal naar row echolon
    for i in range(0, 3):
        row = []
        totaal = 0
        # loop door de matrix
        for j in range(0, 3):
            for k in range(0, 3):
                if i == j:
                    totaal += magcsq[j][k]
                    if magcsq[j][k] == 0:
                        row.append(1)
                    else:
                        row.append(0)
                else:
                    row.append(0)
        row.append(-1)
        aMatrix.append(row)
        bArray.append(0 - totaal)
    info = [aMatrix, bArray]
    return info


def eclon_loop(magcsq, i):
    row = []
    totaal = 0
    # loop door de matrix
    for j in range(0, 3):
        for k in range(0, 3):
            if i == j:
                totaal += magcsq[j][k]
                if magcsq[j][k] == 0:
                    row.append(1)
                else:
                    row.append(0)
            else:
                row.append(0)
    row.append(-1)
    infolist = [row, 0 - totaal]
    return infolist


def sqToRowchelon(magcsq):
    aMatrix = []
    bArray = []
    # horizontaal naar row echolon
    for i in range(0, 3):
        rowAndArry = eclon_loop(magcsq, i)

        aMatrix.append(rowAndArry[0])
        bArray.append(rowAndArry[1])
        info = [aMatrix, bArray]
    return info


print(hor_loop(magicSq1)[0])
print(hor_loop(magicSq1)[1])
