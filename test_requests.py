import json

import unittest
import requests

TEST_IP = 'http://0.0.0.0:5000'

class TestRequests(unittest.TestCase):
    def test_csv_with_extension(self):
        url = 'https://raw.githubusercontent.com/vitururu/photoslurp/master/test_files/photo_export.csv'
        response = requests.get(TEST_IP, params = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'csv'}
        self.assertEqual(response, correct_response)

    def test_tsv_with_extension(self):
        url = 'https://raw.githubusercontent.com/vitururu/photoslurp/master/test_files/example_feed.tsv'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'tsv'}
        self.assertEqual(response, correct_response)

    def test_xml_with_extension(self):
        url = 'https://raw.githubusercontent.com/vitururu/photoslurp/master/test_files/test.xml'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'xml'}
        self.assertEqual(response, correct_response)

    def test_csv_without_extension(self):
        url = 'https://raw.githubusercontent.com/vitururu/photoslurp/master/test_files/photo_export_csv'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'csv'}
        self.assertEqual(response, correct_response)

    def test_tsv_without_extension(self):
        url = 'https://www.dropbox.com/s/82epqwb1ogbbx49/example_feed_tsv.txt'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'tsv'}
        self.assertEqual(response, correct_response)

    def test_xml_without_extension(self):
        url = 'https://raw.githubusercontent.com/vitururu/photoslurp/master/test_files/test_xml'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'xml'}
        self.assertEqual(response, correct_response)

    def test_return_error(self):
        url = 'https://raw.githubusercontent.com/vitururu/photoslurp/master/test_files/favicon.ico'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, "error": "File format unknown or not recognizable."}
        self.assertEqual(response, correct_response)




if __name__ == '__main__':
    unittest.main()