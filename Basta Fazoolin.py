from datetime import datetime, time

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.start = start_time
    self.end = end_time
    self.start_t = time(start_time)
    self.end_t = time(end_time)
    self.items = items

  def __repr__(self):
    return "{menu} menu available from {start} to {end}".format(menu=self.name,start=self.start_t.strftime("%H%p"),end=self.end_t.strftime("%H%p"))

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

#creating brunch menu
brunch = Menu("Brunch", {
'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

#creating early bird menu
early_bird = Menu("Early Bird", {
'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

#creating dinner menu
dinner = Menu("Dinner", {
'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17,23)

#creating kids menu
kids = Menu("Kids", {
'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

#creating arepa menu
arepas_menu = Menu("Take a’ Arepa", {
'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)


#testing if kids menu works
print(kids)

#We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price. Example order: 
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

#testing other example order
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#creating franchise class
class Franchise: 
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address
#checking avail menus at certain time input
  def available_menus(self,time):
    lst_of_menus = []
    for menu in self.menus:
      if menu.start < time and menu.end > time:
        lst_of_menus.append(menu.name)
    return lst_of_menus

#setting up franchises
flagship_store = Franchise("232 West End Road",[brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street",[brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#testing classes, avail menus
print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

class Business:
  def __init__(self, name, franchises):
    pass

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
second_business = Business("Take a' Arepa", [arepas_place])



