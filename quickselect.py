import random


def quickselect(l, k, counter):
    length = len(l)
    # Pick a random pivot element from the list, each
    # equally likely
    pivot = l[random.randint(0,length-1)]
    
    l_small = []
    l_big = []
    # Put all elements smaller than pivot into l_small, and all
    # larger elements into l_big.
    
    for element in l:
        if element == pivot:
            continue
        elif element < pivot:
            l_small.append(element)
        else:
            l_big.append(element)
    
    # We assume all elements are distinct, so (besides the pivot) every element
    # should go into l_small or l_big
    assert(length == len(l_small) + len(l_big) + 1)
    if  k == len(l_big) + 1:
        return pivot, counter+1
    elif k <= len(l_big):
        # kth largest must be in l_big
        res = quickselect(l_big, k, counter+1)
        return res
    elif k > len(l_big) + 1:
        # kth largest must be in l_small
        res = quickselect(l_small, k - len(l_big) - 1, counter+1)
        return res
    


def quickselect2(l, k,counter):
    
    length = len(l)
    if length == 1:
        return l[0], counter+1
    # Pick a random pivot element from the list, each
    # equally likely
    pivot1 = random.choice([ele for ele in l])
    pivot2 = random.choice([ele for ele in l if ele != pivot1])
    
    l_small = []
    l_medium = []
    l_big = []
    # Put all elements smaller than pivot into l_small, and all
    # larger elements into l_big.
    a = 0
    b = 0
    if pivot1 > pivot2:
        b = pivot1
        a = pivot2
    else:
        b = pivot2
        a = pivot1 
    for element in l:
        if element == pivot1 or element == pivot2:
            continue
        elif element < a:
            l_small.append(element)
        elif element > a and element < b:
            l_medium.append(element)
        else:
            l_big.append(element)
    # We assume all elements are distinct, so (besides the pivot) every element
    # should go into l_small or l_big
    assert(length == len(l_small) + len(l_medium) + len(l_big) + 2)

    
    
    if k == len(l_big) +1:
        return b, counter +1
    elif k == len(l_big) + len(l_medium) + 2:
        return a, counter+1
    elif k<= len(l_big):
        # kth largest must be in l_big
        res = quickselect2(l_big, k, counter+1)
        return res 
    #elif k == len(l_big)+ 1:
        #return b, counter +1
    elif (k > (len(l_big)+1)) and (k <= (len(l_big) + len(l_medium) + 1)):
        # kth largest must be in l_medium
        res = quickselect2(l_medium, k - len(l_big) - 1,counter+1)
        return res
    #elif k == len(l_big)+len(l_medium)+2:
        #return a, counter+1
    elif k > len(l_big)+len(l_medium)+2:
        # kth largest must be in l_small
        res = quickselect2(l_small, k - len(l_big) - len(l_medium) - 2, counter+1)
        return res
    
    



def montecarlo(l,k,counter,n):
    list_of_qs1_trials = []
    list_of_qs2_trials = []
    listsum1 = 0
    listsum2 = 0
    for i in range(0,n-1):
        a = quickselect(l,k,counter)
        b = list(a)
        list_of_qs1_trials.append(b[1])
        listsum1 += list_of_qs1_trials[i]
##        c = quickselect2(l,k,counter)
##        d = list(c)
##        list_of_qs2_trials.append(d[1])
##        listsum2 += list_of_qs2_trials[i]

 
    return listsum1/len(list_of_qs1_trials)


def main():
    number_of_trials = int(input("How many trials would you like to simulate?"))

    v = montecarlo(superbiglist,7,0,100)
    if v <= 0:
        print("Quickselect with 2 pivots had ", -v, "less recursions per trial compared to quickselect with 1 pivot")
    else:
        print("Quickselect with 2 pivots had ", v, "more recursions per trial compared to quickselect with 1 pivot")
                           
    
superbiglist = list(range(175))
print(montecarlo(superbiglist,30,0,20000))

    




    
