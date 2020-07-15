import random
import unittest

class MkPw:
    """ WIP Password maker.  Caveat: This doesn't fully address the cryptographic security of the RNG."""

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


import string

class TestMkPw( unittest.TestCase ):
    x = MkPw()

    def test1(self):
        d = self.x.getRandomDigit()
        self.assertTrue( d in string.digits )

    def test2(self):
        a = self.x.getRandomLetterLC()
        self.assertTrue( a in string.ascii_lowercase )

    def test3(self):
        a = self.x.getRandomLetterUC()
        self.assertTrue( a in string.ascii_uppercase )



    
if __name__ == '__main__':
    print( 'Testing MkPw ...' )
    print( MkPw.__doc__ )
    unittest.main()

