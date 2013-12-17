'''
Created on Feb 22, 2012

@author: miria
'''
import unittest
from WebPalette.data import Image

class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def setUp(self):
        self.image1 = Image(url="mine", title="something", attribution="me", image_id="1", 
                    owner_id="1234", height=5, width=5, source='123', path="data/images/kitty.jpg")
        self.image2 = Image(url="mine", title="something", attribution="me", image_id="2", 
                    owner_id="1234", height=5, width=5, source='123', path="data/images/black.jpg")

    
    def testDownloadImages(self):
        pass
    
    def testCropImages(self):
        images = [self.image1, self.image2]
        images[0]['path'] = 'todo copy the image somewhere else'
        #also to do - compare with cropped copy?

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()