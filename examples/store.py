import sys

from department import Department
from product import Product
from user import User

class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    
    def print_departments(self):
      for id in self.departments:
        print(self.departments[id])
      print()
    
    def __str__(self):
      return f"Welcome to the Quarantine Store! Have a nice shopping experience!"



  




