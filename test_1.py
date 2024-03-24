import unittest
from models.base_model import BaseModel


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_to_dict(self):
        self.assertTrue(self.model.to_dict() != {""})


if __name__ == '__main__':
    unittest.main()