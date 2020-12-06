def calculateConversion(amount, UOM1, UOM2, denomDict, factorDict):
    number1 = denomDict.get(UOM1)
    number2 = denomDict.get(UOM2)
    firstFactor = False
    secondFactor = False
    if(number1 == None):
        number1 = factorDict.get(UOM1)
        firstFactor = True
    if(number2 == None):
        number2 = factorDict.get(UOM2)
        secondFactor = True
    if(number1 == None):
        number1 = 1
        firstFactor = True
    if(number2 == None):
        number2 = 1
        secondFactor = True
    number1 = float(number1)
    number2 = float(number2)
    if (firstFactor & secondFactor):
        number3 = amount * number1/number2
    elif(firstFactor):
        number3 = number1/number2*amount
    elif(secondFactor):
        number3 = number1/number2*amount
    else:
        number3 = amount*number1/number2
    return number3