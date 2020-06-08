# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:45:09 2018

@author: kinse
"""

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random


# Creating arrays for each number where 1=white pixel and -1=black pixel
one = np.ones((7,7), dtype=int, order='C')
one[3,[3]] = [-1]

two = np.ones((7,7), dtype=int, order='C')
two[2,[2]] = [-1]
two[4,[4]] = [-1]

three = np.ones((7,7), dtype=int, order='C')
three[1,[1]] = [-1]
three[3,[3]] = [-1]
three[5,[5]] = [-1]

four = np.ones((7,7), dtype=int, order='C')
four[1,[1]] = [-1]
four[5,[5]] = [-1]
four[1,[5]] = [-1]
four[5,[1]] = [-1]

five = np.ones((7,7), dtype=int, order='C')
five[1,[1]] = [-1]
five[1,[5]] = [-1]
five[3,[3]] = [-1]
five[5,[1]] = [-1]
five[5,[5]] = [-1]

six = np.ones((7,7), dtype=int, order='C')
six[1,[1]] = [-1]
six[1,[5]] = [-1]
six[3,[1]] = [-1]
six[3,[5]] = [-1]
six[5,[1]] = [-1]
six[5,[5]] = [-1]

# Here is a function that prints a black and white image
def arrayPlot(data):
   
    fig, ax = plt.subplots()
    ax.imshow(data, cmap='gray', interpolation='none')

    # Set the major ticks at the centers and minor tick at the edges
    locs = np.arange(len(data))
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_ticks(locs + 0.5, minor=True)
        axis.set(ticks=locs, ticklabels=[])

    # Turn on the grid for the minor ticks
    ax.grid(False, which='minor', linestyle='-')
    plt.show()


# Assign the arrays to variables
Roll_one = one
Roll_two = two
Roll_three = three
Roll_four = four
Roll_five = five
Roll_six = six

# Create a list of possible variables
Possible_Rolls = [Roll_one, Roll_two, Roll_three, Roll_four, Roll_five, Roll_six]


# Randomly plot one of the variables
x = random.choice(Possible_Rolls)
Empty_List = []
Empty_List.append(x)
arrayPlot(x)
