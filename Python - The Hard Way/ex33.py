
i = 0
numbers = []

def myloop(j):
    global i
    while i < j:
        print "At the top i is %d" % i
        numbers.append(i)
        i += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

myloop(6)

print "The numbers:"
for num in numbers:
    print num