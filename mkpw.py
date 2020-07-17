import random
import unittest

class MkPw:
    """ WIP Password maker.  Caveat: This doesn't fully address the cryptographic security of the RNG. """
    """ For now, asks the user to press enter.  My assumption is that this will set the RNG seed to    """
    """ something truly random because it is dependent on user input.  """
    wordList = []

    def getRandomDigit(self):
        List = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
        input( "press enter to generate a random digit" )
        random.seed()
        choice = random.choice(List)
        return choice

    def getRandomLetterLC(self):
        List = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s','t','u','v','w','x','y','z' ]
        input( "press enter to generate a random LC letter" )
        random.seed()
        choice = random.choice(List)
        return choice

    def getRandomLetterUC(self):
        List = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T','U','V','W','X','Y','Z' ]
        input( "press enter to generate a random UC letter" )
        random.seed()
        choice = random.choice(List)
        return choice

    ########################################################################################################################
    ##   getRandomWord()
    ##      For now, uses default word file.  This is for dev only.  I wouldn't recommend actually using this file.
    def getRandomWord(self):
        if ( self.wordList == [] ):
            with open('defaultWords.txt') as file:
                wordList = list(file.read().split())

        input( "press enter to generate a random word" )
        random.seed()
        choice = random.choice( wordList )
        return choice


import string

class TestMkPw( unittest.TestCase ):
    x = MkPw()

    def testDigit(self):
        d = self.x.getRandomDigit()
        self.assertTrue( d in string.digits )

    def testLower(self):
        a = self.x.getRandomLetterLC()
        self.assertTrue( a in string.ascii_lowercase )

    def testUpper(self):
        a = self.x.getRandomLetterUC()
        self.assertTrue( a in string.ascii_uppercase )

    def testWord(self):
        word = self.x.getRandomWord()
        self.assertTrue( len(word)>=2 and len(word)<8 )

        for c in word:
            self.assertTrue( c in string.ascii_lowercase )

    
if __name__ == '__main__':
    print( 'Testing MkPw ...' )
    print( MkPw.__doc__ )
    unittest.main()

