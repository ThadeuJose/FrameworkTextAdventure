from unittest import TestCase
from Direction import Direction

__author__ = 'Thadeu Jose'


class TestDirection(TestCase):
  def test_oppositeDirection(self):
    direc = Direction()
    self.assertEqual(direc.oppositeDirection('North'),'south')
    self.assertEqual(direc.oppositeDirection('South'),'north')
    self.assertEqual(direc.oppositeDirection('East'),'west')
    self.assertEqual(direc.oppositeDirection('West'),'east')

  def test_in(self):
    direc = Direction()
    self.assertFalse('As' in direc)
    self.assertTrue('North' in direc)
    self.assertTrue('South' in direc)
    self.assertTrue('East' in direc)
    self.assertTrue('West' in direc)