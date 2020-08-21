import mkpw
import random

##########################
#  Arguments
import argparse
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument( "filename", type=str )
arguments = argumentParser.parse_args()

class myPw(mkpw.MkPw):
    """ Derived from MkPw, allows user to choose from random set of words. """

    def getRandomWord(self, seed="" ):
        if (seed == "" ):
            input( "press enter to generate a random word" )
            random.seed()
        else:
            random.seed( seed )
        response = "n"
        while (response != "y"):
            choice = random.choice( self.wordList )
            print("Chosen word is ", choice)
            response = input("Is that ok(y/n?")
            print("response is ", response)
        return choice


##############################
#  Main
print("penpw.py:main")
po = myPw( arguments.filename )

print("penpw.py:calling po.genPW()")
pw = po.genPW()

print("Password:", pw)


#TODO: A very long word could result in out-of-bounds reference.
#TODO: Some authentication systems are restricted in which special characters they take.
#TODO: Words currently come out all lower case.  Consider ways to get more complexity.

