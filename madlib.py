# make a madlib
# ask for three words:
    # noun
    # adjective
    # adverb
# fill in the mad lib
# print it out

def noun():
    """ Prompts and recieves a noun as input from user. Returns input as value of function"""
    print('First we need a NOUN')
    return input('> ')

def adjective():
    """ Prompts and recieves an adjective as input from user. Returns input as value of function"""
    print('Next we need ADJECTIVE')
    return input('> ')

def adverb():
    """ Prompts and recieves an adverb as input from user. Returns input as value of function"""
    print('Finally, give us an ADVERB')
    return input('> ')

# variables to store the user input

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
