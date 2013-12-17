import unittest
import WebPalette.services.Providers as Providers
from WebPalette.services.Providers import HTTPProvider, FileProvider

class ProviderTests(unittest.TestCase):
    
    def testHTTPProvider(self):
        provider = HTTPProvider()
        data = provider.fetch_data('http://www.example.com', param1='this', param2='that')
        self.assertTrue(data.startswith('<!DOCTYPE'))
        
    def testFileProvider(self):
        provider = FileProvider("data/flickr/bad_results.txt")
        data = provider.fetch_data('http://www.example.com', param1='this', param2='that')
        self.assertTrue(data.startswith('{"stat":"fail",')) 
        
    def testBuildURL(self):
        url = Providers.build_URL("http://www.example.com", {"param1":["this", "that"], "param2":4})
        self.assertEquals(url, "http://www.example.com?param2=4&param1=this&param1=that") 
    
if __name__ == "__main__":
    unittest.main()