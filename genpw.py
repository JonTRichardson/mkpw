#import mkpw
import interactiveWord
import random

##########################
#  Arguments
import argparse
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument( "filename", type=str )
arguments = argumentParser.parse_args()

##############################
#  Main
print("penpw.py:main")
po = interactiveWord.interactiveWord( arguments.filename )

print("penpw.py:calling po.genPW()")
pw = po.genPW()

print("Password:", pw)

print("Stats:", po.getStats() );

