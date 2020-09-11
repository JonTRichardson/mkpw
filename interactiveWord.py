import mkpw
import random

class interactiveWord(mkpw.MkPw):
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
        self.nWords = self.nWords + 1
        return choice

