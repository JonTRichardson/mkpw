import mkpw
import random

po = mkpw.MkPw( "" )

methods = [ po.getRandomDigit, po.getRandomLetterLC, po.getRandomLetterUC, po.getRandomSpecial, po.getRandomWord ]

pw = ""
targetLength = 12
wordLengthIncrement = [0, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9] 

while len(pw) < targetLength:
    input( "Press <enter>" )
    random.seed()
    chosenMethod = random.choice(methods)
    print( chosenMethod )
    if chosenMethod==po.getRandomWord:
        print( "method was getRandomWord" )
        word = chosenMethod()
        print( "word is:", word )
        pw += word
        print( "Adding to length:", wordLengthIncrement[ len(word) ] )
        targetLength += wordLengthIncrement[ len(word) ] 
        print( "New targetLength:", targetLength )
    else:
        pw += chosenMethod()
    
print("Password:", pw)


#TODO: A very long word could result in out-of-bounds reference.
#TODO: Some authentication systems are restricted in which special characters they take.
#TODO: Words currently come out all lower case.  Consider ways to get more complexity.

