import flask
from flask import jsonify
from UOMSystem.Calculations import *
from UOMSystem.InitLists import *

dimSet = set()
quanSet = set()
numDict = {}
denomDict = {}
dimDict = {}
quanDict = {}
factorDict = {}
annotDict = {}

if __name__ == '__main__':
    listDimensionClasses(dimSet)
    listQuantityTypes(quanSet)
    createConvDenom(denomDict)
    createConvNum(numDict)
    createConvFactor(factorDict)
    createDimDict(dimDict)
    createQuanDict(quanDict)
    createAnnotDict(annotDict)

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True


    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Engineering units oppgave</h1>" \
               "<p>Add '/listdimensionclasses/' to the URL to list all dimension classes. <br/>" \
               "Add '/listquantitytypes/' to the URL to list all quantity types. <br/> " \
               "Add '/givendimension/dimension class/' to the URL to list UOM's of a given dimension class. <br/> " \
               "Add '/givenquantityType/quantity type/' to the URL to list all UOM's of a given quantity type. <br/> " \
               "Add '/convertuom/amount/uom1/uom2/' to the URL to calculate the amount of UOM2 there is when you have the given amount of UOM1. <br/> </p>"


    @app.route('/listdimensionclasses/', methods=['GET'])
    def dimensionlistpage():

        tempDict = {}
        tempDict['Dimension classes'] = []
        for i in dimSet:
            tempDict['Dimension classes'].append(i)
        return jsonify(tempDict)

    @app.route('/listquantitytypes/', methods =['GET'])
    def quantitylistpage():
        tempDict = {}
        tempDict['Quantity types'] = []
        for i in quanSet:
            tempDict['Quantity types'].append(i)
        return jsonify(tempDict)

    @app.route('/givendimension/<path:givenDim>/', methods =['GET'])
    def givendimensionpage(givenDim):
        givenDim = str(givenDim)
        dim = printUOMDim(dimDict, givenDim)
        tempDict = {}
        tempDict[givenDim] = []
        for i in dim:
            tempDict[givenDim].append(i)
        return jsonify(tempDict)


    @app.route('/givenquantitytype/<path:givenQuan>/', methods=['GET'])
    def givenquantitypage(givenQuan):
        givenQuan = str(givenQuan)
        quan = printUOMDim(quanDict, givenQuan)
        tempDict = {}
        tempDict[givenQuan] = []
        for i in quan:
            tempDict[givenQuan].append(i)
        return jsonify(tempDict)

    @app.route('/convertuom/<amount>/<uom1>/<uom2>/', methods=['GET'])
    def convertuompage(amount, uom1, uom2):
        try:
            amount = float(amount)
        except ValueError:
            return 'The entered amount is not valid'
        tempDict = {}
        uom1 = str(uom1)
        uom2 = str(uom2)
        answer = str(calculateConversion(amount, uom1, uom2, denomDict, factorDict))

        anno = str(printUOMAnnot(annotDict, uom2))

        tempDict['Unit of measure'] = uom2
        tempDict['Annotation'] = anno
        tempDict['Amount'] = answer

        return jsonify(tempDict)


    app.run(host='0.0.0.0')
