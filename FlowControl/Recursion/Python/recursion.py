def recursiveFunction(numberOfRecurses):
    if numberOfRecurses <= 0:
        print("The recursion has ended")
        return
    print(f"There are {numberOfRecurses} recursions left")
    recursiveFunction(numberOfRecurses - 1)

recursiveFunction(5)

def createFibonnaci(fibonnaciIndex):
    if(fibonnaciIndex == 0):
        print("0 ", end="")
        return((0, 0))
    if(fibonnaciIndex == 1):
        print("0 1 ", end="")
        return((1, 0))
    previous, twoBefore = createFibonnaci(fibonnaciIndex - 1)
    currFibb = previous + twoBefore
    print(str(currFibb) + " ", end = "")
    return((currFibb, previous))

createFibonnaci(12)
