class Bicycle:
    def __init__(self,name,weight,cost):
        self.name=name
        self.weight=float(weight)
        self.cost = float(cost)
    
class Bike_Shops:
    def __init__(self,name):
        self.name = name
        
    def Inventory(self,bike):
        self.inventory_list = list()
        self.inventory_list.append(bike)
        
        
    def Markup(self,markup):
        for bike in self.Inventory.inventory_list:
            self.markup = markup
            bike.cost * markup
        
    def Profit(self,profit):
        for Bike in self.Inventory.inventory_list:
            Bike_Shops.Markup - Bike.Cost

class Customer:
    def __init__(self,name):
        self.name=name
    
    def Fund(self,fund):
        self.fund = float(fund)
        
    def Buy(self, buy):
        Bought = []
        Bought.append(self.Buy)
        self.buy = buy
        self.fund -= Bike_Shops.Markup
        
Speeder = Bicycle("Speeder",45,245)
Fireball = Bicycle("Fireball",49,139)
Death = Bicycle("Death",70,400)
Skull = Bicycle("Skull",43,122)
Vishnu = Bicycle("Vishnu",12,421)
Heracles = Bicycle("Heracles",0.1,1000)


Warner = Bike_Shops("Warner") 

Warner.Inventory(Speeder)
Warner.Inventory(Fireball)
Warner.Inventory(Death)
Warner.Inventory(Heracles)
Warner.Inventory(Skull)
Warner.Inventory(Vishnu)


for items in Warner.inventory_list:
    print items.name
