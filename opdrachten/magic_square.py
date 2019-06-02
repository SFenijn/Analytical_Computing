import numpy as np

magicSq1 = [[8,0,0],[0,0,9],[0,0,2]]
magicSq2 = [[5,0,0],[0,0,4],[0,0,6]]

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


def ver_loop(magcsq):
    aMatrix = []
    bArray = []
    # verticaal naar row echolon
    for i in range(0, 3):
        row = []
        totaal = 0
        # loop door de matrix
        for j in range(0, 3):
            for k in range(0, 3):
                if i == k:
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


def digLR_loop(magcsq):
    aMatrix = []
    bArray = []
    # diagonaal LR naar row echolon
    row = []
    totaal = 0
    # loop door de matrix
    for j in range(0, 3):
        for k in range(0, 3):
            if j == k:
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


def digRL_loop(magcsq):
    # diagonaal RL naar row echolon
    aMatrix = []
    bArray = []
    row = []
    totaal = 0
    counter = 2
    # loop door de matrix
    for j in range(0, 3):
        for k in range(0, 3):
            if k == counter:
                totaal += magcsq[j][counter]
                if magcsq[j][counter] == 0:
                    row.append(1)
                else:
                    row.append(0)
            else:
                row.append(0)
        counter -= 1
    row.append(-1)
    aMatrix.append(row)
    bArray.append(0 - totaal)
    info = [aMatrix, bArray]
    return info

def get_matrix_array(magcsq):
    matrix = []
    array = []
    row = [0, 0, 0, 0, 3, 0, 0, 0, 0, -1]
    hor = hor_loop(magcsq)
    ver = ver_loop(magcsq)
    digLR = digLR_loop(magcsq)
    digRL = digRL_loop(magcsq)

    for i in range(0, 3):
        matrix.append(hor[0][i])
        array.append(hor[1][i])
    for i in range(0, 3):
        matrix.append(ver[0][i])
        array.append(ver[1][i])
    matrix.append(digLR[0][0])
    array.append(digLR[1][0])
    matrix.append(digRL[0][0])
    array.append(digRL[1][0])
    matrix.append(row)
    matrix.append(row)
    array.append(0)
    array.append(0)
    infoList = [matrix, array]
    return infoList


infoList = get_matrix_array(magicSq1)

A = infoList[0]
b = infoList[1]
# inverse of A
invA = np.linalg.inv(A)
# som A en b voor x:
x = A * b

print(x)

