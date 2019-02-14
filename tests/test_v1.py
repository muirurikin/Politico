import json
import unittest

from run import app


class TestParty(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {
          "name": "Wiper",
          "address": "Kitui",
          "logo": "https://www.google.com/images/wiper.png"
        }
        self.update_data = {
          "name": "Wiper Party",
          "address": "Kitui",
          "logo": "https://www.google.com/images/wiper.png"
        }

    def post(self, path='/api/v1/parties', data={}):
        if not data:
            data = self.data

        response = self.client.post(path, data=json.dumps(self.data), content_type='application/json')
        return response

    def test_getting_all_parties(self):
        res = self.client.get(path='/api/v1/parties')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json, self.data)

    def test_post_party(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)
        self.assertTrue(res.json['message'])

    def test_get_party_by_id(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)
        p_id = int(res.json['id'])
        path = '/api/v1/parties/%d' % p_id
        resp = self.client.get(path, content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_update_party(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)
        p_id = int(res.json['id'])
        path = '/api/v1/parties/%d' % p_id
        resp = self.client.patch(path, data=json.dumps(self.update_data), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json['name'], 'Wiper Party')

    def test_delete_party(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)
        p_id = int(res.json['id'])
        path = '/api/v1/parties/%d' % p_id
        resp = self.client.delete(path, content_type='application/json')
        self.assertEqual(resp.status_code, 202)


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {
            "name": "Senator",
            "type": "local govt"
        }

    def post(self, path='/api/v1/offices', data={}):
        if not data:
            data = self.data

        response = self.client.post(path, data=json.dumps(self.data), content_type='application/json')
        return response

    def test_getting_all_offices(self):
        res = self.client.get(path='/api/v1/offices')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json, self.data)

    def test_post_office(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)
        self.assertTrue(res.json['Message'], 'Office Info Added')
        self.assertTrue(res.json['office_id'])

    def test_get_office_by_id(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)
        o_id = int(res.json['office_id'])
        path = '/api/v1/offices/%d' % o_id
        resp = self.client.get(path, content_type='application/json')
        self.assertEqual(resp.status_code, 200)

if __name__ == "__main__":
    unittest.main()
