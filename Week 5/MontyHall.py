import random
from matplotlib import pyplot as plt

def simulation(n):
    #counters for correct and incorrect totals as well as the total trials
    correct_switch_counter = 0
    correct_noswitch_counter = 0
    incorrect_switch_counter = 0
    incorrect_noswitch_counter = 0
    switch_trials = 0


    #initialize lists so that data can be graphed
    switchincorrectlist = []
    switchlist = []
    switchtrialslist = []
    
    for i in range(n):

        #generate random numbers for the correct answer and guess, initialize the revea;
        correct = random.randint(1,3)
        guess = random.randint(1,3)
        reveal = 0

        #the reveal must be different from correct and guess if those 2 values are not the same
        if correct != guess:
            reveal = random.randint(1,3)
            while (reveal == correct) or (reveal == guess):
                reveal = random.randint(1,3)

        #if guess and correct are the same, then randomly pick one of the other 2 values, only condition is that it
        #can't be the same as correct
        else:
            reveal = random.randint(1,3)
            while (reveal == correct):
                reveal = random.randint(1,3)

        #coin flip choosing if you switch your choice or not
        switch_or_not = random.randint(1,2)

        #1 indicates you want to switch
        
        if switch_or_not == 1:
            #since guess reveal and correct occupy 3 out of 3 possible values and we can't choose the revealed one,
            #guess has to equal correct
            if (correct != guess):
                guess = correct
            else:
            #if correct and guess are the same, then guess must be changed to the value that isn't correct or reveal
                while (guess == correct) or (guess == reveal):
                    guess = random.randint(1,3)
            #check if the guess is correct, increment counters accordingly
            if guess == correct:
                correct_switch_counter += 1
            else:
                incorrect_switch_counter += 1
            switch_trials += 1

            #update the lists used to graph the data
            switchtrialslist.append(switch_trials)
            switchlist.append(correct_switch_counter)
            switchincorrectlist.append(incorrect_switch_counter)
        else:
            if guess == correct:
                correct_noswitch_counter += 1
            else:
                incorrect_noswitch_counter += 1
    
    plt.style.use("fivethirtyeight")
    plt.plot(switchtrialslist, frequency(switchlist), label = "Number of Correct Guesses")
    plt.plot(switchtrialslist, frequency(switchincorrectlist), label = "Number of Incorrect Guesses")
    plt.title("Frequency of Correct vs. Incorrect Guesses If You Switch")
    plt.xlabel("# of Trials")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
    #print(switchlist)
    return correct_switch_counter, incorrect_switch_counter, correct_noswitch_counter, incorrect_noswitch_counter 

def frequency(list1):
    list1_copy = list1
    for i in range(len(list1)):
        list1_copy[i] = list1_copy[i]/(i+1)
    return list1_copy

print(simulation(500)) 
