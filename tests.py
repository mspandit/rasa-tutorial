import unittest
import requests
   
BASEURL = "http://localhost:5005/"
WEBHOOKURL = "http://localhost:5005/webhooks/rest/webhook"

class TestServer(unittest.TestCase):
   """docstring for TestServer"""

   # start server with rasa run --endpoints endpoints.yml -vv --enable-api
   def test_health_check(self):
      self.assertEqual(requests.get(BASEURL).content, b'Hello from Rasa: 1.3.3')

   def test_version_check(self):
      """docstring for test_version_check"""
      headers = {'Accept': 'application/json'}
      self.assertEqual(
         requests.get(BASEURL + "version", headers=headers).content, 
         b'{"version":"1.3.3","minimum_compatible_version":"1.3.0a2"}')

   def test_start_conversation(self):
      """docstring for test_start_conversation"""
      self.assertEqual(
         requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"Hi there!\" }").content, 
         b'[{"recipient_id":"Rasa","text":"Hey! How are you?"}]')
      self.assertEqual(
         requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"Sad.\" }").content,
         b'[{"recipient_id":"Rasa","text":"Here is something to cheer you up:"},{"recipient_id":"Rasa","image":"https:\\/\\/i.imgur.com\\/nGF1K8f.jpg"},{"recipient_id":"Rasa","text":"Did that help you?"}]')
      self.assertEqual(
         requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"Yes.\" }").content,
         b'[{"recipient_id":"Rasa","text":"Great, carry on!"}]')

   def test_nnp_conversation(self):
      """docstring for test_nnp_conversation"""
      self.assertEqual(
         requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"What's new?\" }").content,
         b'[{"recipient_id":"Rasa","text":"Intel made an important announcement at Hot Chips 2019 on August 20th."}]'
      )
      self.assertTrue(b"NNP-T for training and the NNP-I for inference" in requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"Oh\" }").content)
      self.assertTrue(b"NNP-I" in requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"NNP I\" }").content)
      self.assertTrue(b"NNP-I" in requests.post(WEBHOOKURL, data="{ \"sender\": \"Rasa\", \"message\": \"What else?\" }").content)
      
if __name__ == '__main__':
    unittest.main()
