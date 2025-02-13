#Version without loop while.
n = int(input("Write the number:\n"))
print("The multiplication table of the number {} is...".format(n))
print("{} x 0 = {}".format(n, n * 0))
print("{} x 1 = {}".format(n, n * 1))
print("{} x 2 = {}".format(n, n * 2))
print("{} x 3 = {}".format(n, n * 3))
print("{} x 4 = {}".format(n, n * 4))
print("{} x 5 = {}".format(n, n * 5))
print("{} x 6 = {}".format(n, n * 6))
print("{} x 7 = {}".format(n, n * 7))
print("{} x 8 = {}".format(n, n * 8))
print("{} x 9 = {}".format(n, n * 9))
print("{} x 10 = {}".format(n, n * 10))

#Version with loop while.
n = int(input("Write the number:\n"))
print("The multiplication table of the number {} is...".format(n))
count = 0
while count <= 10:
    print("{} x {} = {}".format(n, count, n * count))
    count += 1

#Version with list and loop for
n = int(input("Write the number:\n"))
print("The multiplication table of the number {} is...".format(n))
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nl in list:
    print("{} x {} = {}".format(n, nl, n * nl))