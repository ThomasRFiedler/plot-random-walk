"""
Author: Tommy Fiedler, tommyrfiedler@gmail.com
Date: 02/25/2023

Description:
    Generate plots of random walks to simulate market data.

"""

import random
from math import sqrt, exp, log
from matplotlib import pyplot as plt

# Generate a random number from a normal distribution
def getRandom(size, stddev, avg):
  
    samples = [random.random() - 0.5 for i in range(size)]
    R = sum(samples) * (sqrt(size/12))
    R *= stddev
    R += avg

    return R

# Generate x and y 
def randWalk(start, length, stddev, avg):
    
    x = [1]
    y = [start]

    # Number of random numbers to draw from
    N = 10

    for i in range(length):
        x.append(i+2)
        
        # Get Random Variable
        R = getRandom(N, stddev, avg)

        # Brownian motion
        
        result = log(y[i]) + R
        
        
        y.append(exp(result))

    return x, y

# Plot the specified number of walks
def plotWalks(num, start, length, stddev, avg):
    
    for i in range(1, num+1):
        
        x, y = randWalk(start, length, stddev, avg)

        l_label = "Walk " + str(i)
        plt.plot(x, y, label=l_label)
    
    plt.legend(loc="upper right")
    plt.title("Random Walk")
    plt.ylabel("Stock Price")
    plt.xlabel("Time")
    plt.show()
    
def getInput():
    
    start = float(input("Enter the starting price -> "))
    length = int(input("Enter the length of simulation -> "))
    stddev = float(input("Enter the standard dev. -> "))
    # Assume average of 0
    avg = 0
    #avg = float(input("Enter the average -> "))
    
    return start, length, stddev, avg

def main():
  
    start, length, stddev, avg = getInput()
    
    plotWalks(5, start, length, stddev, avg)
    
if __name__ == "__main__":
  main()
