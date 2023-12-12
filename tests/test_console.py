#!/usr/bin/python3
"""Test for the console using several technoque"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class test console."""

    def create(self):
        """create the intance"""
        return HBNBCommand()

    def test_quit(self):
        """ test for the method to quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test for the method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
