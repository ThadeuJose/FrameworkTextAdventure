from unittest import TestCase
from FrameworkException import EmptyStringException
from BaseTextObject import TextObject
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

  def test_description__setter(self):
    textObject = TextObject("Test","Test")
    with self.assertRaises(EmptyStringException):
      textObject.description=""

