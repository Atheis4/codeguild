"""
5-16-16:

Considering creating lists of nouns, adjectives, adverbs, and verbs to be plugged into the madlib--or referenced by index--using a for loop.
"""

def noun():
    """ Prompts and recieves a noun as input from user. Returns input as value of function"""
    return input('First we need a NOUN\n> ')

def adjective():
    """ Prompts and recieves an adjective as input from user. Returns input as value of function"""
    return input('Next we need ADJECTIVE\n> ')

def adverb():
    """ Prompts and recieves an adverb as input from user. Returns input as value of function"""
    return input('Finally, give us an ADVERB\n> ')

def construct_madlib(noun, adverb, adject):
    """ Using the return variables from the functions noun, adjective, and adverb, add said variables to a complex-ish string to construct the madlib."""
    return noun + '\'s are very dangerous. When dealing with ' + noun + ' it is important to wait ' + adverb + '. If you don\'t, you will end up with ' + adject + ' hands.'

print('Hello USER')
print('Time for a MadLib, eh?')

noun = noun()
adject = adjective()
adverb = adverb()

madlib = construct_madlib(noun, adject, adverb)

print(madlib)
