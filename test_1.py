"""This module contains tests for the BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestModel(unittest.TestCase):
    """testing the base model"""

    def setUp(self):
        """set public properties"""

        self.model = BaseModel()

    def test_to_dict(self):
        """testing the to_dict method"""
        self.assertTrue(self.model.to_dict() != {""})


if __name__ == '__main__':
    unittest.main()
