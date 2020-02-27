with open('examplefile.txt', 'r') as exFile:
    print("The file will close when the with is exited, without us doing so")
#With can be used to encapsulate try, catch, and finally routines into one
#common block of code. See the documentation for more details along with:
#https://book.pythontips.com/en/latest/context_managers.html
