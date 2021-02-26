from scipy.special import binom, factorial

def main():
    for i in range(0,101):
        for j in range(0,i):
            alpha = 1 - probcalc(0.7,0.3,i,j)
            beta = probcalc(0.5,0.5,i,j)
            if (alpha < 0.05) and (beta < 0.05):
                print(i,j,alpha,beta)
                break
        

def probcalc(prob1, prob2, trials, cases):
    prob = 0
    for i in range (cases, trials+1):
        prob += (prob1**i)*(prob2**(trials-i))*binom(trials,i)
    return prob



main()
