# ## You’ve been hired as a lead programmer at a restraunt and are respnsible for keeping things organized.

# Create menu class
class Menu:
  # Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time)
  # Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items.Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

# Create our first menu: brunch. Brunch is served from 11am to 4pm. Note: set times in military time.
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

# Create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. Note: set times in military time.
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

# Create our third menu, dinner. Dinner is served from 5pm to 11pm. Note: set times in military time.
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

# Create our last menu, kids. The kids menu is available from 11am until 9pm. Note: set times in military time.
kid_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids_menu = Menu('Kids', kid_items, 1100, 2100)


# # What if there is a decision to create more than one restaurant?

# Create a Franchise class. Note: Could ceate before or after Menu class to make code look cleaner.
class Franchise:
  # Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # Give the Franchises a string representation so that we’ll be able to tell them apart. Should tell the address of the restaurant if a Franchise is printed.
  def __repr__(self):
    return self.address
  # tell our customers what they can order! Give Franchise an .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# Create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# # What if we decide to diversify by creating a restraunt that sells arepas?

# Create a Business class. Note: Could ceate next to Menu class and/or Franchise class to make code look cleaner.
class Business:
  # Give Business a constructor. A Business needs a name and a list of franchises.
  def __init__(self, name, franchise):
    self.name = name
    self.franchise = franchise
# create our first Business. The name is "Max Heart" and the two franchises are flagship_store and new_installment.
basta = Business("Max Heart", [flagship_store,new_installment])

# Create arepa items and menu
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

# Create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". Save the Franchise object to a variable called arepas_place.
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Make our new Business! The business is called "Take a' Arepa"!
arepa = Business("Take a' Arepa", [arepas_place])

# Test print
print(arepa.franchise[0].menus[0])

# Output: Take a' Arepa menu available from 1000 to 2000