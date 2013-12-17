'''
Created on Feb 22, 2012

@author: miria
'''
import unittest
from WebPalette.data import Image
from WebPalette.processor import ColorProcessor


class ColorProcessorTest(unittest.TestCase):

    def testName(self):
        pass

    def setUp(self):
        self._processor = ColorProcessor()
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
    
    def testSetTopColors(self):
        images = [self.image1, self.image2]
        new_images = self._processor.set_top_colors(images)
        self.assertEquals(len(new_images), 1)
        self.assertEquals(new_images[0]['image_id'], "1")
    
    
    def testGetColors(self):  
        (dark, mid, light) = self._processor.get_colors(self.image1)
        self.assertEquals(dark[0], (19,17,18))
        self.assertEquals(mid[0], (150, 151, 137))
        self.assertEquals(light[0], (200, 201, 205))
        
    def testGetColorsIncompleteColors(self):
        (dark, mid, light) = self._processor.get_colors(self.image2)
        self.assertEquals(dark[0], (1,1,1))
        self.assertEquals(len(mid), 0)
        self.assertEquals(len(light), 0)
        
    
    def testGetSaturation(self):
        self.assertEquals(self._processor.get_saturation((255,255,255)), 255)
        self.assertEquals(self._processor.get_saturation((0,0,0)), 0)
        self.assertEquals(self._processor.get_saturation((121,203,006)), 156)

    
    def testGetWebColor(self):
        self.assertEquals(self._processor.get_web_color((255,255,255)), "#ffffff")
        self.assertEquals(self._processor.get_web_color((0,0,0)), "#000000")
        self.assertEquals(self._processor.get_web_color((121,203,006)), "#79cb06")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()