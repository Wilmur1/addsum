summm = open("Quiz Game/sum.txt", "r")
sum1 = summm.read()
add = sum1.split(",")
sum5 = 0
for a in add:
    integer = int(a)
    sum5 = sum5 + integer
print(sum5)
