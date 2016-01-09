x = 1
y = 2
total = 2
while x < 4000000 and y < 4000000:
    x = x + y
    y = x + y
    if x % 2 == 0:
        total = total + x
    if y % 2 == 0:
        total = total + y
    print total
