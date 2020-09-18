import random
import unittest

class MkPw:
    """ Password maker base class """

    # Statistics:
    nDigits   = 0
    nLetterLC = 0
    nLetterUC = 0
    nSpecial  = 0
    nWords    = 0

    lastMethod = ''  # Previous chosen method

    def __init__(self, file):
        if (file == ""):
            wordFileName = "defaultWords.txt"
        else:
            wordFileName = file

        print( "wordFileName is ", wordFileName )

        with open( wordFileName ) as self.file:
            self.wordList = list(self.file.read().split())

    def resetStats(self):
        self.nDigits   = 0
        self.nLetterLC = 0
        self.nLetterUC = 0
        self.nSpecial  = 0
        self.nWords    = 0

    def getStats(self):
        return dict([ ( "nDigits",   self.nDigits   ),
                      ( "nLetterLC", self.nLetterLC ),
                      ( "nLetterUC", self.nLetterUC ),
                      ( "nSpecial",  self.nSpecial  ),
                      ( "nWords",    self.nWords    ) ])

    #######################################################################################
    ##   getRandomDigit()
    ##      Picks 1 random digit using the seed parameter.
    ##      With default, empty seed, requests input, then resets the seed.
    def getRandomDigit(self, seed=""):
        List = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
        if (seed == "" ):
            input( "press enter to generate a random digit" )
            random.seed()
        else:
            random.seed( seed )
        choice = random.choice(List)
        self.nDigits = self.nDigits + 1
        return choice

    #######################################################################################
    ##   getRandomLetterLC()
    ##      Picks 1 random lower-case letter using the seed parameter.
    ##      With default, empty seed, requests input, then resets the seed.
    def getRandomLetterLC(self, seed=""):
        List = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
        if (seed == "" ):
            input( "press enter to generate a random LC letter" )
            random.seed()
        else:
            random.seed( seed )
        choice = random.choice(List)
        self.nLetterLC = self.nLetterLC + 1
        return choice

    #######################################################################################
    ##   getRandomLetterUC()
    ##      Picks 1 random upper-case letter using the seed parameter.
    ##      With default, empty seed, requests input, then resets the seed.
    def getRandomLetterUC(self, seed=""):
        List = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
        if (seed == "" ):
            input( "press enter to generate a random UC letter" )
            random.seed()
        else:
            random.seed( seed )
        choice = random.choice(List)
        self.nLetterUC = self.nLetterUC + 1
        return choice

    #######################################################################################
    ##   getRandomSpecial()
    ##      Picks 1 random special character using the seed parameter.
    ##      With default, empty seed, requests input, then resets the seed.
    def getRandomSpecial(self, seed=""):
        List = [ '`', '-', '=', '[', ']', ';', "'", ',', '.', '/', '\\', '~', '!',
                 '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',  '{', '}',
                 '|', ':', '"', '<', '>', '?' ]
        if (seed == "" ):
            input( "press enter to generate a random special character" )
            random.seed()
        else:
            random.seed( seed )
        choice = random.choice(List)
        self.nSpecial = self.nSpecial + 1
        return choice


    #######################################################################################
    ##   getRandomWord()
    ##      Picks 1 random word using the seed parameter, chosen from the wordList member.
    ##      With default, empty seed, requests input, then resets the seed.
    def getRandomWord(self, seed="" ):
        if (seed == "" ):
            input( "press enter to generate a random word" )
            random.seed()
        else:
            random.seed( seed )
        choice = random.choice( self.wordList )
        self.nWords = self.nWords + 1
        return choice

    #######################################################################################
    ##   chooseMethod()
    ##       Picks which class of character(s) to use for the next part of the password.
    ##       Override this method if you want a different way of mixing component types.
    def chooseMethod(self):
        methods = [ self.getRandomDigit, self.getRandomLetterLC, self.getRandomLetterUC,
                    self.getRandomSpecial, self.getRandomWord ]
        input( "Press <enter> to choose next method" )
        random.seed()
        chosenMethod = random.choice(methods)
        self.lastMethod = chosenMethod
        return chosenMethod

    #######################################################################################
    ##   getLengthIncrement()
    ##       Determine how much to add to the target length based on length of a word
    ##       component.  We add to the lengh because a familiar word makes it easier to
    ##       remember & enter so a longer password is tolerable; furthermore, a word
    ##       provides less entropy than a string of random letters of similar length.
    def getLengthIncrement(self, word):
        wordLengthIncrement = [0, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7]
        if len(word) < len(wordLengthIncrement):
            return wordLengthIncrement[ len(word) ]
        else:
            # word too long.  Return the last value in the array plus the additional
            # length of the word beyond the end of the array.
            return ( wordLengthIncrement[-1] + len(word) - (len(wordLengthIncrement)-1) )

    #######################################################################################
    ##   genPW()
    ##      Generates a password composed of characters from the different
    ##      components (digits, words etc).  Picks a target password length and continues
    ##      to add characters until the target is met.  If a word is chosen, then some
    ##      length is added to the target.
    def genPW(self):

        pw = ""
        targetLength = 12
        self.resetStats()

        while len(pw) < targetLength:
            chosenMethod = self.chooseMethod()
            if chosenMethod==self.getRandomWord:
                print( "method was getRandomWord" )
                word = chosenMethod()
                print( "word is:", word )
                pw += word
                targetLength += self.getLengthIncrement( word )
                print( "New targetLength:", targetLength )
            else:
                pw += chosenMethod()

        return pw


import string

if __name__ == '__main__':
    class TestMkPw( unittest.TestCase ):
        """ TestMkPw: unit tester for the MkPw class -- calls methods and verifies results """
        x = MkPw("")
        y = MkPw("testWords.txt")

        def testGetLengthIncrement(self):
            word = '123'
            self.assertEqual( 1, self.x.getLengthIncrement(word) )
            word = '123456789'
            self.assertEqual( 6, self.x.getLengthIncrement(word) )
            word = '1234567890'
            self.assertEqual( 7, self.x.getLengthIncrement(word) )
            word = '12345678901'
            self.assertEqual( 8, self.x.getLengthIncrement(word) )
            word = '123456789012'
            self.assertEqual( 9, self.x.getLengthIncrement(word) )
            word = '1234567890123456789012345678901234567890'
            self.assertEqual( 37, self.x.getLengthIncrement(word) )

        def testDigit(self):
            for seed in range( 1000 ):
                d = self.x.getRandomDigit( seed )
                self.assertTrue( d in string.digits )
    
        def testLower(self):
            for seed in range( 1000 ):
                a = self.x.getRandomLetterLC( seed )
                self.assertTrue( a in string.ascii_lowercase )
    
        def testUpper(self):
            for seed in range( 1000 ):
                a = self.x.getRandomLetterUC( seed )
                self.assertTrue( a in string.ascii_uppercase )
    
        def testSpecial(self):
            for seed in range( 1000 ):
                a = self.x.getRandomSpecial( seed )
                self.assertTrue( a in string.punctuation )
    
        def testWord(self):
            for seed in range( 1000 ):
                word = self.x.getRandomWord( seed )
                self.assertTrue( len(word)>=2 and len(word)<10 )
    
                for c in word:
                    self.assertTrue( c in string.ascii_lowercase )
    
        def testWord2(self):
            for seed in range( 1000 ):
                word = self.y.getRandomWord( seed )
                self.assertTrue( len(word)>=2 and len(word)<17 )
    
                for c in word:
                    self.assertTrue( c in string.ascii_lowercase or c=='-', word )
    
    print( TestMkPw.__doc__ )
    print( 'Testing MkPw ...' )
    print( MkPw.__doc__ )
    unittest.main()

