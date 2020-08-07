# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []
  
  def __str__(self):
    return f"Your items: {self.items}"

  def move(self, direction):
    directions = ['n', 's', 'w', 'e']
    if direction not in directions:
      next_direction = input('Please enter a valid direction [`n`, `s`, `w`, `e`]')
      self.move(next_direction)

  def retrieve(self, item):
    self.items.append(item)
    self.print_items()
  
  def print_items(self):
    print("Your items: ", [f"{item.name}" for item in self.items], '\n')