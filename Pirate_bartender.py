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

Tastes = { }

def pirate ():
    """I will ask what drinks you like"""
    Tastes.update(ingredients)
    
    print "I'm a {}, I will ask you what you like".format(pirate.__name__)
    Strong = raw_input(questions["strong"])
    if Strong == "yes" or Strong == "y":
        L_Strong=True
    else:
        L_Strong = False
    if L_Strong == False:
       del Tastes["strong"]
    
    Salty = raw_input(questions["salty"])
    if Salty == "yes" or Salty == "y":
        L_Salty=True
    else:
        L_Salty = False
    if L_Salty == False:
        del Tastes["salty"]
    
    Bitter = raw_input(questions["bitter"])
    if Bitter == "yes" or Bitter == "y":
        L_Bitter=True
    else:
        L_Bitter = False
    if L_Bitter == False:
        del Tastes["bitter"]
   
    Sweet = raw_input(questions["sweet"])
    if Sweet == "yes" or Sweet == "y":
        L_Sweet=True
    else:
        L_Sweet = False
    if L_Sweet == False:
        del Tastes["sweet"]
    
        
    Fruity = raw_input(questions["fruity"])
    if Fruity == "yes" or Fruity == "y":
        L_Fruity=True
    else:
        L_Fruity = False
    if L_Fruity == False:
        del Tastes["fruity"]
    
    return Tastes
    
    
import random
    
Drink = []

def drink():
    print "Yarr now we will see what {} I can scavenge up from the poop deck, land lubber".format(drink.__name__)
    
    
    if "strong" in Tastes == True:
        for strong in Tastes:
            Drink.append(strong)
            print strong
    if "salty" in Tastes == True:
        Salt = random.choice(Tastes)
        print Salt
        Drink.append(Salt)
    if "bitter" in Tastes == True:
        Bitt = random.choice("bitter")
        print Bitt
        Drink.append(Bitt)
    if "sweet" in Tastes == True:
        Swe = random.choice("sweet")
        print Swe
        Drink.append(Swe)
    if "fruity" in Tastes == True:
        Fru = random.choice("fruity")
        print Fru
        Drink.append(Fru)
    
    print random.choice(Drink)
    
    

if __name__ == '__main__':
    pirate()
    drink()
    