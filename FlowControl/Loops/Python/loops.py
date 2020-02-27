currIteration = 0
numberOfIterations = 5
while currIteration < numberOfIterations:
    print(f"This will be printed 5 times. Current Iteration is {currIteration}")
    currIteration += 1
currentValue = 5
while currentValue > 0:
    print(f"This will also be printed 5 times. Current Value is {currentValue}")
    currentValue -= 1
else:
    print(f"This will be printed once, when currentValue is 0. It is {currentValue}")

while currentValue > 0:
    print("This will never be printed")
    currentValue -= 1
else:
    print("See, the else prints out but the loop never ran")

while currentValue < numberOfIterations:
    if currentValue > 2:
        break
    print(f"This will only be printed out 3 times. Current Value is {currentValue}")
    currentValue += 1

currentValue = 0
while currentValue < numberOfIterations:
    currentValue += 1
    if currentValue == 3:
        continue
    print(f"This will skip 3. Current Value is {currentValue}")

for i in range(0, 5):
    print(f"This will print 5 times. Currently on iteration {i}")

for i in range(0, 5):
    print(f"This will print 5 times. Currently on iteration {i}")
else:
    print(f"This will print one time. The value of i is {i}")

exampleList = ["elem1", "elem2", "elem3", "elem4"]
for elem in exampleList:
    print(elem)

for elem in exampleList:
    if elem == "elem2":
        break
    print(elem)

for elem in exampleList:
    if elem == "elem2":
        continue
    print(elem)

for i in range(10):
    print(i)
    i = 5  
