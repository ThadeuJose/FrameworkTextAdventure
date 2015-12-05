from unittest import TestCase

from Framework.Item import Item

__author__ = 'Thadeu Jose'


class TestItem(TestCase):
  def test_equal(self):
    item1 = Item('Test1','test')
    item2 = Item('Test2','test')
    self.assertIsNot(item1,item2)