# test_blockcore.py
"""
Tests for BlockCore module.
"""

import unittest
from blockcore import BlockCore

class TestBlockCore(unittest.TestCase):
    """Test cases for BlockCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockCore()
        self.assertIsInstance(instance, BlockCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
