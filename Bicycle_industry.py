class Bicycle(object):

    def __init__(self,name,weight,cost, number):
        self.name=name
        self.weight=float(weight)
        self.cost = float(cost)
        self.number = int(number)
        self.markup = self.cost * markup
        self.profit = self.markup-self.cost
       
       
class Bike_Shops(object):
    def __init__(self, name):
        self.name = name
        self.inventory_list = list()
        self.Bikes_sold = list()
        self.running_profit = 0
    
    def Inventory(self,bike):
        self.inventory_list.append(bike)
    
    def SellBike(self,bike):
        self.Bikes_sold.append(bike)
        
    def Markup(self,markup):
        for bike in self.inventory_list:
            bike.markup = bike, bike.cost * markup


class Customer(object):
    def __init__(self,name):
        self.name = name
        self.Bought = list()

    def Fund(self,fund):
        self.fund = float(fund)
        
    def Buy(self, bike_shop, bike):
        self.Bought.append(self.Buy)
        self.fund -= bike.markup
        bike_shop.running_profit += bike.profit
        bike.number -= 1
        bike_shop.Bikes_sold.append(bike)


markup = 1.2
"""six different bikes"""        
Speeder = Bicycle("Speeder",45,245,5)
Fireball = Bicycle("Fireball",49,139,5)
Death = Bicycle("Death",70,400,5)
Skull = Bicycle("Skull",43,122,4)
Vishnu = Bicycle("Vishnu",12,421,3)
Heracles = Bicycle("Heracles",0.1,1000,1)

"""Warner's bikes and markup"""
Warner = Bike_Shops("Warner") 
Warner.Markup(1.2)
Warner.Inventory(Speeder)
Warner.Inventory(Fireball)
Warner.Inventory(Death)
Warner.Inventory(Skull)
Warner.Inventory(Vishnu)
Warner.Inventory(Heracles)

"""Customers and print names"""
Cust_list = list()
Jim = Customer("Jim")
Cust_list.append(Jim)
print Jim.name
James = Customer("James")
print James.name
Cust_list.append(James)
Jane = Customer("Jane")
print Jane.name
Cust_list.append(Jane)

"""Customers funds"""
Jim.fund = 200
James.fund = 500
Jane.fund = 1000


print "Jim can buy:"
Jim_pos = list()
for items in Warner.inventory_list:
    if items.markup < Jim.fund:
        print items.name
        Jim_pos.append(items)
    
print "James can buy:"
James_pos = list()
for items in Warner.inventory_list:
    if items.markup < James.fund:
        print items.name
        James_pos.append(items)
        
print "Jane can buy:"
Jane_pos = list()
for items in Warner.inventory_list:
    if items.markup < Jane.fund:
        print items.name
        Jane_pos.append(items)


"""initial inventory of the bike shop"""
for items in Warner.inventory_list:
    print items.name
    print items.number




    



Jim.Buy(Warner,Skull)
print "The bike Jim bought was {}".format(Skull.name)
print "The cost was {}".format(Skull.cost)
print "Jim has {} dollars left.".format(Jim.fund)

James.Buy(Warner,Speeder)
print "The bike James bought was {}".format(Speeder.name)
print "The cost was{}".format(Speeder.cost)
print "James has {} dollars left.".format(James.fund)   

Jane.Buy(Warner,Vishnu)
print "The bike Vishnu bought was {}".format(Vishnu.name)
print "The cost was {}".format(Vishnu.cost)
print "Jane has {} dollars left.".format(Jane.fund)

print "There are {} {}s left.".format(Skull.number,Skull.name)
print "There are {} {}s left.".format(Speeder.number,Speeder.name)
print "There are {} {}s left.".format(Vishnu.number,Vishnu.name)


print "The bike shop made {} dollars.".format(Warner.running_profit)