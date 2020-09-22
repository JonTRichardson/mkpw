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
po = interactiveWord.interactiveWord( arguments.filename )

pw = po.genPW()

print("Password:", pw)

print("Stats:", po.getStats() );

