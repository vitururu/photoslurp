import json

import unittest
import requests

TEST_IP = 'http://0.0.0.0:5000'

class TestRequests(unittest.TestCase):
    def test_csv_with_extension(self):
        url = 'https://www.indiandcold.com/media/photo_export.csv'
        response = requests.get(TEST_IP, params = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'csv'}
        self.assertEqual(response, correct_response)

    def test_tsv_with_extension(self):
        url = 'https://www.dropbox.com/s/6wgcp2wyl2p71q8/example_feed.tsv'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'tsv'}
        self.assertEqual(response, correct_response)

    def test_xml_with_extension(self):
        url = 'https://www.w3schools.com/xml/note.xml'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'xml'}
        self.assertEqual(response, correct_response)

    def test_csv_without_extension(self):
        url = 'https://www.dropbox.com/s/8n9c8nvw3w1j2n6/photo_export_csv.txt'
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
        url = 'https://www.dropbox.com/s/73gf13hqh31k11s/test_xml.txt'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, 'format': 'xml'}
        self.assertEqual(response, correct_response)

    def test_return_error(self):
        url = 'https://www.dropbox.com/s/8m11j7vmq7cpbx0/VERTICAL.gpx'
        response = requests.get(TEST_IP, data = {'url':url})
        response = json.loads(response.content)
        correct_response = {'url': url, "error": "File format unknown or not recognizable."}
        self.assertEqual(response, correct_response)




if __name__ == '__main__':
    unittest.main()