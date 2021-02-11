import numpy

def main():
    d = int(input("How many dice would you like to roll?"))
    a = int(input("What is your first sum"))
    b = int(input("What is your second sum"))
    print(sums(d,a,b))

def sums(d,a,b):
    counterA = 0
    counterB = 0
    printStatement = " is more likely"


    for x in range(100000):
        sum1 = 0
        for x in range(d):
            z = numpy.random.randint(1,7)
            sum1 += z
        if a == sum1:
            counterA += 1
        if b == sum1:
            counterB += 1


    probA = counterA/100000
    probB = counterB/100000
    difference = abs(probA - probB)
    if difference < 1/(6**d):
        return str(a) + " and " + str(b) + " are equally likely"
    elif counterB > counterA:
        return str(b) + printStatement
    else:
        return str(a) + printStatement


        
main()


