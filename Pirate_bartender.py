import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "apple on top"]
}

Drink = []
Tastes = { }
Prefer = [ ]
def pirate ():
    """I will ask what drinks you like"""
    
    print "I'm a {}, I will ask you what you like".format(pirate.__name__)
   
    for taste in questions:
        print questions[taste]
        x =raw_input().lower()
        if x == "y" or x == "yes":
            Prefer.append(taste)
        print Prefer


def drink():
    print "Yarr now we will see what {} I can scavenge up from the poop deck, land lubber".format(drink.__name__)
    for taste in Prefer:
        Drink.append(random.choice(ingredients[taste]))
    print "Here it is ye scally wag"
    for ingred in Drink:
        print "A {}".format(ingred)
    

if __name__ == '__main__':
    pirate()
    drink()
    