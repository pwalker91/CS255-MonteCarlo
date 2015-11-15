#!/usr/local/bin/python3
"""
solovay_strassen.py
AUTHOR:     Peter Walker
DATE:       08 November 2015
ABSTRACT:
    This file is an implementation of the Solovay/Strassen Algorithm for
    determining if a number is prime.
    I will also attempt to make some improvements to the efficiency of the
    algorithm using ___.
"""

import sys
import math
import random
import warnings


def _run(P, accuracy=90):
    """
    Using _test(), this determines if the given value, P, is a prime number
    INPUTS:
        P : Integer, the value we are testing
        accuracy : Number, the percent certainty that the number should be prime
    RETURNS:
        True : P is prime with accuracy 'accuracy'
        False : P is not prime
    """
    #For every random number we select that returns 1, the probability that P is
    # prime is 1 - 1/2^(iterations). So, given the accuracy passed, we can deduce
    # how many iterations we need.
    NUMITERS = math.ceil( math.log(1-(accuracy/100.0), 0.5) )
    USED = []
    CT = 0
    #For each iteration, we pick a random number that has not already been
    # used, and pass it to the _test() function. If the value returned is not 1,
    # then the number is not prime
    while (CT < NUMITERS):
        NEWRAND = random.randint(2, P)
        while (NEWRAND in USED):
            NEWRAND = random.randint(2, P)
        USED.append(NEWRAND)
        RES = pow(USED[-1], int((P-1)/2), P)

        print(USED[-1], P, RES)

        CT+=1
    #END WHILE
    return True
#END DEF


def _run_i(P, accuracy=90):
    """
    Using _test(), this determines if the given value, P, is a prime number. This
      is an 'improved' version of the original algorithm
    INPUTS:
        P : Integer, the value we are testing
        accuracy : Number, the percent certainty that the number should be prime
    RETURNS:
        True : P is prime with accuracy 'accuracy'
        False : P is not prime
    """
    return False
#END DEF




def __printh():
    """Printing the help text"""
    print("SOLOVAY-STRASSEN ALGORITHM:")
    print("USAGE: FILE.py [-oeh] NUMBER [ACCURACY]")
    print("  NUMBER : Value you want to test for primeness")
    print("  -o : Test using original Solovay/Strassen algorithm. Default option")
    print("  -i : Test using 'improved' algorithm")
    print("  ACCURACY : Percent accuracy of primeness. Default 90")
    print("  -h : help screen")
    print("EXAMPLE: python3 solovay_strassen.py -o 173 95")
#END DEF


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("ERROR: Please provide some command arguements.")
        __printh()
        return

    sys.argv = sys.argv[1:]
    if sys.argv[0] == '-h':
        __printh()
        return
    #Testing that the user has given one of the three flags
    if sys.argv[0] not in ["-o", "-i", "-h"]:
        sys.argv = ["-o"] + sys.argv

    #Testing that the second value is a number (our testee)
    if (len(sys.argv)<2) or not sys.argv[1].isdigit():
        print("ERROR: You must pass in a number to this program.")
        __printh()
        return
    #Since we know we have a number, casting the string to an int
    sys.argv[1] = int(sys.argv[1])

    #Making sure we have a percent on the end of our arguments
    if len(sys.argv) < 3:
        sys.argv.append(90)
    elif not sys.argv[2].isdigit():
        print("ERROR: Please pass in a percent certainty for primeness.")
        __printh()
        return
    elif sys.argv[2] < 1 or sys.argv[2] >= 100:
        print("ERROR: Please provide a percentage between 1 and 100.")
        __printh()
        return
    #Since we know we have a number between 1 and 100, cast to float
    sys.argv[2] = float(sys.argv[2])


    #Now that we've done our tests, calling the appropiate _run() function based
    # on the given flag
    if sys.argv[0] == "-o":
        isPrime = _run(sys.argv[1], sys.argv[2])
    elif sys.argv[0] == "-i":
        isPrime = _run_i(sys.argv[1], sys.argv[2])
    else:
        print("ERROR: Something went wrong. How did you get here?")
        __printh()
        return

    if (isPrime):
        print(str(sys.argv[1])+" is prime with at least "+str(sys.argv[2])+"% certainty.")
    else:
        print(str(sys.argv[1])+" is NOT prime.")
#END DEF


main()

#END OF LINE
