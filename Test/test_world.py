from unittest import TestCase
from Framework.Exceptions import LocalNotImplementException,IncorrectTypeException
from Framework.World import World
from Framework.Local import Local

__author__ = 'Thadeu Jose'


class TestWorld(TestCase):

  def test_addLocal_IncorrectTypeException(self):
    world = World()
    with self.assertRaises(IncorrectTypeException):
      world.addLocal("Teste")

  def test_addLocal_sucessful(self):
    world = World()
    world.addLocal(Local("Teste1","Teste"))
    local = world.getlocal("Teste1")
    self.assertEqual(local,Local("Teste1","Teste"))

  def test_getLocal_LocalNotImplementException(self):
    world = World()
    world.addLocal(Local("Teste1","Teste"))
    with self.assertRaises(LocalNotImplementException):
      world.getlocal("Teste")
