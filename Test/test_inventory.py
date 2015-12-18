from unittest import TestCase

from Framework.Controller import Controller
from Framework.Inventory import Inventory
from Framework.Item import Item
from Framework.Local import Local
from Framework.Exceptions import *

__author__ = 'Thadeu Jose'


class TestInventory(TestCase):
  #TODO testar contain
  def test_addItem(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.add(item1)
    self.assertTrue(item1 in inventory)
    inventory.add(item2)
    self.assertTrue(item1 in inventory)
    self.assertTrue(item2 in inventory)

  def test_removeItem(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    item3 = Item('Test3','Test')
    inventory.add(item1)
    inventory.add(item2)
    inventory.add(item3)
    inventory.remove(item2)
    self.assertNotIn(item2,inventory)

  def test_removeItem_ItemException(self):
    inventory = Inventory()
    local = Local('Test1','Test',Controller)
    with self.assertRaises(ItemException):
      inventory.add(local)

  def test_removeItem_EmptyInventoryException(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    with self.assertRaises(EmptyInventoryException):
      inventory.remove(item1)

  def test_removeItem_ItemNotFoundException(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.add(item1)
    with self.assertRaises(ItemNotFoundException):
      inventory.remove(item2)

  def test_print(self):
    inventory = Inventory()
    inventory.add(Item('Test1','Test'))
    inventory.add(Item('Test2','Test'))
    inventory.add(Item('Test2','Test'))
    inventory.add(Item('Test2','Test'))
    resp = str(inventory)
    self.assertEqual(resp,'Test1x1,Test2x3')
