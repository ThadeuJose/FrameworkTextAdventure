from unittest import TestCase

from Framework.Controller import Controller
from Framework.Inventory import Inventory
from Framework.Item import Item
from Framework.Local import Local
from Framework.Exceptions import *

__author__ = 'Thadeu Jose'


class TestInventory(TestCase):
  #todo Testar Take
  def test_addItem(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.add(item1)
    self.assertTrue(item1 in inventory)
    inventory.add(item2)
    self.assertTrue(item1 in inventory)
    self.assertTrue(item2 in inventory)

  def test_contain_item_class(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.add(item1)
    inventory.add(item2)
    self.assertIn(item1, inventory)

  def test_contain_string(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    inventory.add(item1)
    inventory.add(item2)
    self.assertIn('Test1', inventory)

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

  def test_removeItem_2(self):
    inventory = Inventory()
    item1 = Item('Test1','Test')
    item2 = Item('Test2','Test')
    item3 = Item('Test3','Test')
    inventory.add(item1)
    inventory.add(item2)
    inventory.add(item3)
    inventory.remove('Test2')
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

  def test_str(self):
    inventory = Inventory()
    inventory.add(Item('Test1','Test'))
    inventory.add(Item('Test2','Test'))
    inventory.add(Item('Test2','Test'))
    inventory.add(Item('Test2','Test'))
    resp = str(inventory)
    self.assertEqual(resp,'Test1, Test2 x 3')

  def test_inter_(self):
    inventory = Inventory()
    inventory.add(Item('Test1','Test'))
    inventory.add(Item('Test2','Test'))
    inventory.add(Item('Test3','Test'))
    resp = list()
    for i in inventory:
      resp.append(i.name)
    self.assertEqual(" ".join(resp),"Test1 Test2 Test3")