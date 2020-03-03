import math
dictOfBuiltInTypes = [
    "boolean", "int", "float", "complex",
    "iterator", "list", "tuple", "range",
    "string", "bytes", "bytearray", "memoryview"
    "set", "frozenset", "dict"
]

dictOfSpecializedDataTypes = ["namedtuple"]

def showBooleanUsage():
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

def showBytesUsage():
    exampleBytes = bytes()
    exampleBytes = b'still allows embedded "double" quotes'
    print(exampleBytes)
    exampleBytes = b"still allows embedded 'single' quotes"
    print(exampleBytes)
    exampleBytes = b'''3 single quotes'''
    print(exampleBytes)
    exampleBytes = b"""3 double quotes"""
    print(exampleBytes)
    exampleBytes = bytes.fromhex('2Ef0 F1f2 ')
    print(exampleBytes)
    exampleBytes = bytes.fromhex('54657374')
    print(exampleBytes)
    #Check documentation for more functions, these cover basics

def showByteArrayUsage():
    exampleBytesArray = bytearray()
    exampleBytesArray = bytearray.fromhex('546573742069732074686973')
    print(exampleBytesArray)
    ##################### Mutable Operations Region
    exampleBytesArray[0] = 87
    print(exampleBytesArray)
    helperByteArray = bytearray(b"hi")
    print(exampleBytesArray)
    exampleBytesArray[0:2] = helperByteArray
    print(exampleBytesArray)
    del exampleBytesArray[0:2]
    print(exampleBytesArray)
    exampleBytesArray[0:6:3] = helperByteArray
    print(exampleBytesArray)
    del exampleBytesArray[0:5:2]
    print(exampleBytesArray)
    exampleBytesArray.append(33)
    print(exampleBytesArray)
    exampleBytesArray.clear()
    print(exampleBytesArray)
    exampleBytesArray = helperByteArray.copy()
    print(exampleBytesArray)
    print(helperByteArray)
    exampleBytesArray[0] = 48
    print(exampleBytesArray)
    #Copy does not pass between the two copies. They are stored separately
    print(helperByteArray)
    exampleBytesArray.extend(bytearray(b"This Should Be Extended"))
    print(exampleBytesArray)
    exampleBytesArray *= 3
    print(exampleBytesArray)
    exampleBytesArray.insert(1, 115)
    print(exampleBytesArray)
    exampleBytesArray.pop(1)
    print(exampleBytesArray)
    exampleBytesArray.remove(84)
    print(exampleBytesArray)
    exampleBytesArray.reverse()
    print(exampleBytesArray)
    ##################### End Region
    #Check documentation for more functions, these cover basics

def showMemoryviewsage():
    exampleMemoryView = memoryview(b'This is a memory view')
    print(exampleMemoryView)
    #Used to access the internal data of an object that supports the buffer protocol
    #without copying. The types bytes and bytearray both support it.

def showSetUsage():
    #Sets contain unordered collections of hashable objects
    exampleSet = set([1, 2, 3, 4 , 5])
    ###### Operations for set and frozen set Region
    print(exampleSet)
    print(len(exampleSet))
    print(1 in exampleSet)
    print(6 not in exampleSet)
    otherSet = set([6, 7, 8, 9])
    print(exampleSet.isdisjoint(otherSet))
    otherSet = set([5, 6, 7, 8, 9])
    print(not exampleSet.isdisjoint(otherSet))
    otherSet = set([2, 3, 4])
    print(otherSet.issubset(exampleSet))
    otherSet = set([5, 6, 7, 8, 9])
    print(not otherSet.issubset(exampleSet))
    #Check if example set is a subset of other set another way
    otherSet = set([0,1,2,3,4,5,6,7])
    print(exampleSet <= otherSet) #True
    #Check if example set is a proper subset of otherSet, subset and not equal to.
    print(exampleSet < otherSet) #True
    print(otherSet.issuperset(exampleSet)) # True
    print(otherSet >= exampleSet) # True
    print(otherSet > exampleSet) #True
    #Check if example set is a subset of other set another way
    #This is to show off the "proper subset" distinction
    otherSet = set([1, 2, 3, 4 , 5])
    print(exampleSet <= otherSet) # True
    #Check if example set is a proper subset of otherSet, subset and not equal to.
    print(exampleSet < otherSet) #False
    print(otherSet.issuperset(exampleSet)) #True
    print(otherSet >= exampleSet) #True
    print(otherSet > exampleSet) #False
    otherSet = set([4,5,6,7])
    print(exampleSet.union(otherSet)) #Note that the function versions of these accept any iterable, not just sets
    print(exampleSet | otherSet)
    print(exampleSet.intersection(otherSet))  #Note that the function versions of these accept any iterable, not just sets
    print(exampleSet & otherSet)
    print(exampleSet.difference(otherSet))  #Note that the function versions of these accept any iterable, not just sets
    print(exampleSet - otherSet)
    print(otherSet.difference(exampleSet))  #Note that the function versions of these accept any iterable, not just sets
    print(otherSet - exampleSet)
    print(exampleSet.symmetric_difference(otherSet))  #Note that the function versions of these accept any iterable, not just sets
    print(exampleSet ^ otherSet)
    ###### End Region
    print("Set only operations: ")
    ###### Set Only Region
    exampleSet = set([1, 2, 3, 4 , 5])
    otherSet = set([4,5,6,7])
    exampleSet.update(otherSet) #The operator version is |=
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet |= otherSet
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet.intersection_update(otherSet) #Operator version is &=
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet &= otherSet
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet.difference_update(otherSet) #Operator version is -=
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet -= otherSet
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet.symmetric_difference_update(otherSet) #Operator version is ^=
    print(exampleSet)
    exampleSet = set([1, 2, 3, 4 , 5])
    print(exampleSet)
    exampleSet ^= otherSet
    print(exampleSet)
    exampleSet.add(8)
    print(exampleSet)
    exampleSet.remove(1) #Error if not present
    print(exampleSet)
    exampleSet.discard(8) #Checks and removes if present
    print(exampleSet)
    exampleSet.discard(9) # No error even though 9 isn't present
    print(exampleSet)
    elem = exampleSet.pop() #Removes an arbitrary element
    print(elem)
    print(exampleSet)
    exampleSet.clear()
    print(exampleSet)
    ###### End Region

def showFrozenSetUsage():
    #FrozenSets contain unordered collections of hashable objects
    exampleFrozenSet = frozenset([1, 2, 3, 4 , 5])
    ###### Operations for FrozenSet and frozen FrozenSet Region
    print(exampleFrozenSet)
    print(len(exampleFrozenSet))
    print(1 in exampleFrozenSet)
    print(6 not in exampleFrozenSet)
    otherFrozenSet = frozenset([6, 7, 8, 9])
    print(exampleFrozenSet.isdisjoint(otherFrozenSet))
    otherFrozenSet = frozenset([5, 6, 7, 8, 9])
    print(not exampleFrozenSet.isdisjoint(otherFrozenSet))
    otherFrozenSet = frozenset([2, 3, 4])
    print(otherFrozenSet.issubset(exampleFrozenSet))
    otherFrozenSet = frozenset([5, 6, 7, 8, 9])
    print(not otherFrozenSet.issubset(exampleFrozenSet))
    #Check if example FrozenSet is a subFrozenSet of other FrozenSet another way
    otherFrozenSet = frozenset([0,1,2,3,4,5,6,7])
    print(exampleFrozenSet <= otherFrozenSet) #True
    #Check if example FrozenSet is a proper subFrozenSet of otherFrozenSet, subFrozenSet and not equal to.
    print(exampleFrozenSet < otherFrozenSet) #True
    print(otherFrozenSet.issuperset(exampleFrozenSet)) # True
    print(otherFrozenSet >= exampleFrozenSet) # True
    print(otherFrozenSet > exampleFrozenSet) #True
    #Check if example FrozenSet is a subFrozenSet of other FrozenSet another way
    #This is to show off the "proper subFrozenSet" distinction
    otherFrozenSet = frozenset([1, 2, 3, 4 , 5])
    print(exampleFrozenSet <= otherFrozenSet) # True
    #Check if example FrozenSet is a proper subFrozenSet of otherFrozenSet, subFrozenSet and not equal to.
    print(exampleFrozenSet < otherFrozenSet) #False
    print(otherFrozenSet.issuperset(exampleFrozenSet)) #True
    print(otherFrozenSet >= exampleFrozenSet) #True
    print(otherFrozenSet > exampleFrozenSet) #False
    otherFrozenSet = frozenset([4,5,6,7])
    print(exampleFrozenSet.union(otherFrozenSet)) #Note that the function versions of these accept any iterable, not just FrozenSets
    print(exampleFrozenSet | otherFrozenSet)
    print(exampleFrozenSet.intersection(otherFrozenSet))  #Note that the function versions of these accept any iterable, not just FrozenSets
    print(exampleFrozenSet & otherFrozenSet)
    print(exampleFrozenSet.difference(otherFrozenSet))  #Note that the function versions of these accept any iterable, not just FrozenSets
    print(exampleFrozenSet - otherFrozenSet)
    print(otherFrozenSet.difference(exampleFrozenSet))  #Note that the function versions of these accept any iterable, not just FrozenSets
    print(otherFrozenSet - exampleFrozenSet)
    print(exampleFrozenSet.symmetric_difference(otherFrozenSet))  #Note that the function versions of these accept any iterable, not just FrozenSets
    print(exampleFrozenSet ^ otherFrozenSet)
    ###### End Region

# def showDictUsage():
#     f

showFrozenSetUsage()
