x = int(input("First Number?:"))
y = int(input("Second Number?:"))

result = 0

if y < 0:
    count = -y
else:
    count = y

while count > 0:

    if x == 0:
        count = 0
    result += x
    count -= 1

print (result)