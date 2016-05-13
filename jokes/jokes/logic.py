joke_list = []

class Joke:
    """docstring for Joke"""
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

def save_joke_obj(setup, punchline):
    new_joke = Joke(setup, punchline)
    joke_list.append(new_joke)

def return_humor():
    return joke_list
