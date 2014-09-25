__author__ = 'GD020348'
import random

def main():
    thefile = "input.txt"
    # thefile = input("What's the name of the file?")
    inputfile = open(thefile)
    lines = inputfile.readlines()
    word = ""

    # First, grab out individual lines in the input file
    for line in lines:
        # Make a list variable out of each character on the current line
        # and assign it to the charactrs variable
        words = line.split()
        #print(words)
        for word in words:

    inputfile.close()

main()