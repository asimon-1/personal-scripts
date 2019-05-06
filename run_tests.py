"""Discovers and runs functions that "look like tests"
    Name test directories starting with "test"
    Test classes should be subclasses of unittest.TestCase and named starting with "Test"
    Name test methods starting with "test_"
    Make sure all packages with test code have an "init.py" file even if it is empty
"""
import nose

if __name__ == '__main__':
    nose.main()
