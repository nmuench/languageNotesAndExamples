a = 4
b = 2
try:
    c = a / b
    print(f"This will work without any problem")
except Exception as e:
    print("This will not print")
b = 0
try:
    c = a / b
    print("This will not be printed, because an exception will be raised by dividing by zero")
except ZeroDivisionError as e:
    print(str(e))
print("The exception was caught, and the program continued form the end of the try-except block")

try:
    c = a / b
    print("This will not be printed, because an exception will be raised by dividing by zero")
except Exception as e:
    print(str(e))
    print("We can catch general exceptions if we want broader coverage than the specific example above")

try:
    c = a / b
    print("This will not be printed, because an exception will be raised by dividing by zero")
except Exception as e:
    print("The exception was caught")
finally:
    print("This will always happen, exception or no exception")
b = 1
try:
    c = a / b
    print("There was no exception this time")
except Exception as e:
    print("This won't happen without an exception being raised and caught")
finally:
    print("This will always happen, exception or no exception")
