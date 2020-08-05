# mkpw
Experimental password generator

# Intro 
This project is a password generator.  I set out to do something useful, explore information, randomness and security and to have fun making something.

I can’t guarantee that you can use this to make passwords secure enough for your needs.  I like to think that I am clever and have given this some informed thought and considered other viewpoints.

This isn’t intended as a turnkey program.  The intent is for a user to customize it for their own needs.

In addition to this readme, I am working on another document delving into the issues and deeper into the thinking.

This is an actively evolving work in progress.  I’m figuring out what it will look like as I go.  

Passwords are a tradeoff between ease of recall and security.  My goal here is to provide building blocks by which a user could choose their own tradeoffs between this ease and security.  See https://xkcd.com/2176/ & https://xkcd.com/936/.

# About the implementation
The base class provides random characters in different classes (number, upper-case etc).  This is to help support a common requirement that passwords contain at least one of each of these.

It also includes a way to read a dictionary and pick a random word in that dictionary.  The default dictionary that I include is not suitable for generation of passwords – it is much too small and too predictable for good passwords.  I don’t include a dictionary that I would recommend because the idea is that each individual should provide their own.  See the section below about using random words in passwords.

# The pros and cons of dictionary words
Using known words as part of a password helps with one end of the trade-off (human ability to remember it) but can, if not done intelligently, seriously compromise security, the other side of the tradeoff.  I don’t want to be complacent in thinking that I’ve figured out how to be intelligent with them, but my strategy is to allow a PW with words to be longer than one without words.  I can easily manage a 30-character password composed of a few words, but would be hard-pressed to remember a 10-character PW with each character being an independent random variable.  So, my initial implementation will increase the length of the password if a word is selected from a dictionary. 

# Random Number Generators
The issue of using RNG’s for security applications is a bigger one than I fully wish to take on.  My design is to rely on user interaction to provide what is essentially real randomness.  I considered using /dev/random or /dev/urandom, but hesitated and then ruled it out in case I want this to run in a non-linux environment.  I also considered a way to generate my own randomness pool.  That might be an interesting project of its own, but relying on user interaction works fine, since this is meant to be an interactive program.  Before generating a random number, the code waits for a user to hit <enter>, then sets a new seed before calling the function.  This is a possible Achilles heal – if the python documentation, or my understanding of it, is incorrect, then it might introduce a vulnerability into the result.
  
To facilitate automated testing and other batch investigations, there is a defaulted argument which allows overriding the user interaction.

# The real solution to this problem
*	Use 2-Factor-Authentication where practical
*	Use password manager software
*	Record the passwords in some way that you can access them.  Keep them in a place where you trust that others won’t access them.  If there is no such place, then keep it on your person or encrypt it.  You can keep them written in a notebook somewhere that is physically secure or you can keep it electronically secure.
*	Don’t use the supposedly clever tricks to come up with passwords that you can remember (e.g. substituting ‘1’ for ‘I’).

# The (not-quite-abstract) base class
I’m providing a base class, which I intend for a user to override with their own tailoring.  I didn’t make it abstract, for one because I haven’t figured out how to do that in python, or if it can be done in python.  Second, I want to have unit tests for the methods and I don’t want to deal with the inconvenience of abstractness.  These decisions may change as this evolves.

# Top-level generator
The top-level generator randomly chooses methods and calls the methods to do their random thing.  This generator has a sense of the “quality of the password” that it is seeking.  “Quality” has different measures.  As I write this, password length is the only measure that I have implement with some adjustment based on what has gone into the pw so far (increasing the target length when a word is chosen from the word list).  The intent is for there to be additional quality measures (e.g. forcing there to be a number, upper, lower etc).
