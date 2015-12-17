import math

rows = 10

a = int(math.floor(rows / 7))
b = ((a * (a + 1)) / 2) * 21

print(a)
print(b)

# rest
r = rows % 7

for x in xrange((a * 7) + 1, rows+1):
    t = int(x - ((math.ceil(x/7) * (x % 7)) + (x % 7)))
    print(t)
    b += t

#remove first 21 none existing triangle
print(rows, b-21, (rows*(rows+1) / 2) - (b-21))