__author__ = 'GD020348'
import random


def main():
    thefile = "input.txt"
    # thefile = input("What's the name of the file?")
    inputfile = open(thefile)
    lines = inputfile.readlines()
    word = ""
    output = []

    # First, grab out individual lines in the input file
    for line in lines:
        # Make a list variable out of each character on the current line
        # and assign it to the charactrs variable
        characters = list(line)
        # Parse through each character in the characters variable
        for character in characters:
            # See if that character is a space, which will signal
            # that it's a new word
            if character != " ":
                # Add the non-space character to the current word
                word = word + character
            else:
                firstchar = word[0]
                lastchar = word[-1]
                mid = word[1:-1]
                final = ""
                middle = random.sample(mid, len(mid))
                for x in middle:
                    final = final + x
                #print(middle)
                #print(word[0] + word[1:-1].shuffle())
                #print(word[0]+final+word[-1])
                output += word[0]+final+word[-1]
                word = ""
        #print(final)
    print(output)
    inputfile.close()

main()