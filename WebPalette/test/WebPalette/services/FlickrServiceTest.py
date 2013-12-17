'''
Created on Jan 2, 2012

@author: miria
'''
import time
import unittest
from WebPalette.services.FlickrService import FlickrService
from WebPalette.services.Providers import FileProvider


class FlickrServiceTest(unittest.TestCase):

    def testInterestingImages(self):
        '''
        Image 4 has no URL, image 5 is private
        '''
        provider = FileProvider("data/flickr/good_results.txt")
        service = FlickrService(provider=provider)
        images = service.get_photos()
        self.assertEquals(len(images), 3)
        self.assertEquals([i['image_id'] for i in images], ['1111', '2222', '3333'])
        self.assertEquals(provider.get_URL(), 'http://api.flickr.com/services/rest/?'+
            'sort=interestingness-desc&min_upload_date='+str(int(time.time()-60*60*24))+'&'+
            'license=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8&format=json&safe_search=1&nojsoncallback=1'+
            '&page=1&extras=url_l%2Cowner_name%2Clicense&content_type=1&per_page=500&'+
            'api_key=None&method=flickr.photos.search')
        
    def testInterestingImagesBadResponse(self):
        service = FlickrService(provider=FileProvider("data/flickr/bad_results.txt"))
        self.assertRaises(Exception, service.get_photos)


if __name__ == "__main__":
    unittest.main()