from unittest import TestCase

from Framework.Exceptions import EmptyStringException
from Framework.BaseTextObject import TextObject

__author__ = 'Thadeu Jose'


class TestTextObject(TestCase):
  def test_init_name(self):
    with self.assertRaises(EmptyStringException):
      textObject = TextObject("","Test")

  def test_init_name(self):
    with self.assertRaises(EmptyStringException):
      textObject = TextObject("Test","")

  def test_name_setter(self):
    textObject = TextObject("Test","Test")
    with self.assertRaises(EmptyStringException):
      textObject.name=""

  def test_description_setter_Empty_String(self):
    textObject = TextObject("Test","Test")
    with self.assertRaises(EmptyStringException):
      textObject.description=""

  def test_description_setter(self):
    textObject = TextObject("Test", "Test")
    textObject.description = "None"
    self.assertEqual(textObject.description, "None")
