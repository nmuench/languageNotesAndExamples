a = 1
b = 2
c = a + b

if a == 1:
    print("This will print")

if a == 2:
    print("This will not print")

if a == 2:
    print("This will not print")
else:
    print("This will print")

if a == b:
    print("This will not print")
elif c == (a + b):
    print("This will print")

if a == b:
    print("This will not print")
elif not c == (a + b):
    print("This will not print")
else:
    print("This will print")

d = c if (a == b) else a
print(f"d is {d}, c is {c}, a is {a}")
d = c if c == (a + b) else a
print(f"d is {d}, c is {c}, a is {a}")
