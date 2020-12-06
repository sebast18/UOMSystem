import xml.etree.ElementTree as ET

tree = ET.parse('poscUnits22.xml')
root = tree.getroot()

def listDimensionClasses(dimensionSet):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            dimension = UOM.find('DimensionalClass')
            if dimension is not None:
                dimension = dimension.text
                dimensionSet.add(dimension)
    return dimensionSet


def listQuantityTypes(quantitySet):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            quantity = UOM.find('QuantityType')
            if quantity is not None:
                quantity = quantity.text
                quantitySet.add(quantity)
    return quantitySet

def createDimDict(dimDict):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            dimension = UOM.find('DimensionalClass')
            name = UOM.find('Name')
            if dimension is not None:
                dimension = dimension.text
                name = name.text
                dimDict[name] = dimension
    return dimDict

def createQuanDict(quanDict):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            quantity = UOM.find('QuantityType')
            name = UOM.find('Name')
            if quantity is not None:
                quantity = quantity.text
                name = name.text
                quanDict[name] = quantity
    return quanDict

def printUOMDim(dimDict, givenDim):
    tempSet = set()
    for x in dimDict:
        val = dimDict[x]
        if givenDim == val:
            tempSet.add(x)
    if len(tempSet) == 0:
        return('Could not find any values for the given dimensional class')
    else:
        return tempSet

def printUOMQuantity(quanDict, givenQuan):
    tempSet = set()
    for x in quanDict:
        val = quanDict[x]
        if givenQuan == val:
            tempSet.add(x)
    if len(tempSet) == 0:
        return('Could not find any values for the given quantity type')
    else:
        return tempSet



def createConvNum(numDict):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            name = UOM.find('Name')
            for CTBU in UOM.findall('ConversionToBaseUnit'):
                for fraction in CTBU.findall('Fraction'):
                    num = fraction.find('Numerator')
                    if num is not None:
                        num = num.text
                        name = name.text
                        numDict[name] = num
    return numDict

def createConvDenom(denomDict):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            name = UOM.find('Name')
            for CTBU in UOM.findall('ConversionToBaseUnit'):
                for fraction in CTBU.findall('Fraction'):
                    denom = fraction.find('Denominator')
                    if denom is not None:
                        denom = denom.text
                        name = name.text
                        denomDict[name] = denom
    return denomDict

def createConvFactor(factorDict):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            name = UOM.find('Name')
            for CTBU in UOM.findall('ConversionToBaseUnit'):
                factor = CTBU.find('Factor')
                attri = str(CTBU.attrib)
                if factor is not None:
                    factor = factor.text
                    if(attri.find('1/') != -1):
                        factor = float(factor)
                        factor = 1/factor
                    name = name.text
                    factorDict[name] = factor
    return factorDict


def createAnnotDict(annotDict):
    for doc in root.iter('UnitsDefinition'):
        for UOM in doc.findall('UnitOfMeasure'):
            name = UOM.find('Name')
            annot = UOM.get('annotation')
            if annot is not None:
                annot = str(annot)
                name = name.text
                annotDict[name] = annot
    return annotDict

def printUOMAnnot(annotDict, givenAnnot):
    val = annotDict.get(givenAnnot)
    return val

