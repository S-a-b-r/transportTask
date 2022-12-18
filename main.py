from pprint import pprint

def PrintMatrix(matrix):
    for i in range(len(matrix)):
        print("------" * len(matrix[i]))
        for j in range(len(matrix[i])):
            if(matrix[i][j] == None):
                print("| None", end="")
            else:
                print("|{0:5.0f}".format(int(matrix[i][j])), end="")
        print()
    print()
    print()

def inputProductionQuantity():
    print("Введите кол-во продукции на каждом производстве через пробел")
    prod = input().split(" ")
    for i in range(len(prod)):
        prod[i] = int(prod[i])
    return prod

def inputNeededQuantity():
    print("Введите кол-во продукции необходимое в пункте потребления")
    need = input().split(" ")
    for i in range(len(need)):
        need[i] = int(need[i])
    return need

def breakProg(message):
    print(message)
    return

def inputCoef(row, column):
    matrix = [[]]
    for i in range(len(row)):
        for j in range(len(column)):
            print("Введите коэффициент для "+ str(i) + "ой строки и "+ str(j)+ "ого столбца")
            matrix[i].append(int(input()))
        matrix.append([])
    matrix.pop()#Вырезаем последнюю строку(лишнюю)
    return matrix

def unionMatrixWithProdAndNeed(matrix, prod, need):
    for i in range(len(matrix)):
        matrix[i].append(prod[i])
    matrix.append(need)
    return matrix

def findMinCoefInMatrix(matrix):
    min = 10000
    minI = 0
    minJ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] < min 
            and needFlags[j] 
            and prodFlags[i]):
                min = matrix[i][j]
                minI = i
                minJ = j
    return [minI, minJ]

def findMinCoefInLine(matrix, line):
    min = 10000
    minJ = 0
    for j in range(len(matrix[line])):
        if(matrix[line][j] < min and needFlags[j]):
            min = matrix[line][j]
            minJ = j
    return [line, minJ]

def findMinCoefInColumn(matrix, column):
    min = 10000
    minI = 0
    for i in range(len(matrix)):
        if(matrix[i][column] < min and prodFlags[i]):
            min = matrix[i][column]
            minI = i
    return [minI, column]        

def getZeroMatrix(quantString, quantCol):
    matrix = []
    for i in range(quantString):
        matrix.append([])
        for j in range(quantCol):
            matrix[i].append(0)
    return matrix

def summInLine(matrix, line):
    summ = 0
    for i in range(len(matrix[line])):
        summ += matrix[line][i]
    return summ

def summInColumn(matrix, column):
    summ = 0
    for i in range(len(matrix)):
        summ += matrix[i][column]
    return summ

def findPotencialsInLine(line):
    for i in range(len(matrixCoefs[line])):
        if(matrixDeliv[line][i] != 0 and verticalPotencials[line] != None):
            horizontalPotencials[i] = matrixCoefs[line][i] - verticalPotencials[line]

def findPotencialsInColumn(column):
    for i in range(len(matrixCoefs)):
        if(matrixDeliv[i][column] != 0 and verticalPotencials[column] != None):
            verticalPotencials[i] = matrixCoefs[i][column] - horizontalPotencials[column]

def findInArray(array, el):
    try:
        return array.index(el)
    except ValueError:
        return -1

def findContur(matrix, elemI, elemJ):
    matrix = matrix.copy()
    for i in range(len(matrix)):
        matrix[i] = matrix[i].copy()
    matrix[elemI][elemJ] = 1
    for n in range(len(matrix[0]) + len(matrix)):
        for i in range(len(matrix)):
            countInLine = 0

            for j in range(len(matrix[i])):
                if(matrix[i][j] != 0 and matrix[i][j] != None):
                    countInLine +=1

            if(countInLine <= 1):
                for j in range(len(matrix[i])):
                    matrix[i][j] = None

        countInColumns = []
        for j in range(len(matrix[0])):
            countInColumns.append(0)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] != 0 and matrix[i][j] != None):
                    countInColumns[j] += 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(countInColumns[j] <=1):
                    matrix[i][j] = None
    return matrix          

def checkDelivLine(line):
    quantNoZero = 0
    for j in range(len(matrixDeliv[line])):
        if(matrixDeliv[line][j] != 0):
            quantNoZero += 1
    return quantNoZero

def checkDelivColumn(column):
    quantNoZero = 0
    for i in range(len(matrixDeliv)):
        if(matrixDeliv[i][column] != 0):
            quantNoZero += 1
    return quantNoZero

def findNextElemInLine(matrix, elemI, elemJ):
    for j in range(len(matrix[elemI])):
        if(matrix[elemI][j] != None and matrix[elemI][j] != 0 and j != elemJ):
            return [elemI, j]

def findNextElemInColumn(matrix, elemI, elemJ):
    for i in range(len(matrix)):
        if(matrix[i][elemJ] != None and matrix[i][elemJ] != 0 and elemI != i):
            return [i, elemJ]

def countNoZeroAndNoneInMatrix(matrix):
    count = 0  
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] != 0 and matrix[i][j] != None):
                count += 1
    return count

def setMinusesInContur(matrix, elemI, elemJ):
    matrix = matrix.copy()
    for i in range(len(matrix)):
        matrix[i] = matrix[i].copy()
    nextElem = [elemI, elemJ]
    min = -1000
    minI = elemI
    minJ = elemJ
    quantNoZero = countNoZeroAndNoneInMatrix(matrix)
    stepen = 1
    for i in range(quantNoZero//2):
        nextElem = findNextElemInLine(matrix, nextElem[0], nextElem[1])
        matrix[nextElem[0]][nextElem[1]] = matrix[nextElem[0]][nextElem[1]] * (-1) ** (stepen)
        if(abs(matrix[nextElem[0]][nextElem[1]]) < abs(min) and matrix[nextElem[0]][nextElem[1]] < 0):
            min = matrix[nextElem[0]][nextElem[1]]
            minI = nextElem[0]
            minJ = nextElem[1]
        stepen += 1

        nextElem = findNextElemInColumn(matrix, nextElem[0], nextElem[1])
        matrix[nextElem[0]][nextElem[1]] = matrix[nextElem[0]][nextElem[1]] * (-1) ** (stepen)
        stepen += 1

    for i in range(quantNoZero//2):
        nextElem = findNextElemInLine(matrix, nextElem[0], nextElem[1])
        matrix[nextElem[0]][nextElem[1]] = abs(matrix[nextElem[0]][nextElem[1]]) - ((-1) ** (stepen)) * min
        stepen +=1

        nextElem = findNextElemInColumn(matrix, nextElem[0], nextElem[1])
        matrix[nextElem[0]][nextElem[1]] = abs(matrix[nextElem[0]][nextElem[1]]) - ((-1) ** (stepen)) * min
        stepen += 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == None):
                matrix[i][j] = matrixDeliv[i][j]

    return matrix

def countSum():
    sum = 0
    for i in range(len(matrixDeliv)):
        for j in range(len(matrixDeliv[i])):
            sum += matrixDeliv[i][j] * matrixCoefs[i][j]
    return sum
# prod = inputProductionQuantity()
# prod = [85, 112, 72, 120]
# prod = [90, 70, 50]
prod = [15,15,15,15]
prodSumm = 0
prodFlags = []
for i in range(len(prod)):
    prodSumm += prod[i]
    prodFlags.append(True)

# need = inputNeededQuantity()
# need = [75, 125, 64, 65, 60]
# need = [80, 60, 40, 30]
need = [11,11,11,11,16]
needSumm = 0
needFlags = []
for i in range(len(need)):
    needSumm += need[i]
    needFlags.append(True)

if(needSumm != prodSumm):
    breakProg("Задача не сбалансирована, пожалуйста, приведите ее к сбалансированному виду(Добавьте столбец/строку)")

# matrixCoefs = inputCoef(prod, need)
# matrixCoefs = [[7,1,4,5,2],
# [13,4,7,6,3],
# [3,8,0,18,12],
# [9,5,3,4,7]
# ]
# matrixCoefs = [[2,1,3,2],
# [2,3,3,1],
# [3,3,2,1]
# ]
matrixCoefs = [[17,20,29,26,25],
[3,4,5,15,24],
[19,2,22,4,13],
[20,27,1,17,19]]

matrixDeliv = getZeroMatrix(len(prod), len(need))

minCoef = findMinCoefInMatrix(matrixCoefs)
matrixDeliv[minCoef[0]][minCoef[1]] = min(prod[minCoef[0]] , need[minCoef[1]])

for i in range(len(need) + len(prod) - 2):
    if(summInLine(matrixDeliv, minCoef[0]) == prod[minCoef[0]]):
        prodFlags[minCoef[0]] = False

    if(summInColumn(matrixDeliv, minCoef[1]) == need[minCoef[1]]):
        needFlags[minCoef[1]] = False

    if(summInColumn(matrixDeliv, minCoef[1]) < need[minCoef[1]] and needFlags[minCoef[1]]):
        minCoef = findMinCoefInColumn(matrixCoefs, minCoef[1])
    elif(summInLine(matrixDeliv, minCoef[0]) < prod[minCoef[0]] and prodFlags[minCoef[0]]):
        minCoef = findMinCoefInLine(matrixCoefs, minCoef[0])
    else:
        minCoef = findMinCoefInMatrix(matrixCoefs)

    matrixDeliv[minCoef[0]][minCoef[1]] = min(
        prod[minCoef[0]] - summInLine(matrixDeliv, minCoef[0]), 
        need[minCoef[1]] - summInColumn(matrixDeliv, minCoef[1])
    )

horizontalPotencials = []
for i in range(len(need)):
    horizontalPotencials.append(None)

verticalPotencials = [0]
for i in range(len(prod)-1):
    verticalPotencials.append(None)

min = -1
while(min < 0):
    for i in range(len(horizontalPotencials)):
        horizontalPotencials[i] = None
    for i in range(len(verticalPotencials)):
        verticalPotencials[i] = None
    verticalPotencials[0] = 0
    
    findPotencialsInLine(0)
    countIteration = 0
    while(findInArray(verticalPotencials, None) != -1 or findInArray(horizontalPotencials, None) != -1):
        
        if(countIteration > 10):
            horizontalPotencials[0] = 0
        if(countIteration > 20):
            horizontalPotencials[1] = 0
        if(countIteration > 30):
            verticalPotencials[1] = 0
        for i in range(len(verticalPotencials)):
            if(verticalPotencials[i] != None):
                for j in range(len(matrixCoefs[i])):
                    if(matrixDeliv[i][j] != 0 and horizontalPotencials[j] == None):
                        horizontalPotencials[j] = matrixCoefs[i][j] - verticalPotencials[i]

        for j in range(len(horizontalPotencials)):
            if(horizontalPotencials[j] != None):
                for i in range(len(matrixCoefs)):
                    if(matrixDeliv[i][j] != 0 and verticalPotencials[i] == None):
                        verticalPotencials[i] = matrixCoefs[i][j] - horizontalPotencials[j]
        countIteration+=1

    matrixDelta = getZeroMatrix(len(prod), len(need))
    
    min = 0
    minI = 0
    minJ = 0
    for i in range(len(matrixDelta)):
        for j in range(len(matrixDelta[i])):
            matrixDelta[i][j] = matrixCoefs[i][j] - verticalPotencials[i] - horizontalPotencials[j]
            if(matrixDelta[i][j] < min):
                minI = i
                minJ = j
                min = matrixDelta[i][j]
    if(min < 0):
        contur = findContur(matrixDeliv, minI, minJ)
        matrixDeliv = setMinusesInContur(contur, minI, minJ)
        matrixDeliv[minI][minJ] -= 1
    else:
        pprint("Минимальная стоимость: " + str(countSum()))
        PrintMatrix(unionMatrixWithProdAndNeed(matrixDeliv, prod, need))

