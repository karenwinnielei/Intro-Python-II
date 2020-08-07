# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items=[]):
    self.name = name
    self.description = description
    self.items = items

  def get_item(self, item):
    del self.items[item]
  
  def add_item(self, item):
    if self.items:
      self.items.append(item)
    return self.items
  
  def __str__(self):
    return f'{self.name}: {self.description}'
  
  def print_item(self):
    for name, description in enumerate(self.items):
      print(f"{name}: {description}")
