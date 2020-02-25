import math
dictOfBuiltInTypes = [
    "boolean", "int", "float", "complex",
    "iterator", "list", "tuple", "range",
    "string", "bytes", "bytearray", "memoryview"
    "set", "frozenset", "dict"
]

def showBooleanUsage():
    exampleBool = Boolean()
    exampleBool = True
    if exampleBool:
        print("exampleBool is True")
    if not exampleBool:
        print("This won't print out")
    exampleBool = False
    if not exampleBool:
        print("exampleBool is False")
    if exampleBool:
        print("This won't print out")

def showIntUsage():
    print("Int Usage: ")
    exampleInt = int()
    exampleInt = 1
    print(exampleInt)
    exampleInt = 1 + 2
    print(exampleInt)
    exampleInt = 1 - 2
    print(exampleInt)
    exampleInt = 2 * 3
    print(exampleInt)
    exampleInt = 4 / 2 #Returns floating point
    print(exampleInt)
    exampleInt = 5 // 2 #Floored Quotient
    print(exampleInt)
    exampleInt = 5 % 2
    print(exampleInt)
    exampleInt = -exampleInt
    print(exampleInt)
    exampleInt = +exampleInt
    print(exampleInt)
    exampleInt = abs(exampleInt)
    print(exampleInt)
    exampleInt = int(3.0)
    print(exampleInt)
    floorQuotient, remainder = divmod(5, 2)
    print(floorQuotient)
    print(remainder)
    print(exampleInt)
    exampleInt = pow(3, 2)
    print(exampleInt)
    exampleInt = 3 ** 2
    print(exampleInt)

def showFloatUsage():
    print("Float Usage: ")
    exampleFloat = int()
    exampleFloat = 1.
    print(exampleFloat)
    exampleFloat = 1. + 2.5
    print(exampleFloat)
    exampleFloat = 1. - 2.5
    print(exampleFloat)
    exampleFloat = 2.3 * 3
    print(exampleFloat)
    print(math.ceil(exampleFloat))
    print(round(exampleFloat, 1))
    exampleFloat = 4 / 2 #Returns floating point
    print(exampleFloat)
    exampleFloat = 5 // 2 #Floored Quotient
    print(exampleFloat)
    exampleFloat = 5 % 2
    print(exampleFloat)
    exampleFloat = 2.1
    exampleFloat = -exampleFloat
    print(exampleFloat)
    exampleFloat = +exampleFloat
    print(exampleFloat)
    exampleFloat = abs(exampleFloat)
    print(exampleFloat)
    exampleFloat = float(1)
    print(exampleFloat)
    floorQuotient, remainder = divmod(5.5, 2)
    print(floorQuotient)
    print(remainder)
    print(exampleFloat)
    exampleFloat = pow(3.3, 2)
    print(exampleFloat)
    print(math.ceil(exampleFloat))
    print(round(exampleFloat, 1))
    exampleFloat = 3.3 ** 2
    print(exampleFloat)
    print(math.ceil(exampleFloat))
    print(round(exampleFloat, 1))

def showComplexUsage():
    exampleComplex = complex(1, -2)
    print(exampleComplex.real)
    print(exampleComplex.imag)
    print(exampleComplex.conjugate())

def showIteratorUsage():
    a = ["1", "2", "3"]
    exampleIter = a.__iter__()
    print(exampleIter.__next__())
    print(next(exampleIter))

def showListUsage():
    exampleList = ["1", "2", "3", "4"]
    print("1" in exampleList)
    print("5" not in exampleList)
    helperList = ["5", "6", "7"]
    print(exampleList + helperList)
    print(exampleList * 3)
    print(exampleList[1])
    print(exampleList[1:3])

# def showTupleUsage():
#     f
# def showRangeUsage():
#     f
# def showStringUsage():
#     f
# def showBytesUsage():
#     f
# def showByteArrayUsage():
#     f
# def showMemoryviewsage():
#     f
# def showSetUsage():
#     f
# def showFroaenSetUsage():
#     f
# def showDictUsage():
#     f

# showIntUsage()
# showFloatUsage()
showIteratorUsage()
