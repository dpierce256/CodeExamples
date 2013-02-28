FeatureSet = [False, False, False, False]


def GetProductCapabilities(ProductID):
	"""Stores dictionary of products and related feature capabilities."""
	Products = {
	#Product Category A
	'ProductA1' : ProductCategoryA,
	'ProductA2' : ProductCategoryA,
	'ProductA3' : ProductCategoryA,
	'ProductA4' : ProductCategoryA,
	'ProductA5' : ProductCategoryA,
	'ProductA6' : ProductCategoryA,

	#Product Category B
	'ProductB1' : ProductCategoryB,
	'ProductB2' : ProductCategoryB,
	'ProductB3' : ProductCategoryB,
	'ProductB4' : ProductCategoryB,
	'ProductB5' : ProductCategoryB,
	'ProductB6' : ProductCategoryB,

	#Product Category C
    'ProductC1' : ProductCategoryC,
	'ProductC2' : ProductCategoryC,
	'ProductC3' : ProductCategoryC,
	'ProductC4' : ProductCategoryC,
	'ProductC5' : ProductCategoryC,
	'ProductC6' : ProductCategoryC,
    
	#Product Category D
    'ProductD1' : ProductCategoryD,
	'ProductD2' : ProductCategoryD,
	'ProductD3' : ProductCategoryD,
	'ProductD4' : ProductCategoryD,
	'ProductD5' : ProductCategoryD,
	'ProductD6' : ProductCategoryD,

	#Product Category E
    'ProductE1' : ProductCategoryE,
	'ProductE2' : ProductCategoryE,
	'ProductE3' : ProductCategoryE,
	'ProductE4' : ProductCategoryE,
	'ProductE5' : ProductCategoryE,
	'ProductE6' : ProductCategoryE,
	}
	Products[ProductID]()

def ProductCategoryA():
    global FeatureSet
    FeatureSet = [True, True, False, False]

def ProductCategoryB():
    global FeatureSet
    FeatureSet = [True, True, True, True]

def ProductCategoryC():
    global FeatureSet
    FeatureSet = [True, False, False, False]

def ProductCategoryD():
    global FeatureSet
    FeatureSet = [True, False, True, False]

def ProductCategoryE():
    global FeatureSet
    FeatureSet = [True, False, True, True]


#Generate CLI output required to run tests for each feature, and
#store it in a .bat file.
MyProduct = raw_input('Which product? ')

MyTest = raw_input('Which test?' )

GetProductCapabilities(MyProduct)

f = open('TestRun.bat', 'w')

if FeatureSet[0] == True:
    f.write('TestSystemCLI -p Type=FeatureA ' + MyTest + '\n')

if FeatureSet[1] == True:
    f.write('TestSystemCLI -p Type=FeatureB ' + MyTest + '\n')

if FeatureSet[2] == True:
    f.write('TestSystemCLI -p Type=FeatureC ' + MyTest + '\n')

if FeatureSet[3] == True:
    f.write('TestSystemCLI -p Type=FeatureD ' + MyTest + '\n')

f.close()

raw_input('Batch file generated. Press any key to exit.')