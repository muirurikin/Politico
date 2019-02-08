import json
import unittest

from run import app

class TestParty(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.client = self.app.test_client()
    self.data = {
      "id": 0,
      "name": "Wiper",
      "address": "Kitui",
      "logo": "https://www.google.com/images/wiper.png"
    }

  def test_getting_all_parties(self):
    res = self.client.get(path='/api/v1/parties', content_type='application/json')
    self.assertEqual(res.status_code, 200)



    
if __name__ == "__main__":
    unittest.main()
