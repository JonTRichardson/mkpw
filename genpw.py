# genpw.py
#   The main for the password generator.  
#   Processes command line arguments and invokes the password generating object.

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

