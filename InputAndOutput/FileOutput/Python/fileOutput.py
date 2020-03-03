a = "This will be printed to the file output.txt"

with open("output.txt", "w") as outFile:
    outFile.write(a)
