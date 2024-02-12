#!/usr/bin/bash
"""
Test cases for console
"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """
    Unit tests for console.py
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.console = HBNBCommand()

    def test_prompt_string(self):
        """
        Test if the prompt is correctly set
        """
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_empty_line(self):
        """
        Test if an empty line plus ENTER should do nothing
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """
        Test quit command
        """
        self.assertTrue(self.console.do_quit(None))

    def test_EOF(self):
        """
        Test EOF command
        """
        self.assertTrue(self.console.do_EOF(None))

    def test_help(self):
        """
        Test help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_help(None)
            output = f.getvalue()
            self.assertTrue('Documented commands' in output)

    def tearDown(self):
        """
        Tear down the test case.
        """
        self.console = None


if __name__ == '__main__':
    unittest.main()
