import unittest
import my_python_file


class Test_my_func1(unittest.TestCase):
    def setUp(self):
        """This method is run before each test.
        Useful for common configuration steps."""
        pass

    def tearDown(self):
        """The method is run after each test.
        Useful for cleaning up any extra running processes."""
        pass

    def test_my_func_returns_true(self):
        """Tests that my_func returns True"""
        self.assertTrue(my_python_file.my_func())  # Return true with no arguments
        self.assertTrue(my_python_file.my_func('Cat'))  # Return true with a positional string
        self.assertTrue(my_python_file.my_func(animal='Cat'))  # Return true with a keyword

    def test_my_func_returns_false(self):
        """Tests that my_func returns False"""
        self.assertFalse(my_python_file.my_func(False))  # Return false with a positional argument
        self.assertFalse(my_python_file.my_func('Cat', 5, False))  # Return false with several positional arguments
        self.assertFalse(my_python_file.my_func(False, animal='Cat'))  # Return false with a keyword

    def test_my_func_exception(self):
        """Tests that my_func raises an exception."""
        try:
            my_python_file.my_func("Error")  # Raise a RuntimeError
        except Exception as e:
            self.assertIsInstance(e, RuntimeError)

    def test_my_func_return_none(self):
        """Tests that my_func returns None. THIS TEST IS DESIGNED TO FAIL"""
        # Note that my_func never returns None, so this test will fail.
        self.assertIsNone(my_python_file.my_func())
