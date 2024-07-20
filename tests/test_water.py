import unittest
from .src.AHH import create_header

# how to make a test 😱😱

class TestScript(unittest.TestCase):
    def test_main(self):
        # Here, you would add tests for your main function
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()