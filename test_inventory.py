from unittest import TestCase
from Inventory import Inventory
from Item import Item
from Local import Local
from FrameworkException import *

__author__ = 'Thadeu Jose'

class TestInventory(TestCase):

  def test_addItem(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.addItem(item1)
    self.assertTrue(item1 in inventory)
    inventory.addItem(item2)
    self.assertTrue(item1 in inventory)
    self.assertTrue(item2 in inventory)

  def test_removeItem(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    item3 = Item('Test3','Test')
    inventory.addItem(item1)
    inventory.addItem(item2)
    inventory.addItem(item3)
    inventory.removeItem(item2)
    self.assertNotIn(item2,inventory)

  def test_removeItem_ItemException(self):
    inventory = Inventory()
    local = Local('Test1','Test')
    with self.assertRaises(ItemException):
      inventory.addItem(local)

  def test_removeItem_EmptyInventoryException(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    with self.assertRaises(EmptyInventoryException):
      inventory.removeItem(item1)

  def test_removeItem_ItemNotFoundException(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.addItem(item1)
    with self.assertRaises(ItemNotFoundException):
      inventory.removeItem(item2)

  def test_print(self):
    inventory = Inventory()
    inventory.addItem(Item('Test1','Test'))
    inventory.addItem(Item('Test2','Test'))
    inventory.addItem(Item('Test2','Test'))
    inventory.addItem(Item('Test2','Test'))
    resp = str(inventory)
    self.assertEqual(resp,'Test1x1,Test2x3')
