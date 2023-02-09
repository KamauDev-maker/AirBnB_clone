import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test Cases
    """
    
    def test_init(self):
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="Wileli", location="Naivasha")
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b2.id, str)
        self.assertEqual(b2_uuid, b2.id)
        self.assertEqual(b2.location, "Naivasha")
        self.assertEqual(b2.name, "Wileli")
        self.assertIsInstance(b1.created_at, datetime)
        
    
    def test_dict(self):
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="Wileli", location="Naivasha")
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id',b1_dict.keys())
        self.assertIn('created_at',b1_dict.keys())
        self.assertIn('updated_at',b1_dict.keys())

if __name__ == "__main__":
    unittest.main()       
    