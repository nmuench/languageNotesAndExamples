import math
dictOfBuiltInTypes = [
    "boolean", "int", "float", "complex",
    "iterator", "list", "tuple", "range",
    "string", "bytes", "bytearray", "memoryview"
    "set", "frozenset", "dict"
]

dictOfSpecializedDataTypes = ["namedtuple"]

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
    ##################### Common Sequence Operations Region
    print("1" in exampleList)
    print("5" not in exampleList)
    helperList = ["5", "6", "7"]
    print(exampleList + helperList)
    exampleList = exampleList * 3
    print(exampleList)
    print(exampleList[1])
    print(exampleList[1:3])
    print(exampleList[::2])
    print(len(exampleList))
    print(min(exampleList))
    print(max(exampleList))
    print(exampleList.index('3', 3, 9))
    print(exampleList.count("1"))
    print(exampleList[-1])
    print(exampleList[-2])
    ##################### End Region
    ##################### Mutable Operations Region
    exampleList[0] = "5"
    print(exampleList)
    helperList = ["a", "b", "c"]
    print(exampleList)
    exampleList[0:2] = helperList
    print(exampleList)
    del exampleList[0:2]
    print(exampleList)
    exampleList[0:5:2] = helperList
    print(exampleList)
    del exampleList[0:5:2]
    print(exampleList)
    exampleList.append("Appended")
    print(exampleList)
    exampleList.clear()
    print(exampleList)
    exampleList = helperList.copy()
    print(exampleList)
    print(helperList)
    helperList[0] = "Test"
    print(exampleList)
    #Copy does not pass between the two copies. They are stored separately
    print(helperList)
    exampleList.extend(["This", "Should", "Be", "Extended"])
    print(exampleList)
    exampleList *= 3
    print(exampleList)
    exampleList.insert(1, "Second Element")
    print(exampleList)
    exampleList.pop(1)
    print(exampleList)
    exampleList.remove("This")
    print(exampleList)
    exampleList.reverse()
    print(exampleList)
    ##################### End Region
    exampleList.sort(key=str.lower)
    print(exampleList)

def showTupleUsage():
    exampleTuple = ("1", "2", "3", "4")
    ##################### Common Sequence Operations Region
    print("1" in exampleTuple)
    print("5" not in exampleTuple)
    helperTuple = ("5", "6", "7")
    print(exampleTuple + helperTuple)
    exampleTuple = exampleTuple * 3
    print(exampleTuple)
    print(exampleTuple[1])
    print(exampleTuple[1:3])
    print(exampleTuple[::2])
    print(len(exampleTuple))
    print(min(exampleTuple))
    print(max(exampleTuple))
    print(exampleTuple.index('3', 3, 9))
    print(exampleTuple.count("1"))
    print(exampleTuple[-1])
    print(exampleTuple[-2])
    ##################### End Region
    print(hash(exampleTuple))

# # TODO: Make correct
# def showNamedTupleUsage():
#     exampleTuple = ("1", "2", "3", "4")
#     ##################### Common Sequence Operations Region
#     print("1" in exampleTuple)
#     print("5" not in exampleTuple)
#     helperTuple = ("5", "6", "7")
#     print(exampleTuple + helperTuple)
#     exampleTuple = exampleTuple * 3
#     print(exampleTuple)
#     print(exampleTuple[1])
#     print(exampleTuple[1:3])
#     print(exampleTuple[::2])
#     print(len(exampleTuple))
#     print(min(exampleTuple))
#     print(max(exampleTuple))
#     print(exampleTuple.index('3', 3, 9))
#     print(exampleTuple.count("1"))
#     print(exampleNamedTuple[-1])
#     print(exampleNamedTuple[-2])
#     ##################### End Region
def showRangeUsage():
    exampleRange = range(0, 10)
    ##################### Common Sequence Operations Region
    print(1 in exampleRange)
    print(10 not in exampleRange)
    print(exampleRange)
    print(exampleRange[1])
    print(exampleRange[1:3])
    print(exampleRange[::2])
    print(exampleRange[-1])
    print(exampleRange[-2])
    ##################### End Region
def showStringUsage():
    exampleString = 'Single quotes allow us to use "" within the string'
    exampleString = "Double quotes allow us to use '' within the string"
    exampleString = '''Triple quotes allow us to use '' and "" within the string'''
    exampleString = """
    Triple quotes allow us to use '' and "" within the string,
    plus we can span multiple lines"""
    exampleString = str("Hello, this is a string")
    ##################### Common Sequence Operations Region
    print("Hello" in exampleString)
    print("5" not in exampleString)
    helperString = " this will be added on"
    print(exampleString + helperString)
    exampleString = "This will be repetead three times "
    exampleString = exampleString * 3
    print(exampleString)
    print(exampleString[1])
    print(exampleString[1:3])
    print(exampleString[::2])
    print(len(exampleString))
    print(min(exampleString))
    print(max(exampleString))
    print(exampleString.index('will', 3, 9))
    print(exampleString.count("be"))
    print(exampleString[-2])
    print(exampleString[-3])
    ##################### End Region
    ##################### String Methods Region
    exampleString = "this is an example string"
    print(exampleString.capitalize())
    exampleString = "Uppercase becomes lowercase"
    print(exampleString.casefold())
    print(exampleString.center(50))
    exampleString = "Repeat Repeat Repeat"
    print(exampleString.count("Repeat"))
    print(exampleString.encode())
    print(exampleString.endswith("Repeat"))
    #THERE ARE MANY MORE OF THESE, BUT YOU CAN LOOK THEM UP
    ##################### End Region
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
showStringUsage()
