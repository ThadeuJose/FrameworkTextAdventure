from unittest import TestCase
from Framework.Direction import directions,oppositeDirection

__author__ = 'Thadeu Jose'


class TestDirection(TestCase):
  def test_oppositeDirection(self):
    self.assertEqual(oppositeDirection('North'),'south')
    self.assertEqual(oppositeDirection('South'),'north')
    self.assertEqual(oppositeDirection('East'),'west')
    self.assertEqual(oppositeDirection('West'),'east')

  def test_in(self):
    self.assertFalse('As' in directions)
    self.assertTrue('north' in directions)
    self.assertTrue('south' in directions)
    self.assertTrue('east' in directions)
    self.assertTrue('west' in directions)