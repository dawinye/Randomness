import numpy


def function1(d,a,b):
    counterA = 0
    counterB = 0
    counterA1 = 0
    counterB1 = 0
    printStatement = " is more likely"
    
    for x in range(400):
        for x in range(400):
            alloutcomes = [] 
            for x in range(d):
                z = numpy.random.randint(1,7)
                alloutcomes.append(z)
                sum1 = sum(alloutcomes)
            if a == sum1:
                counterA += 1
            if b == sum1:

                counterB += 1

        if counterA > counterB:
            counterA1 += 1
        elif counterA < counterB:
            counterB1 += 1

    if counterA1 > counterB1:
        return str(a) + printStatement
    elif counterB1 > counterA1:
        return str(b) + printStatement
    else:
        function(d,a,b)

  
        

    
print(function1(3,11,12))

